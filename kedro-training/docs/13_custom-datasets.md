# Creating custom datasets

Often, real world data is stored in formats that are not supported by Kedro. We will illustrate this with `shuttles.xlsx`. In fact, Kedro has built-in support for Microsoft Excel files that includes support for versioning and writer arguments. This example explains a simplified implementation.

Let’s create a custom dataset class which will allow you to load and save `.xlsx` files.

To keep your code well-structured you should create a Python sub-package called **`kedro_tutorial.io`**. You can do that by running this in your Unix terminal:

```bash
mkdir -p src/kedro_tutorial/io && touch src/kedro_tutorial/io/__init__.py
```

Or, if you are a Windows user:

```bat
mkdir src\kedro_tutorial\io && type nul > src\kedro_tutorial\io\__init__.py
```

Creating new custom dataset implementations is done by creating a class that extends and implements all abstract methods from `AbstractDataSet`. To implement a class that will allow you to load and save Excel files locally, you need to create the file `src/kedro_tutorial/io/xls_local.py` by running in your Unix terminal:

```bash
touch src/kedro_tutorial/io/xls_local.py
```
For Windows, try:
```bat
type nul > src\kedro_tutorial\io\xls_local.py
```

and paste the following into the newly created file:

```python
"""ExcelLocalDataSet loads and saves data to a local Excel file. The
underlying functionality is supported by pandas, so it supports all
allowed pandas options for loading and saving Excel files.
"""
from os.path import isfile
from typing import Any, Union, Dict

import pandas as pd

from kedro.io import AbstractDataSet


class ExcelLocalDataSet(AbstractDataSet):
    """``ExcelLocalDataSet`` loads and saves data to a local Excel file. The
    underlying functionality is supported by pandas, so it supports all
    allowed pandas options for loading and saving Excel files.

    Example:
    ::

        >>> import pandas as pd
        >>>
        >>> data = pd.DataFrame({'col1': [1, 2], 'col2': [4, 5],
        >>>                      'col3': [5, 6]})
        >>> data_set = ExcelLocalDataSet(filepath="test.xlsx",
        >>>                              load_args={'sheet_name':"Sheet1"},
        >>>                              save_args=None)
        >>> data_set.save(data)
        >>> reloaded = data_set.load()
        >>>
        >>> assert data.equals(reloaded)

    """

    def _describe(self) -> Dict[str, Any]:
        return dict(
            filepath=self._filepath,
            engine=self._engine,
            load_args=self._load_args,
            save_args=self._save_args,
        )

    def __init__(
        self,
        filepath: str,
        engine: str = "xlsxwriter",
        load_args: Dict[str, Any] = None,
        save_args: Dict[str, Any] = None,
    ) -> None:
        """Creates a new instance of ``ExcelLocalDataSet`` pointing to a concrete
        filepath.

        Args:
            engine: The engine used to write to excel files. The default
                          engine is 'xlswriter'.

            filepath: path to an Excel file.

            load_args: Pandas options for loading Excel files.
                Here you can find all available arguments:
                https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_excel.html
                The default_load_arg engine is 'xlrd', all others preserved.

            save_args: Pandas options for saving Excel files.
                Here you can find all available arguments:
                https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_excel.html
                All defaults are preserved.

        """
        self._filepath = filepath
        default_save_args = {}
        default_load_args = {"engine": "xlrd"}

        self._load_args = (
            {**default_load_args, **load_args}
            if load_args is not None
            else default_load_args
        )
        self._save_args = (
            {**default_save_args, **save_args}
            if save_args is not None
            else default_save_args
        )
        self._engine = engine

    def _load(self) -> Union[pd.DataFrame, Dict[str, pd.DataFrame]]:
        return pd.read_excel(self._filepath, **self._load_args)

    def _save(self, data: pd.DataFrame) -> None:
        writer = pd.ExcelWriter(self._filepath, engine=self._engine)
        data.to_excel(writer, **self._save_args)
        writer.save()

    def _exists(self) -> bool:
        return isfile(self._filepath)
```

And update the `conf/base/catalog.yml` file by adding the following:

```yaml
shuttles:
  type: kedro_tutorial.io.xls_local.ExcelLocalDataSet
  filepath: data/01_raw/shuttles.xlsx
```

> *Note:* The `type` specified is `kedro_tutorial.io.xls_local.ExcelLocalDataSet` which points Kedro to use the custom dataset implementation. To use Kedro's internal support for reading Excel datasets, you can simply specify `ExcelLocalDataSet`, which is implemented similar to the code above.

A good way to test that everything works as expected is by trying to load the dataset within a new `kedro ipython` session:

```python
context.catalog.load('shuttles').head()
```

### Contributing a custom dataset implementation

Kedro users create many custom dataset implementations while working on real-world projects, and it makes sense that they should be able to share their work with each other. That is why Kedro has a `kedro.contrib.io` sub-package, where users can add new custom dataset implementations to help others in our community. Sharing your custom datasets implementations is possibly the easiest way to contribute back to Kedro and if you are interested in doing so, you can check out the [Kedro contribution guide](https://github.com/quantumblacklabs/kedro/blob/develop/CONTRIBUTING.md) in the GitHub.
