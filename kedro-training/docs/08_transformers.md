# Kedro transformers

[Transformers](https://kedro.readthedocs.io/en/stable/04_user_guide/04_data_catalog.html#transforming-datasets) intercept the load and save operations on Kedro `DataSet`s. Some use cases that transformers enable include: performing data validation, tracking operation performance and converting a data format (although we would recommend [Transcoding](https://kedro.readthedocs.io/en/stable/04_user_guide/04_data_catalog.html#transcoding-datasets) for this). We will cover _tracking operation performance_ with the following:
1. Applying built-in transformers for monitoring load and save operation latency
2. Developing our own transformer for tracking memory consumption

## Applying built-in transformers

Transformers are applied at the `DataCatalog` level. To apply the built-in `ProfileTimeTransformer`, you need to:
1. Navigate to `src/kedro_training/run.py`
2. Override `_create_catalog` method for your `ProjectContext` class using the following:

```python
from typing import Dict, Any

from kedro.context import KedroContext
from kedro.extras.transformers import ProfileTimeTransformer  # new import
from kedro.io import DataCatalog
from kedro.versioning import Journal


class ProjectContext(KedroContext):

    ...

    def _create_catalog(
        self,
        conf_catalog: Dict[str, Any],
        conf_creds: Dict[str, Any],
        save_version: str = None,
        journal: Journal = None,
        load_versions: Dict[str, str] = None,
    ) -> DataCatalog:
        catalog = DataCatalog.from_config(
            conf_catalog,
            conf_creds,
            save_version=save_version,
            journal=journal,
            load_versions=load_versions,
        )
        profile_time = ProfileTimeTransformer()  # instantiate a build-in transformer
        catalog.add_transformer(profile_time)  # apply it to the catalog
        return catalog
```

Once complete, rerun the pipeline from the terminal and you should see the following logging output:

```bash
$ kedro run

...
2019-11-13 15:09:01,784 - kedro.io.data_catalog - INFO - Loading data from `companies` (CSVDataSet)...
2019-11-13 15:09:01,827 - ProfileTimeTransformer - INFO - Loading companies took 0.043 seconds
2019-11-13 15:09:01,828 - kedro.pipeline.node - INFO - Running node: preprocess1: preprocess_companies([companies]) -> [preprocessed_companies]
2019-11-13 15:09:01,880 - kedro_tutorial.nodes.data_engineering - INFO - Running 'preprocess_companies' took 0.05 seconds
2019-11-13 15:09:01,880 - kedro_tutorial.nodes.data_engineering - INFO - Running 'preprocess_companies' took 0.05 seconds
2019-11-13 15:09:01,880 - kedro.io.data_catalog - INFO - Saving data to `preprocessed_companies` (CSVDataSet)...
2019-11-13 15:09:02,112 - ProfileTimeTransformer - INFO - Saving preprocessed_companies took 0.232 seconds
2019-11-13 15:09:02,113 - kedro.runner.sequential_runner - INFO - Completed 1 out of 6 tasks
...
```

You can notice 2 new `INFO` level log messages from `ProfileTimeTransformer`, which report the corresponding dataset load and save operation latency.

> Pro Tip: You can narrow down the application of the transformer by specifying an optional list of the datasets in `add_transformer`. For example, the command `catalog.add_transformer(profile_time, ["dataset1", "dataset2"])` will apply `profile_time` transformer _only_ to the datasets named `dataset1` and `dataset2`. This may be useful when you need to apply a transformer only to a subset of datasets, rather than all of them.

## Developing your own transformer

Let's create our own transformer using [memory-profiler](https://github.com/pythonprofilers/memory_profiler). Custom transformer should:
1. Inherit the `kedro.io.AbstractTransformer` base class
2. Implement the `load` and `save` method (as show in the example below)

Now please create `src/kedro_training/memory_profile.py` and then paste the following code into it:

```python
import logging
from typing import Callable, Any

from kedro.io import AbstractTransformer
from memory_profiler import memory_usage


def _normalise_mem_usage(mem_usage):
    # memory_profiler < 0.56.0 returns list instead of float
    return mem_usage[0] if isinstance(mem_usage, (list, tuple)) else mem_usage


class ProfileMemoryTransformer(AbstractTransformer):
    """ A transformer that logs the maximum memory consumption during load and save calls """

    @property
    def _logger(self):
        return logging.getLogger(self.__class__.__name__)

    def load(self, data_set_name: str, load: Callable[[], Any]) -> Any:
        mem_usage, data = memory_usage(
            (load, [], {}),
            interval=0.1,
            max_usage=True,
            retval=True,
            include_children=True,
        )
        # memory_profiler < 0.56.0 returns list instead of float
        mem_usage = _normalise_mem_usage(mem_usage)

        self._logger.info(
            "Loading %s consumed %2.2fMiB memory at peak time", data_set_name, mem_usage
        )
        return data

    def save(self, data_set_name: str, save: Callable[[Any], None], data: Any) -> None:
        mem_usage = memory_usage(
            (save, [data], {}),
            interval=0.1,
            max_usage=True,
            retval=False,
            include_children=True,
        )
        mem_usage = _normalise_mem_usage(mem_usage)

        self._logger.info(
            "Saving %s consumed %2.2fMiB memory at peak time", data_set_name, mem_usage
        )
```

Finally, you need to update `ProjectContext._create_catalog` method definition to apply your custom transformer:

```python

...
from .memory_profile import ProfileMemoryTransformer  # new import


class ProjectContext(KedroContext):

    ...

    def _create_catalog(
        self,
        conf_catalog: Dict[str, Any],
        conf_creds: Dict[str, Any],
        save_version: str = None,
        journal: Journal = None,
        load_versions: Dict[str, str] = None,
    ) -> DataCatalog:
        catalog = DataCatalog.from_config(
            conf_catalog,
            conf_creds,
            save_version=save_version,
            journal=journal,
            load_versions=load_versions,
        )
        profile_time = ProfileTimeTransformer()
        catalog.add_transformer(profile_time)

        profile_memory = ProfileMemoryTransformer()  # instantiate our custom transformer
        # as memory tracking is quite time-consuming, for the demonstration purposes
        # let's apply profile_memory only to the master_table
        catalog.add_transformer(profile_memory, "master_table")
        return catalog
```

And rerun the pipeline:

```bash
$ kedro run

...
2019-11-13 15:55:01,674 - kedro.io.data_catalog - INFO - Saving data to `master_table` (CSVDataSet)...
2019-11-13 15:55:12,322 - ProfileMemoryTransformer - INFO - Saving master_table consumed 606.98MiB memory at peak time
2019-11-13 15:55:12,322 - ProfileTimeTransformer - INFO - Saving master_table took 10.648 seconds
2019-11-13 15:55:12,357 - kedro.runner.sequential_runner - INFO - Completed 3 out of 6 tasks
2019-11-13 15:55:12,358 - kedro.io.data_catalog - INFO - Loading data from `master_table` (CSVDataSet)...
2019-11-13 15:55:13,933 - ProfileMemoryTransformer - INFO - Loading master_table consumed 533.05MiB memory at peak time
2019-11-13 15:55:13,933 - ProfileTimeTransformer - INFO - Loading master_table took 1.576 seconds
...
```

### Next section
[Go to the next section](./09_versioning.md)
