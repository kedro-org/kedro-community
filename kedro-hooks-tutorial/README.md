# Kedro Hooks Tutorial

## Overview

> N.B.: This tutorial relies on a new feature in Kedro 0.16.0 called Hooks.

This tutorial project built upon the [basic tutorial](../kedro-tutorial) to illustrate how to use hooks to extend Kedro for the following use cases:

* [Adding data validation](src/kedro_hooks_tutorial/hooks/data_validation_hooks.py) to node's inputs and outputs using [Great Expectations](https://docs.greatexpectations.io/en/latest/).

![](docs/images/data_validation.png)

* Adding observability to your pipeline with [statsd](https://statsd.readthedocs.io/en/v3.3/configure.html) and visualise using [Grafana](https://grafana.com/).

![](docs/images/pipeline_observability.png)

* Adding metrics tracking to your model with [MLflow](https://mlflow.org/).

![](docs/images/mlflow.png)


## Setup

To use this project, use `git clone` to clone it. You don’t need to create a new Kedro project. To make sure you have the required dependencies, run in your virtual environment (see [the documentation](https://kedro.readthedocs.io/en/stable/02_getting_started/01_prerequisites.html#python-virtual-environments) for how to set up your virtual environment):

```bash
pip install kedro==0.15.8
kedro install
```

You can run the project with:

```bash
kedro run
```
