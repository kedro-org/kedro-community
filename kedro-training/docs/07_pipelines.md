# Kedro pipelines

## Node basics

A `Node` in Kedro represents a class that facilitates the operations required to run user-provided functions as part of Kedro pipelines.

Let's create a file `src/kedro_training/pipelines/data_engineering/nodes.py` and add the following functions:

```python
import pandas as pd


def _is_true(x):
    return x == "t"


def _parse_percentage(x):
    if isinstance(x, str):
        return float(x.replace("%", "")) / 100
    return float("NaN")


def _parse_money(x):
    return float(x.replace("$", "").replace(",", ""))


def preprocess_companies(companies: pd.DataFrame) -> pd.DataFrame:
    """Preprocess the data for companies.

        Args:
            companies: Source data.
        Returns:
            Preprocessed data.

    """

    # This function should preprocess the 'companies' DataFrame by doing the following:
    # 1. Convert 'iata_approved' column to boolean by applying _is_true function inplace
    # 2. Convert 'company_rating' column to float by applying _parse_percentage function inplace

    return companies


def preprocess_shuttles(shuttles: pd.DataFrame) -> pd.DataFrame:
    """Preprocess the data for shuttles.

        Args:
            shuttles: Source data.
        Returns:
            Preprocessed data.

    """

    # This function should preprocess the 'shuttles' DataFrame by doing the following:
    # 1. Convert 'd_check_complete' and 'moon_clearance_complete' columns to boolean
    # by applying _is_true function inplace
    # 2. Convert 'price' column to float by applying _parse_money function inplace

    return shuttles


def create_master_table(
    shuttles: pd.DataFrame, companies: pd.DataFrame, reviews: pd.DataFrame
) -> pd.DataFrame:
    """Combines all data to create a master table.
        Args:
            shuttles: Preprocessed data for shuttles.
            companies: Preprocessed data for companies.
            reviews: Source data for reviews.
        Returns:
            Master table.
    """

    # This function should prepare the master table by doing the following:
    # 1. Join 'shuttles' with 'reviews' based on shuttle IDs
    # 2. Join the result of step 1 with 'companies' based on company IDs
    # 3. Drop 'shuttle_id' and 'company_id' columns from the resulting master table
    # 4. Drop NAs from the resulting master table

    return master_table
```

<details>
<summary><b>CLICK TO SEE THE ANSWER</b></summary>

```python
import pandas as pd


def _is_true(x):
    return x == "t"


def _parse_percentage(x):
    if isinstance(x, str):
        return float(x.replace("%", "")) / 100
    return float("NaN")


def _parse_money(x):
    return float(x.replace("$", "").replace(",", ""))


def preprocess_companies(companies: pd.DataFrame) -> pd.DataFrame:
    """Preprocess the data for companies.

        Args:
            companies: Source data.
        Returns:
            Preprocessed data.

    """

    companies["iata_approved"] = companies["iata_approved"].apply(_is_true)

    companies["company_rating"] = companies["company_rating"].apply(_parse_percentage)

    return companies


def preprocess_shuttles(shuttles: pd.DataFrame) -> pd.DataFrame:
    """Preprocess the data for shuttles.

        Args:
            shuttles: Source data.
        Returns:
            Preprocessed data.

    """
    shuttles["d_check_complete"] = shuttles["d_check_complete"].apply(_is_true)

    shuttles["moon_clearance_complete"] = shuttles["moon_clearance_complete"].apply(
        _is_true
    )

    shuttles["price"] = shuttles["price"].apply(_parse_money)

    return shuttles


def create_master_table(
    shuttles: pd.DataFrame, companies: pd.DataFrame, reviews: pd.DataFrame
) -> pd.DataFrame:
    """Combines all data to create a master table.
        Args:
            shuttles: Preprocessed data for shuttles.
            companies: Preprocessed data for companies.
            reviews: Source data for reviews.
        Returns:
            Master table.
    """
    rated_shuttles = shuttles.merge(reviews, left_on="id", right_on="shuttle_id")

    with_companies = rated_shuttles.merge(
        companies, left_on="company_id", right_on="id"
    )

    master_table = with_companies.drop(["shuttle_id", "company_id"], axis=1)
    master_table = master_table.dropna()
    return master_table
```
</details>

