# Transcoding

## What is this?

You may come across a situation where you would like to read the same file using two different dataset implementations. Use transcoding when you want to load and save the same file, via its specified `filepath`, using different `DataSet` implementations.

## A typical example of transcoding

For instance, parquet files can not only be loaded via the `ParquetLocalDataSet`, but also directly by `SparkDataSet` using `pandas`. This conversion is typical when coordinating a `Spark` to `pandas` workflow.

To enable transcoding, you will need to define two `DataCatalog` entries for the same dataset in a common format (Parquet, JSON, CSV, etc.) in your `conf/base/catalog.yml`:

```
my_dataframe@spark:
  type: kedro.contrib.io.pyspark.SparkDataSet
  filepath: data/02_intermediate/data.parquet

my_dataframe@pandas:
  type: ParquetLocalDataSet
  filepath: data/02_intermediate/data.parquet
```

These entries will be used in the pipeline like this:

```
Pipeline([
    node(func=my_func1,
        inputs="spark_input",
        outputs="my_dataframe@spark"
        ),
    node(func=my_func2,
        inputs="my_dataframe@pandas",
        outputs="pipeline_output"
        ),
])
```

## How does it work?

In this example, Kedro understands that `my_dataframe` is the same dataset in its `SparkDataSet` and `ParquetLocalDataSet` formats and helps resolve the node execution order.

In the pipeline, Kedro uses the `SparkDataSet` implementation for saving and `ParquetLocalDataSet`
for loading, so the first node should output a `pyspark.sql.DataFrame`, while the second node would receive a `pandas.Dataframe`.

### Next section
[Go to the next section](./13_custom-datasets.md)
