# Configuration

We recommend that you keep all configuration files in the `conf/` directory of a Kedro project. However, if you prefer, you may point Kedro to any other directory and change the configuration paths by overriding `CONF_ROOT` variable from the derived ProjectContext class in `src/kedro_training/run.py` as follows:

```python
class ProjectContext(KedroContext):
    CONF_ROOT = "new_conf_root"

    ...
```

## Loading configuration

Kedro ships a purpose-built `ConfigLoader` class that helps you load configuration from various file formats including: YAML, JSON, INI, Pickle, XML and more.

When searching for the configs, `ConfigLoader` does that in the specified config environments, `base` and `local` by default, which represent the directories inside your root config directory.

Here is an example of how to load configuration for your `DataCatalog`:

```python
from kedro.config import ConfigLoader

conf_envs = ["conf/base", "conf/local"]  # ConfigLoader will search for configs in these directories
conf_loader = ConfigLoader(conf_envs)
conf_catalog = conf_loader.get("catalog*", "catalog*/**")  # returns a dictionary
```

`ConfigLoader` will recursively scan for configuration files firstly in `conf/base/` and then in `conf/local/` directory according to the following rules:
1. The filename starts with `catalog` OR the file is located in a sub-directory which has a name that is prefixed with `catalog`
2. AND the file extension is one of the following: `yaml`, `yml`, `json`, `ini`, `pickle`, `xml`, `properties` or `shellvars`

Configuration data from the files that match these rules will be merged at runtime and returned in the form of a Python dictionary.

> Note: Any top-level keys that start with `_` character are considered hidden (or reserved) and therefore are ignored right after the config load. Those keys will neither trigger a key duplication error mentioned above, nor will they appear in the resulting configuration dictionary. However, you may still use such keys for various purposes. For example, as [YAML anchors and aliases](https://confluence.atlassian.com/bitbucket/yaml-anchors-960154027.html)

* If any 2 different config files located inside the _same_ environment (`base` or `local` here) contain the same top-level key, load_config will raise a `ValueError` indicating that the duplicates are not allowed.
* If 2 different config files have duplicate top-level keys, but are located in _different_ environments (one in `base`, another in `local`, for example) then the last loaded path (`local` in this case) takes precedence and _overrides_ that key value. No errors are raised in this case, however a DEBUG level log message will be emitted with the information on the over-ridden keys.
* If the same environment path is passed multiple times, a `UserWarning` will be emitted to draw attention to the duplicate loading attempt, and any subsequent loading after the first one will be skipped.

## Additional config environments

In addition to the 2 built-in configuration environments, it is possible to create your own. Your project loads `base` as the bottom-level configuration environment but allows you to overwrite it with any other environments that you create. Any additional configuration environments can be created inside `conf` folder and applied to your pipeline run as follows:

```bash
kedro run --env <environment-name>
```

If no `env` option is specified, this will default to `local` environment to overwrite `base`.

## Templating configuration

Kedro also provides an extension `kedro.config.TemplatedConfigLoader` class that allows to template values in your configuration files. To apply `TemplatedConfigLoader` to your `ProjectContext` in `src/kedro_training/run.py`, you will need to overwrite the `_create_config_loader` method as follows:

```python
...
from kedro.config import TemplatedConfigLoader  # new import


class ProjectContext(KedroContext):
    ...

    def _create_config_loader(self, conf_paths: Iterable[str]) -> TemplatedConfigLoader:
        return TemplatedConfigLoader(
            conf_paths,
            globals_pattern="*globals.yml",  # read the globals dictionary from project config
            globals_dict={  # extra keys to add to the globals dictionary, take precedence over globals_pattern
                "bucket_name": "another_bucket_name",
                "non_string_key": 10
            }
        )
```

Let's assume the project contains a `conf/base/globals.yml` file with the following contents:

```yaml
bucket_name: "my_s3_bucket"
key_prefix: "my/key/prefix/"

datasets:
    csv: "pandas.CSVDataSet"
    spark: "spark.SparkDataSet"

folders:
    raw: "01_raw"
    int: "02_intermediate"
    pri: "03_primary"
    fea: "04_features"
```

The contents of the dictionary resulting from the `globals_pattern` get merged with the `globals_dict`. In case of conflicts, the keys from the `globals_dict` take precedence. The resulting global dictionary prepared by `TemplatedConfigLoader` will look like this:

```python
{
    "bucket_name": "another_bucket_name",
    "non_string_key": 10,
    "key_prefix": "my/key/prefix",
    "datasets": {
        "csv": "pandas.CSVDataSet",
        "spark": "spark.SparkDataSet"
    },
    "folders": {
        "raw": "01_raw",
        "int": "02_intermediate",
        "pri": "03_primary",
        "fea": "04_features"
    }
}
```

Now the templating can be applied to the configs. Here is an example of templated `catalog.yml`:

```yaml
raw_boat_data:
    type: "${datasets.spark}"  # nested paths into global dict are allowed
    filepath: "s3a://${bucket_name}/${key_prefix}/${folders.raw}/boats.csv"
    file_format: parquet

raw_car_data:
    type: "${datasets.csv}"
    filepath: "data/${key_prefix}/${folders.raw}/cars.csv"
    bucket_name: "${bucket_name}"
    file_format: "${non.existent.key|parquet}"  # default to 'parquet' if the key is not found
```

> Note: `TemplatedConfigLoader` uses `jmespath` package in the background to extract elements from global dictionary. For more information about JMESPath syntax please see: https://github.com/jmespath/jmespath.py.

### Next section
[Go to the next section](./12_transcoding.md)