## Assemble nodes into a modular pipeline

### Creating the data engineering pipeline

You have utility functions and two processing functions, `preprocess_companies` and `preprocess_shuttles`, which take Pandas dataframes for `companies` and `shuttles` respectively and output preprocessed versions of those dataframes.

Next you should create the Data Engineering pipeline, which represents a collection of `Node` objects.  To do so, add the following code to `src/kedro_training/pipelines/data_engineering/pipeline.py`:

```python
from kedro.pipeline import Pipeline, node

from .nodes import preprocess_companies, preprocess_shuttles, create_master_table


def create_pipeline(**kwargs) -> Pipeline:
    """Create the project's pipeline.

    Args:
        kwargs: Ignore any additional arguments added in the future.

    Returns:
        Pipeline object.

    """

    # Here you need to construct a Data Engineering ('de_pipeline') object, which
    # satisfies the following requirements:
    # 1. Is an instance of a Pipeline class
    # 2. Contains 3 pipeline nodes:
    #   a. A node called 'preprocessing_companies' that maps 'companies'
    #      to 'preprocessed_companies' by using 'preprocess_companies' function from above
    #   b. A node called 'preprocessing_shuttles' that maps 'shuttles'
    #      to 'preprocessed_shuttles' by using 'preprocess_shuttles' function from above
    #   c. A node called 'creating_master_table' that takes 'preprocessed_shuttles',
    #      'preprocessed_companies' and 'reviews' as inputs and produces a single output
    #      called 'master_table' by using 'create_master_table' function from above

    return de_pipeline
```

<details>
<summary><b>CLICK TO SEE THE ANSWER</b></summary>

```python
from kedro.pipeline import Pipeline, node

from .nodes import preprocess_companies, preprocess_shuttles, create_master_table


def create_pipeline(**kwargs) -> Pipeline:
    """Create the project's pipeline.

    Args:
        kwargs: Ignore any additional arguments added in the future.

    Returns:
        Pipeline object.

    """
    de_pipeline = Pipeline(
        [
            node(
                func=preprocess_companies,
                inputs="companies",
                outputs="preprocessed_companies",
                name="preprocessing_companies"
            ),
            node(
                func=preprocess_shuttles,
                inputs="shuttles",
                outputs="preprocessed_shuttles",
                name="preprocessing_shuttles"
            ),
            node(
                func=create_master_table,
                inputs=["preprocessed_shuttles", "preprocessed_companies", "reviews"],
                outputs="master_table",
            ),
        ]
    )

    return de_pipeline
```
</details>

> Note: The `inputs` and `outputs` arguments are not passed into the underlying function as-is. Instead, Kedro locates the dataset with that name from `conf/base/catalog.yml`, loads it and passes the loaded data as the input for your function call. Outputs are handled similarly - Kedro captures all the outputs and saves them into the corresponding datasets.

To turn it into a Python package, create an empty file `src/kedro_training/pipelines/data_engineering/__init__.py`.

Finally, we need to register the newly created modular pipeline in `src/kedro_training/pipeline.py`:

```python
from typing import Dict

from kedro.pipeline import Pipeline

from kedro_training.pipelines import data_engineering as de


def create_pipelines(**kwargs) -> Dict[str, Pipeline]:
    """Create the project's pipeline.

    Args:
        kwargs: Ignore any additional arguments added in the future.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.

    """

    data_engineering_pipeline = de.create_pipeline()

    return {
        "de": data_engineering_pipeline,
        "__default__": data_engineering_pipeline,
    }
```

### Creating the data science pipeline

The data science pipeline is similar conceptually; it requires nodes and the pipeline definition.

Let's create `src/kedro_training/pipelines/data_science/nodes.py` and put the following code in it to create our nodes:

