# Create a new project

To create a Kedro project using the _interactive_ mode, run:

```bash
kedro new
```

This will ask you to specify:
1. Project name - you can call it `Kedro Training`
2. Repository name - accept the default
3. Python package name - accept the default
4. Whether you want an example pipeline to be generated for you - type in `y`

Alternatively, a Kedro project can be created in _non-interactive_ mode by calling

```bash
kedro new -c `<config.yml>`
```

where `<config.yml>` is a path to a YAML file with the following:

```yaml
output_dir: ~/code  # this directory must exist
project_name: Kedro Training
repo_name: kedro-training
python_package: kedro_training
include_example: true
```

This might be useful when you want to programmatically create your project as part of environment configuration or continuous integration script, for example.

## Project structure

Once you have successfully run `kedro new`, you should get the following project structure:

<details>
<summary><b>CLICK TO EXPAND</b></summary>

```console
kedro-training
├── conf
│   ├── base
│   │   ├── catalog.yml
│   │   ├── credentials.yml
│   │   ├── logging.yml
│   │   └── parameters.yml
│   ├── local
│   └── README.md
├── data
│   ├── 01_raw
│   │   └── iris.csv
│   ├── 02_intermediate
│   ├── 03_primary
│   ├── 04_features
│   ├── 05_model_input
│   ├── 06_models
│   ├── 07_model_output
│   └── 08_reporting
├── docs
├── logs
├── notebooks
├── references
├── results
├── src
│   ├── kedro_training
│   │   ├── nodes
│   │   │   └── __init__.py
│   │   ├── pipelines
│   │   │   ├── data_engineering
│   │   │   │   ├── README.md
│   │   │   │   ├── __init__.py
│   │   │   │   ├── nodes.py
│   │   │   │   └── pipeline.py
│   │   │   ├── data_science
│   │   │   │   ├── README.md
│   │   │   │   ├── __init__.py
│   │   │   │   ├── nodes.py
│   │   │   │   └── pipeline.py
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── pipeline.py
│   │   └── run.py
│   ├── tests
│   ├── requirements.txt
│   └── setup.py
├── README.md
├── kedro_cli.py
└── setup.cfg
```
</details>

This structure may seem overwhelming at the first glance, but rest assured that you will master it very quickly. Also please bear in mind that this structure intends to fit most analytics projects and is a result of the lessons learned from a number of QuantumBlack's analytics studies. Therefore certain sections may not be applicable for your specific use cases. In the next section we will break down those components into 3 categories:
1. _core_ components that are essential for Kedro project
2. the ones that are _nice to have_, so we strongly recommend using them
3. _non-essential_ components that can be amended / removed without breaking the project

### Folder structure

| Folder | Description | Priority |
| ------ | ----------- | -------- |
| `conf` | The `conf` directory is the place where all your project configuration is located. Kedro has a powerful built-in mechanism for loading configuration. Using `conf` encourages a clear and strict separation between project code and configuration. | Core |
| `data` | A place to store _local_ project data according to a suggested [Data Engineering Convention](https://kedro.readthedocs.io/en/stable/06_resources/01_faq.html#what-is-data-engineering-convention). For production workloads we do not recommend storing data locally, but rather utilising cloud storage (AWS S3, Azure Blob Storage), distributed file storage or database interfaces through Kedro's Data Catalog | Non-essential |
| `docs` | `docs` is where your auto-generated project documentation is saved | Nice to have |
| `logs` | A directory for your Kedro pipeline execution logs | Nice to have |
| `notebooks` |  Kedro supports a Jupyter workflow, that allows you to experiment and iterate quickly on your models. `notebooks` is the folder where you can store your Jupyter Notebooks | Nice to have |
| `references`<br/><br/>`results` | Auxiliary folders for project references and standalone results like model artifacts, plots, papers and statistics | Non-essential
| `src` | Source directory that contains all your pipeline code | Core |

#### `src` folder

Source folder by default contains the following components:
1. Your Kedro project Python package - `kedro_training` in this case
2. `tests` folder with example unit tests; newly generated projects are preconfigured to run these tests using the [pytest framework](https://docs.pytest.org/en/stable/)
3. `requirements.txt` file that contains all Python package dependencies
4. `setup.py` - used by [Python Distutils](https://docs.python.org/3/library/distutils.html) for packaging the project

### Python package

A Kedro project is generated in the form of a [Python package](https://packaging.python.org/tutorials/packaging-projects/). Here are the most important building blocks:

1. `nodes/` - a sub-package containing global nodes, i.e. nodes that are applicable to any pipeline
2. `pipelines/` - a sub-package containing modular pipelines
3. `pipeline.py` - a master pipeline that helps you assemble sub-pipelines found in `pipelines/`
4. `run.py` - contains the `ProjectContext` definition, the backbone of Kedro project architecture and the main application entry point

## Running Kedro commands

The list and the behaviour of Kedro CLI commands may vary depending of the working directory where Kedro command is executed. Kedro has 2 command types:

* global commands (e.g., `kedro new`, `kedro info`) which work regardless of the current working directory
* local or project-specific commands (e.g., `kedro run`, `kedro install`) that require the current working directory to be the root of your Kedro project

To see the full list of available commands, you can always run `kedro --help`.

### `kedro install`

This command allows you to easily install or update all your project third-party Python package dependencies. This is roughly equivalent to `pip install -r src/requirements.txt`, however `kedro install` is a bit smarter on Windows when it needs to upgrade its version. It also makes sure that the dependencies are always installed in the same virtual environment as Kedro.

One more very useful command is `kedro build-reqs`, which takes `requirements.in` file (or `requirements.txt` if the first one does not exist), resolves all package versions and 'freezes' them by putting pinned versions back into `requirements.txt`. It significantly reduces the chances of dependencies issues due to downstream changes as you would always install the same package versions.

#### Example

Let's install and try the [Kedro Viz](https://github.com/quantumblacklabs/kedro-viz) - the plugin that helps a lot visualising your Kedro pipelines. You can do this by running the following commands from the terminal:

```bash
echo "kedro-viz>=3.0" >> src/requirements.txt  # src\requirements.txt on Windows
kedro build-reqs  # creates src/requirements.in and pins package versions in src/requirements.txt
kedro install  # installs packages from src/requirements.txt
kedro viz  # start Kedro Viz server
```

## Credentials management

For security reasons, we strongly recommend not committing any credentials or other secrets to the Version Control System. By default any file inside the `conf` folder (and subfolders) in your Kedro project containing `credentials` word in its name will be gitignored and not committed to your repository.

Please bear it in mind when you start working with Kedro project that you have cloned from GitHub, for example, as you might need to configure required credentials first. If you are a project maintainer, you should document it in project prerequisites.

On run Kedro automatically reads the credentials from the `conf` folder and feeds them into the DataCatalog - a Kedro component responsible for loading and saving of the data that comes to and out of pipeline nodes. Shortly, you just need to configure your credentials once and then you can reuse them in multiple datasets.

Example of `conf/local/credentials.yml`:

```yaml
dev_s3:
  aws_access_key_id: token
  aws_secret_access_key: key
```

Example of the dataset using those credentials defined in `conf/base/catalog.yml`:

```yaml
cars:
  type: CSVS3DataSet
  filepath: data/02_intermediate/company/cars.csv
  bucket_name: my_bucket
  credentials: dev_s3
```
