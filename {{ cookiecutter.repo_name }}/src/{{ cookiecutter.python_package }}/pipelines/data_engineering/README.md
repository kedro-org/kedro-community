# Data Engineering pipeline

> *Note:* This `README.md` was generated using `Kedro {{ cookiecutter.kedro_version }}` for illustration purposes. Please modify it according to your pipeline structure and contents.

## Overview

This modular pipeline preprocesses the raw data (`preprocessing_companies` and `preprocessing_shuttles` nodes) and then creates the master table (`master_table` node).

## Pipeline inputs

### `companies`

|      |                    |
| ---- | ------------------ |
| Type | `pandas.DataFrame` |
| Description | Source data about the companies provide the space shuttles |

### `shuttles`

|      |                    |
| ---- | ------------------ |
| Type | `pandas.DataFrame` |
| Description | Source data about technical characteristics of various space shuttles |

### `reviews`

|      |                    |
| ---- | ------------------ |
| Type | `pandas.DataFrame` |
| Description | Source dataset with historical customer reviews of their space trips |


## Pipeline outputs

### `preprocessed_companies`

|      |                    |
| ---- | ------------------ |
| Type | `pandas.DataFrame` |
| Description | Cleansed and normalised version of the `companies` dataset |

### `preprocessed_shuttles`

|      |                    |
| ---- | ------------------ |
| Type | `pandas.DataFrame` |
| Description | Cleansed and normalised version of the `shuttles` dataset |

### `master_table`

|      |                    |
| ---- | ------------------ |
| Type | `pandas.DataFrame` |
| Description | A combined dataset from preprocessed companies and shuttle datasets, and source reviews data |