```python
import logging
from typing import Dict, List

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split


def split_data(data: pd.DataFrame, parameters: Dict) -> List:
    """Splits data into training and test sets.

        Args:
            data: Source data.
            parameters: Parameters defined in parameters.yml.
        Returns:
            A list containing split data.

    """

    # 1. Create X object that contains the following subset of the columns from 'data':
    # engines, passenger_capacity, crew, d_check_complete, moon_clearance_complete
    # 2. Take the values of 'price' column and put them into 'y' object
    # 3. Split X and y into train and test sets X_train, X_test, y_train, y_test by
    # using 'train_test_split' function and 'test_size' and 'random_state' parameters

    return [X_train, X_test, y_train, y_test]


def train_model(X_train: np.ndarray, y_train: np.ndarray) -> LinearRegression:
    """Train the linear regression model.

        Args:
            X_train: Training data of independent features.
            y_train: Training data for price.

        Returns:
            Trained model.

    """
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    return regressor


def evaluate_model(regressor: LinearRegression, X_test: np.ndarray, y_test: np.ndarray):
    """Calculate the coefficient of determination and log the result.

        Args:
            regressor: Trained model.
            X_test: Testing data of independent features.
            y_test: Testing data for price.

    """
    # 1. Calculate predictions for 'X_test' using 'regressor' object
    # 2. Calculate R^2 score for the calculated predictions
    # 3. Log calculated R^2 score. Hint:
    # logger = logging.getLogger(__name__)
    # logger.info(<Your message>)

```

<details>
<summary><b>CLICK TO SEE THE ANSWER</b></summary>

```python
import logging
from typing import Dict, List

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split


def split_data(data: pd.DataFrame, parameters: Dict) -> List:
    """Splits data into training and test sets.

        Args:
            data: Source data.
            parameters: Parameters defined in parameters.yml.
        Returns:
            A list containing split data.

    """

    X = data[
        [
            "engines",
            "passenger_capacity",
            "crew",
            "d_check_complete",
            "moon_clearance_complete",
        ]
    ].values
    y = data["price"].values
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )

    return [X_train, X_test, y_train, y_test]


def train_model(X_train: np.ndarray, y_train: np.ndarray) -> LinearRegression:
    """Train the linear regression model.

        Args:
            X_train: Training data of independent features.
            y_train: Training data for price.

        Returns:
            Trained model.

    """
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    return regressor


def evaluate_model(regressor: LinearRegression, X_test: np.ndarray, y_test: np.ndarray):
    """Calculate the coefficient of determination and log the result.

        Args:
            regressor: Trained model.
            X_test: Testing data of independent features.
            y_test: Testing data for price.

    """
    y_pred = regressor.predict(X_test)
    score = r2_score(y_test, y_pred)
    logger = logging.getLogger(__name__)
    logger.info("Model has a coefficient R^2 of %.3f.", score)
```
</details>

Then we have to build the data science pipeline definition in `src/kedro_training/pipelines/data_science/pipeline.py`:

```python
from kedro.pipeline import Pipeline, node

from .nodes import split_data, train_model, evaluate_model


def create_pipeline(**kwargs) -> Pipeline:
    """Create the project's pipeline.

    Args:
        kwargs: Ignore any additional arguments added in the future.

    Returns:
        Pipeline object.

    """

    # Here you need to construct a Data Science ('ds_pipeline') object, which satisfies
    # the following requirements:
    # 1. Is an instance of a Pipeline class
    # 2. Contains 3 pipeline nodes:
    #   a. Split data: a node that takes 'master_table' and 'parameters' as inputs and
    #   produces 4 objects: 'X_train', 'X_test', 'y_train', 'y_test' by using
    #   'split_data' function
    #   b. Train model: a node that takes 'X_train' and 'y_train' inputs and produces
    #   'regressor' object by using 'train_model' function
    #   c. Evaluate model: a node that takes 'regressor', 'X_test', 'y_test' inputs and
    #   runs 'evaluate_model' function - note that this node does not produce any
    #   outputs

    return ds_pipeline
```

<details>
<summary><b>CLICK TO SEE THE ANSWER</b></summary>

```python
from kedro.pipeline import Pipeline, node

from .nodes import split_data, train_model, evaluate_model


def create_pipeline(**kwargs) -> Pipeline:
    """Create the project's pipeline.

    Args:
        kwargs: Ignore any additional arguments added in the future.

    Returns:
        Pipeline object.

    """

    ds_pipeline = Pipeline(
        [
            node(
                split_data,
                ["master_table", "parameters"],
                ["X_train", "X_test", "y_train", "y_test"],
            ),
            node(train_model, ["X_train", "y_train"], "regressor"),
            node(evaluate_model, ["regressor", "X_test", "y_test"], None),
        ],
        name="ds",
    )

    return ds_pipeline
```
</details>

