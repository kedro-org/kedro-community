# Working with virtual environments

> The main purpose of Python virtual environments is to create an isolated environment for Python projects. This means that each project can have its own dependencies, regardless of what dependencies every other project has. Read more about Python Virtual Environments [**here**](https://realpython.com/python-virtual-environments-a-primer/).

Follow the instructions that best suit your Python installation preference. Virtual environment setups for `conda`, `venv` and `pipenv` are presented here:
 - `conda` used with an Anaconda (Python 3.7 version) installation
 - `venv` or `pipenv` used when Anaconda is not preferred

## Anaconda

Let us create a new Python virtual environment using `conda`:

```bash
conda create --name kedro-environment python=3.7 -y
```

This will create an isolated environment with Python 3.7.

To activate it, run:

```bash
conda activate kedro-environment
```

To exit the environment you can run:

```bash
deactivate kedro-environment
```

### `venv`

If you are using Python 3.0+, then you should already have the `venv` module from the standard library installed. However, for completeness you can install `venv` with:

```bash
pip install virtualenv
```

Create a directory for your virtual environment with:

```bash
mkdir kedro-environment && cd kedro-environment
```

This will create a `kedro-environment` directory for your `virtualenv` in your current working directory.

Create a new virtual environment in this directory by running:

```bash
python -m venv env/kedro-environment  # macOS / Linux
python -m venv env\kedro-environment  # Windows
```

We can activate this virtual environment with:

```bash
source env/bin/activate # macOS / Linux
.\env\Scripts\activate  # Windows
```

To exit the environment you can run:

```bash
deactivate
```

### `pipenv`

You will need to install `pipenv` with:

```bash
pip install pipenv
```

Then create a directory for the virtual environment and change to this working directory with:

```bash
mkdir kedro-environment && cd kedro-environment
```

Once all the dependencies are installed you can run `pipenv shell` which will start a session with the correct virtual environment activated. To exit the shell session using `exit`.
