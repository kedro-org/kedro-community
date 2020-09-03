# Data Science pipeline

> *Note:* This `README.md` was generated using `Kedro {{ cookiecutter.kedro_version }}` for illustration purposes. Please modify it according to your pipeline structure and contents.

## Overview

This modular pipeline:
1. splits the master table into train and test subsets (`split_data` node)
2. trains a simple linear regression model (`train_model` node)
3. evaluates the accuracy of a trained model from (2) on a test set (`evaluate_model` node)


## Pipeline inputs

### `master_table`

|      |                    |
| ---- | ------------------ |
| Type | `pandas.DataFrame` |
| Description | A combined dataset from preprocessed companies and shuttle datasets, and source reviews data |

### `parameters`

|      |                    |
| ---- | ------------------ |
| Type | `dict` |
| Description | Project parameter dictionary that must contain the following keys: `test_size` (the proportion of the dataset to include in the test split), `random_state` (random seed for the shuffling applied to the data before applying the split) |


## Pipeline outputs

### `X_train`

|      |                    |
| ---- | ------------------ |
| Type | `numpy.ndarray` |
| Description | DataFrame containing train set features |

### `y_train`

|      |                    |
| ---- | ------------------ |
| Type | `numpy.ndarray` |
| Description | DataFrame containing train set target variable |

### `X_test`

|      |                    |
| ---- | ------------------ |
| Type | `numpy.ndarray` |
| Description | DataFrame containing test set features |

### `y_test`

|      |                    |
| ---- | ------------------ |
| Type | `numpy.ndarray` |
| Description | DataFrame containing test set target variable |

### `regressor`

|      |                    |
| ---- | ------------------ |
| Type | `sklearn.linear_model.LinearRegression` |
| Description | Trained linear regression model |