We also need to modify `conf/base/parameters.yml` by replacing its contents with the following:

```yaml
test_size: 0.2
random_state: 3
```

Don't forget to create an empty file `src/kedro_training/pipelines/data_science/__init__.py`.

Finally, let's add Data Science pipeline to `src/kedro_training/pipeline.py`:

```python
from typing import Dict

from kedro.pipeline import Pipeline

from kedro_training.pipelines import data_engineering as de, data_science as ds


def create_pipelines(**kwargs) -> Dict[str, Pipeline]:
    """Create the project's pipeline.

    Args:
        kwargs: Ignore any additional arguments added in the future.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.

    """

    # Modify this function such that:
    # 1. The Data Science pipeline object is created using 'create_pipeline' function
    # from the above
    # 2. The Data Science pipeline object is added to '__default__' pipeline

    return {
        ...
    }
```

<details>
<summary><b>CLICK TO SEE THE ANSWER</b></summary>

```python
from typing import Dict

from kedro.pipeline import Pipeline

from kedro_training.pipelines import data_engineering as de, data_science as ds


def create_pipelines(**kwargs) -> Dict[str, Pipeline]:
    """Create the project's pipeline.

    Args:
        kwargs: Ignore any additional arguments added in the future.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.

    """

    data_engineering_pipeline = de.create_pipeline()
    data_science_pipeline = ds.create_pipeline()

    return {
        "de": data_engineering_pipeline,
        "__default__": data_engineering_pipeline + data_science_pipeline,
    }
```
</details>

## Run a modular pipeline

Run your Data Engineering pipeline from the terminal:

```bash
kedro run --pipeline de
```

Or run this pipeline from a Jupyter Notebook cell:

```python
context.run(pipeline_name="de")
```

> Note: It is considered best-practice to restart your Jupyter Notebook kernel (`Kernel` menu -> `Restart`) every time you have made some changes to the pipeline and / or node code.

## Modular pipeline structure

Modular pipelines are intended to be reusable across various projects. Therefore, it is crucial that you, as a pipeline developer, document how it should be used. We would suggest to follow this structure:

```console
src/kedro_training/pipelines/<pipeline_name>
├── __init__.py
├── nodes.py
├── pipeline.py
└── README.md
```

where
* `__init__.py` - indicates that modular pipeline is a Python package
* `nodes.py` - contains all the node definitions
* `pipeline.py` - contains `create_pipeline()` function similar to the above example
* `README.md` - main documentation source for the end users with all the information regarding the execution of the pipeline

### Unsupported components

Kedro _does not_ automatically handle the following components of modular pipelines:
* external package dependencies defined in, say, `src/kedro_training/pipelines/<pipeline_name>/requirements.txt`, those are _not_ currently installed by `kedro install` command
* YAML configuration files - for example, `src/kedro_training/pipelines/<pipeline_name>/conf/base/catalog.yml`, these config files are _not_ discoverage by Kedro `ConfigLoader` by default

If your modular pipeline requires installation of some third-party Python packages (e.g., `pandas`, `numpy`, `pyspark`, etc.), you need to explicitly document this in `README.md` and, ideally, provide the relevant installation command, for example:

```bash
pip install -r src/kedro_training/pipelines/<pipeline_name>/requirements.txt
```

> Note: Modular pipelines should not depend on the main Python package (`kedro_training` in the example above) as it would break the portability to another project.

## Persisting the intermediate data

It is important to emphasise that the Kedro pipeline is runnable only if _all_ free inputs, i.e. the datasets that are not produced by any of the nodes, are defined in `catalog.yml`. In the Spaceflights project those free inputs are: `companies`, `shuttles`, `reviews`.

All intermediary datasets, however, can be missing from the `catalog.yml`, and your pipeline will still run without errors. This is because Kedro automatically creates a `MemoryDataSet` for each intermediary dataset that is not defined in the `DataCatalog`. Intermediary datasets in the Spaceflights project are: `preprocessed_companies`, `preprocessed_shuttles`, `master_table`, `X_train`, `X_test`, `y_train`, `y_test`, `regressor`.

