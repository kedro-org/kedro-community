
# Versioning

## Data versioning
Making a simple addition to your Data Catalog allows you to perform versioning of datasets and machine learning models.

Suppose you want to version `master_table`. To enable versioning, simply add a `versioned` entry in `catalog.yml` as follows:

```yaml
master_table:
  type: CSVLocalDataSet
  filepath: data/03_primary/master_table.csv
  versioned: true
```

The `DataCatalog` will create a versioned `CSVLocalDataSet` called `master_table`. The actual csv file location will look like `data/03_primary/master_table.csv/<version>/master_table.csv`, where the first `/master_table.csv/` is a directory and `<version>` corresponds to a global save version string formatted as `YYYY-MM-DDThh.mm.ss.sssZ`.

With the similar way, you can version your machine learning model. Enable versioning for `regressor` as follow:

```yaml
regressor:
  type: PickleLocalDataSet
  filepath: data/06_models/regressor.pickle
  versioned: true
```

This will save versioned pickle models everytime you run the pipeline.

> *Note:* The list of the datasets supporting versioning can be find in [the documentation](https://kedro.readthedocs.io/en/stable/04_user_guide/08_advanced_io.html#supported-datasets).

## Loading a versioned dataset
By default, the `DataCatalog` will load the latest version of the dataset. However, you can run the pipeline with a particular versioned data set with `--load-version` flag as follows:

```bash
kedro run --load-version="master_table:YYYY-MM-DDThh.mm.ss.sssZ"
```
where `--load-version` contains a dataset name and a version timestamp separated by `:`.


## Journal (code versioning)

Journal in Kedro allows you to save the history of pipeline runs. This functionality helps you reproduce results and gives you an ability to investigate failures in your workflow.
Each pipeline run creates a log file formatted as `journal_YYYY-MM-DDThh.mm.ss.sssZ.log`, which is saved in the `logs/journals` directory. The log file contains two kinds of journal records.

### Context journal record

A context journal record captures all the necessary information to reproduce the pipeline run and has the following JSON format:

```json
{
    "type": "ContextJournalRecord",
    "run_id": "2019-10-01T09.15.57.289Z",
    "project_path": "<path-to-project>/src/kedro-tutorial",
    "env": "local",
    "kedro_version": "0.15.4",
    "tags": [],
    "from_nodes": [],
    "to_nodes": [],
    "node_names": [],
    "from_inputs": [],
    "load_versions": {},
    "pipeline_name": null,
    "git_sha": "48dd0d3"
}
```

You will observe `run_id`, a unique timestamp used to identify a pipeline run, in the context journal record, as well as a `git_sha`, that corresponds to the current git commit hash when your project is tracked by `git`. If your project is not tracked by `git`, then the `git_sha` will be `null`, and you'll see a warning message in your `logs/info.log` as follows:

```bash
2019-10-01 10:31:13,352 - kedro.versioning.journal - WARNING - Unable to git describe /<path-to-project>/src/kedro-tutorial
```

### Dataset journal record

A dataset journal record tracks versioned dataset `load` and `save` operations, it is tied to the dataset name and `run_id`. The `version` attribute stores the exact timestamp used by the `load` or `save` operation. Dataset journal currently records `load` and `save` operations only for the datasets with enabled versioning.

The dataset journal record has the following JSON format:

```json
{
    "type": "DatasetJournalRecord",
    "run_id": "2019-10-01T09.15.57.289Z",
    "name": "example_train_x",
    "operation": "load",
    "version": "2019-10-01T09.15.57.289Z"
}
```

> ❗While the context journal record is always logged at every run time of your pipeline, dataset journal record is only logged when `load` or `save` method is invoked for versioned dataset in `DataCatalog`.

## Steps to manually reproduce your code and run the previous pipeline

Journals must be persisted to manually reproduce your specific pipeline run. You can keep journals corresponding to checkpoints in your development workflow in your source control repo. Once you have found a version you would like to revert to, follow the below steps:

1. Checkout a commit from `git_sha` in the context journal record by running the following `git` command in your terminal:
```bash
git checkout <git_sha>
```
> *Note:* If you want to go back to the latest commit in the current branch, you can run `git checkout <branch-name>`.

2. Verify that the installed Kedro version is the same as the `project_version` in `src/<project-package>/run.py` by running `kedro --version`.
    - If the installed Kedro version does not match the `project_version`, verify that there are no changes that affect your project between the different Kedro versions by looking at [`RELEASE.md`](https://github.com/quantumblacklabs/kedro/blob/master/RELEASE.md), then update the Kedro version by pinning the `kedro==project_version` in `requirements.txt` and run `kedro install` in your terminal.

3. Run the pipeline with the corresponding versioned datasets' load versions fixed. Open the corresponding journal log file found in `logs/journals`, find dataset journal record, list all the dataset load versions and run the following command in your terminal:
```bash
kedro run --load-version="dataset1:YYYY-MM-DDThh.mm.ss.sssZ" --load-version="dataset2:YYYY-MM-DDThh.mm.ss.sssZ"
```
where `--load-version` should contain a dataset name and load version timestamp separated by `:`.

### Next section
[Go to the next section](./10_package-project.md)
