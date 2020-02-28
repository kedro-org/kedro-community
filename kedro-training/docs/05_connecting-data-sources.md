## Adding your datasets to `data`

Before you start a Kedro project, you need to prepare the datasets. This tutorial will make use of fictional datasets for spaceflight companies shuttling customers to the Moon and back. You will use the data to train a model to predict the price of shuttle hire.

The spaceflight tutorial has three files and uses two data formats: `.csv` and `.xlsx`. Download and save the files to the `data/01_raw/` folder of your project directory:

* [reviews.csv](https://quantumblacklabs.github.io/kedro/reviews.csv)
* [companies.csv](https://quantumblacklabs.github.io/kedro/companies.csv)
* [shuttles.xlsx](https://quantumblacklabs.github.io/kedro/shuttles.xlsx)

Here is an example of how you can [download the files from GitHub](https://www.quora.com/How-do-I-download-something-from-GitHub) to `data/01_raw` directory inside your project using [cURL](https://curl.haxx.se/download.html) in a Unix terminal:

<details>
<summary><b>CLICK TO EXPAND</b></summary>

```bash
# reviews
curl -o data/01_raw/reviews.csv https://raw.githubusercontent.com/quantumblacklabs/kedro/develop/docs/source/03_tutorial/data/reviews.csv
# companies
curl -o data/01_raw/companies.csv https://raw.githubusercontent.com/quantumblacklabs/kedro/develop/docs/source/03_tutorial/data/companies.csv
# shuttles
curl -o data/01_raw/shuttles.xlsx https://raw.githubusercontent.com/quantumblacklabs/kedro/develop/docs/source/03_tutorial/data/shuttles.xlsx
```
</details>

Or through using [Wget](https://www.gnu.org/software/wget/):

<details>
<summary><b>CLICK TO EXPAND</b></summary>

```bash
# reviews
wget -O data/01_raw/reviews.csv https://raw.githubusercontent.com/quantumblacklabs/kedro/develop/docs/source/03_tutorial/data/reviews.csv
# companies
wget -O data/01_raw/companies.csv https://raw.githubusercontent.com/quantumblacklabs/kedro/develop/docs/source/03_tutorial/data/companies.csv
# shuttles
wget -O data/01_raw/shuttles.xlsx https://raw.githubusercontent.com/quantumblacklabs/kedro/develop/docs/source/03_tutorial/data/shuttles.xlsx
```
</details>

Alternatively, if you are a Windows user, try [Wget for Windows](https://eternallybored.org/misc/wget/) and the following commands instead:

<details>
<summary><b>CLICK TO EXPAND</b></summary>

```bat
wget -O data\01_raw\reviews.csv https://raw.githubusercontent.com/quantumblacklabs/kedro/develop/docs/source/03_tutorial/data/reviews.csv
wget -O data\01_raw\companies.csv https://raw.githubusercontent.com/quantumblacklabs/kedro/develop/docs/source/03_tutorial/data/companies.csv
wget -O data\01_raw\shuttles.xlsx https://raw.githubusercontent.com/quantumblacklabs/kedro/develop/docs/source/03_tutorial/data/shuttles.xlsx
```
</details>

or [cURL for Windows](https://curl.haxx.se/windows/):

<details>
<summary><b>CLICK TO EXPAND</b></summary>

```bat
curl -o data\01_raw\reviews.csv https://raw.githubusercontent.com/quantumblacklabs/kedro/develop/docs/source/03_tutorial/data/reviews.csv
curl -o data\01_raw\companies.csv https://raw.githubusercontent.com/quantumblacklabs/kedro/develop/docs/source/03_tutorial/data/companies.csv
curl -o data\01_raw\shuttles.xlsx https://raw.githubusercontent.com/quantumblacklabs/kedro/develop/docs/source/03_tutorial/data/shuttles.xlsx
```
</details>

## Using the Data Catalog with `catalog.yml`

To work with the datasets provided you need to make sure they can be loaded by Kedro.

All Kedro projects have a `conf/base/catalog.yml` file where users register the datasets they use. Registering a dataset is as simple as adding a named entry into the `.yml` file, which includes:

* File location (path)
* Type of data
* Versioning (optional)
* Any additional arguments (optional)

Kedro supports a number of different data types, such as `csv`, which is implemented by `CSVLocalDataSet`. You can find all supported datasets in the API docs for ([core datasets](https://kedro.readthedocs.io/en/stable/kedro.io.html) and [contrib datasets](https://kedro.readthedocs.io/en/stable/kedro.contrib.io.html)). The difference between core and contrib dataset is that core datasets are well supported by Kedro team (e.g., all of them support data versioning), and contrib datasets were added by external contributors (e.g., some support data versioning).

Let’s start this process by registering the `csv` datasets by copying the following to the end of the `conf/base/catalog.yml` file:

```yaml
companies:
  type: CSVLocalDataSet
  filepath: data/01_raw/companies.csv

reviews:
  type: CSVLocalDataSet
  filepath: data/01_raw/reviews.csv

shuttles:
  type: ExcelLocalDataSet
  filepath: data/01_raw/shuttles.xlsx
```

If you want to check whether Kedro loads the data correctly, open a `kedro ipython` session and run:

```python
context.catalog.load('companies').head()
```

This will load the dataset named `companies` (as per top-level key in `catalog.yml`), from the underlying filepath `data/01_raw/companies.csv`, and show you the first five rows of the dataset. It is loaded into a `pandas` DataFrame and you can play with it as you wish.

When you have finished, simply close `ipython` session by typing the following:

```python
exit()
```