These `MemoryDataSet`s pass data across nodes during the run, but are automatically deleted after the run finishes, therefore if you want to have an access to those intermediary datasets after the run, you need to define them in `catalog.yml`.

Let's say, we want to persist the `regressor` dataset to local disk. `regressor` is a `LinearRegression` object returned by the `train_model` node. We can't use, for instance, `CSVLocalDataSet` since it only works with `pandas` DataFrames, but we can instead utilise `PickleLocalDataSet` that allows to serialise Python objects and store them in the file system. Now all you have to do is to add the following dataset definition to `conf/base/catalog.yml`:

```yaml
regressor:
  type: PickleLocalDataSet
  filepath: data/06_models/regressor.pickle
  versioned: true
```

As you can see, dataset configuration contains `versioned: true` flag, which enables versioning for the dataset, which tells Kedro to output a new timestamped file containing the model object on every run rather than overwriting the existing file. This helps to keep the history of the models and revert back to an earlier iteration if necessary. Versioning flag is optional and does not change the run logic.

## How to filter Kedro pipelines

Kedro has a flexible mechanism to filter the pipeline that you intend to run. Here is a list of CLI options supported out of the box:

| CLI command                                     | Description                                                      | Multiple options allowed? |
| ----------------------------------------------- | ---------------------------------------------------------------- | ------------------------- |
| `kedro run --pipeline de`                       | Run the whole pipeline by its name                               | No                        |
| `kedro run --node debug_me --node debug_me_too` | Run only nodes with specified names                              | Yes                       |
| `kedro run --from-nodes node1,node2`            | A list of node names which should be used as a starting point    | No                        |
| `kedro run --to-nodes node3,node4`              | A list of node names which should be used as an end point        | No                        |
| `kedro run --from-inputs dataset1,dataset2`     | A list of dataset names which should be used as a starting point | No                        |
| `kedro run --tag some_tag1 --tag some_tag2`     | Run only nodes which have any of these tags attached             | Yes                       |

You can also combine these options together, so the command `kedro run --from-nodes split --to-nodes predict,report` will run all the nodes from `split` to `predict` and `report`.

## Choosing a sequential or parallel runner

Having specified the data catalog and the pipeline, you are now ready to run the pipeline. There are two different runners you can specify:

* `SequentialRunner` - runs your nodes sequentially; once a node has completed its task then the next one starts.
* `ParallelRunner` - runs your nodes in parallel; independent nodes can run at the same time, allowing you to take advantage of multiple CPU cores.

By default, Kedro uses a `SequentialRunner`, which is instantiated when you execute `kedro run` from the command line. Switching to use `ParallelRunner` is as simple as providing an additional flag when running the pipeline from the command line as follows:

```bash
kedro run --parallel
```

`ParallelRunner` executes the pipeline nodes in parallel, and is more efficient when there are independent branches in your pipeline.

> *Note:* `ParallelRunner` performs task parallelisation, which is different from data parallelisation as seen in PySpark.

## Visualising a pipeline

Kedro-Viz shows you how your Kedro data pipelines are structured. With Kedro-Viz you can:
 - See how your datasets and Python functions (nodes) are resolved in Kedro so that you can understand how your data pipeline is built
 - Get a clear picture when you have lots of datasets and nodes by using tags to visualise sub-pipelines
 - Search for nodes and datasets

 You should already have `kedro-viz` installed according to these instructions [**here**](https://github.com/quantumblack/kedro-training/blob/master/docs/project-setup.md#kedro-install).

### Using `kedro-viz`

From your terminal, run:

```
kedro viz
```

This command will run a server on http://127.0.0.1:4141 and will open up your visualisation on a browser.

> *Note:* If port `4141` is already occupied, you can run Kedro-Viz server on a different port by executing `kedro viz --port <alternative-port>`.

### Examples of `kedro-viz`

 - You can have a look at a retail ML use case [**here**](https://quantumblacklabs.github.io/kedro-viz/)
 - And an example of this Spaceflights pipeline [**here**](https://medium.com/@QuantumBlack/demystifying-machine-learning-complexity-through-visualisation-11a9d73db3c5)

### Next section
[Go to the next section](./08_transformers.md)
