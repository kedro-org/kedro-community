from kedro.io import DataCatalog, MemoryDataSet
from kedro.pipeline import node, Pipeline
from kedro.runner import SequentialRunner

# Prepare a data catalog
data_catalog = DataCatalog({"example_data": MemoryDataSet()})


def return_greeting():
    # Prepare first node
    return "Hello"


return_greeting_node = node(
    return_greeting, inputs=None, outputs="my_salutation"
)


def join_statements(greeting):
    # Prepare second node
    return f"{greeting} Kedro!"


join_statements_node = node(
    join_statements, inputs="my_salutation", outputs="my_message"
)

# Assemble nodes into a pipeline
pipeline = Pipeline([return_greeting_node, join_statements_node])

# Create a runner
runner = SequentialRunner()

# Run the pipeline
runner.run(pipeline, data_catalog)
