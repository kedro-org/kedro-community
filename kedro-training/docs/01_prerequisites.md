# Training pre-requisites
The Kedro training materials assume a pre-requisite level of technical understanding.

To optimise your experience and learn the most you can from the Kedro training, please review the following before your training session. We provide external resource links for each topic.

- [Introduction to Python](https://docs.python.org/3/tutorial/)
  - Functions, loops, conditional statements and IO operation
  - Common data structures including lists, dictionaries and tuples
- Intermediate Python
  - [Installing Python packages using `pip`](https://pip.pypa.io/en/stable/quickstart/)
  - [Dependency management with `requirements.txt`](https://pip.pypa.io/en/latest/user_guide/#requirements-files)
  - [Python modules](https://docs.python.org/3/tutorial/modules.html) (e.g how to use `__init__.py` and relative and absolute imports)
  - [Familiarity with Python data science libraries](https://towardsdatascience.com/top-10-python-libraries-for-data-science-cd82294ec266), especially `Pandas` and `scikit-learn`
  - An understanding of how to use [Jupyter Notebook/Lab](https://www.dataquest.io/blog/jupyter-notebook-tutorial/) and [iPython](https://www.codecademy.com/articles/how-to-use-ipython))
  - [Using a virtual environment](https://docs.python.org/3/tutorial/venv.html) (we recommend using `conda`, but you can also use `venv` or `pipenv`)
- [Basic YAML syntax](https://yaml.org/)
- [Working with the command line](https://tutorial.djangogirls.org/en/intro_to_command_line/) (also known as cmd, CLI, prompt, console or terminal)
  -  `cd` to navigate directories
  -  `ls` to list files and directories
  -  [Executing a command and Python program from a command line](https://realpython.com/run-python-scripts/#how-to-run-python-scripts-using-the-command-line)

The following lists software that Kedro integrates with; however, during training these are optional requirements.
- [Version Control with Git](https://git-scm.com/doc)
- Cloud storage ([S3](https://aws.amazon.com/s3/), [Azure Blob](https://azure.microsoft.com/en-gb/services/storage/blobs/) and [GCS](https://cloud.google.com/storage))
- [PySpark](https://spark.apache.org/docs/latest/api/python/index.html)
- [Docker](https://docs.docker.com/) as a deployment option
- [Airflow](https://airflow.apache.org/docs/stable/tutorial.html) for scheduling pipeline execution

# Checklist
Please use this checklist to make sure you have everything necessary to participate in the Kedro training.

- [ ] You have [Python 3 (either 3.6, 3.7 or 3.8)](https://www.python.org/downloads/) installed on your laptop
- [ ] You have Anaconda or an [alternative](https://github.com/quantumblacklabs/kedro-examples/blob/master/kedro-training/docs/02_virtual-environment.md) virtual environment manager
- [ ] You have [a code editor](#text-editors-and-ides) installed for writing Python code
- [ ] You have a [command line](#command-line) installed

Having completed the above checklist, make sure that you are able to execute the following commands in your Terminal:
- [ ]  `python --version` or `python3 --version` returns a correct Python version (either 3.6, 3.7 or 3.8).
- [ ] Download the [Kedro training repository](https://github.com/quantumblacklabs/kedro-examples) by following [these instructions](https://stackoverflow.com/questions/2751227/how-to-download-source-in-zip-format-from-github).

- [ ] `conda create --name=kedro-environment python=3.6 -y && conda activate kedro-environment` creates an virtual environment called `kedro-environment` and activates the environment (you can find how to do this with `venv` or `pipenv` in [here](https://github.com/quantumblacklabs/kedro-examples/blob/master/kedro-training/docs/02_virtual-environment.md)).

- [ ] `pip install kedro` installs Kedro in your conda environment.

- [ ]  `kedro --version` shows [the latest Kedro version](https://pypi.org/project/kedro/).


If you are able to complete all of the above, you are ready for the training! In case you have any problems or questions in any of the above checklist, please contact an instructor and resolve the issues before the training.

# Installation prerequisites

Kedro supports macOS, Linux and Windows (7 / 8 / 10 and Windows Server 2016+). If you encounter any problems on these platforms please engage Kedro community support on [Stack Overflow](https://stackoverflow.com/questions/tagged/kedro).

## Python

Kedro supports Python 3.6, 3.7 and 3.8. We recommend using [Anaconda](https://www.anaconda.com/download) (Python 3.7 version) to install Python packages. However, if Anaconda is not preferred then this [tutorial](https://realpython.com/installing-python/) can help you with installation and setup.

## Command line
The command line works as a text-based application for viewing, navigating and manipulating files on your computer. You can find more information for each OS platform:
- [Terminal in macOS](https://support.apple.com/en-gb/guide/terminal/welcome/mac)
- [Windows command line](https://www.computerhope.com/issues/chusedos.htm)

### Text editors and IDEs
Text editors are tools with powerful features designed to optimize writing code. There are many text editors that you can choose from. Here are some we recommend:

- [PyCharm](https://www.jetbrains.com/pycharm/download/)
- [VS Code](https://code.visualstudio.com/)
- [Atom](https://atom.io/)

## Optional tools

### `PySpark`

[Java 8](https://www.oracle.com/technetwork/java/javase/downloads/index.html) will need to be installed if `PySpark` is a workflow requirement.

> _Note:_ Windows users will require admin rights to install [Anaconda](https://www.anaconda.com/download) and [Java](https://www.oracle.com/technetwork/java/javase/downloads/index.html).


### Git
Git is a version control software that records changes to a file or set of files. Git is especially helpful for software developers as it allows changes to be tracked (including who and when) when working on a project.

To download `git`, go to the following link and choose the correct version for your operating system: https://git-scm.com/downloads.

#### Installing Git on Windows
Download the [`git` for Windows installer](https://gitforwindows.org/). Make sure to select **Use `git` from the Windows command prompt** this will ensure that `git` is permanently added to your PATH.

Also select **Checkout Windows-style, commit Unix-style line endings** selected and click on **Next**.

This will provide you both `git` and `git bash`. We might have a few exercises using the command line quite a lot during the workshop so using `git bash` is a good option.

### GitHub
GitHub is a web-based service for version control using Git. You will need to set up an account at: https://github.com.

Basic GitHub accounts are free and you can now also have private repositories.

### Docker
Docker is a tool that makes it easier to create, deploy and run applications. It uses containers to package an application along with its dependencies and then runs the application in an isolated virtualised environment.

If Docker is a tool that you use internally then make sure to carefully read the prerequisites and instructions here: https://docs.docker.com/install/.

### Next section
[Go to the next section](./02_virtual-environment.md)
