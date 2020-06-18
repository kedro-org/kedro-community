# Training pre-requisites
This Kedro training materials assume the following pre-requisites for your technical understanding.

We assume that you understand these technology and won't be teaching how to do any of them. In order to maximise your learning experience from the Kedro training, please review them before the training if you are not familiar with any of them.

- Intermediate Python knowledge
  - Basic Python
    - Functions
    - Classes
    - Loops
    - Conditional statements
    - Common data structures (lists, dictionaries, tuples)
    - IO operation (reading and writing data using Python)
  - Using Python modules (e.g how to use `__init__.py` and [relative and absolute imports](https://realpython.com/absolute-vs-relative-python-imports/))
  - Importing Python packages with `pip`.
  - Dependency management with `requirements.txt`
  - Working on many Python files in nested directory structures.
  - Familiarity with Python data science libraries (e.g `Pandas`, `PySpark`, `scikit-learn`, Jupyter notebook/labs, iPython)
  - Using virtual environment (Anaconda, venv, pipenv)
- Object-oriented programming (overriding class methods, class inheritance).
- Basic YAML syntax
- Working with the command line (aka. cmd, CLI, prompt, console or terminal)
  -  `cd` to navigate directories
  -  `ls` to list files and directories
  -  Executing a command and Python program from a command line

Below is optional and won't cause any issues if you don't know them (but Kedro integrates well with these technologies)
- Version Control with Git
- Cloud storage (S3, Azure Blob, GCP)
- PySpark
- Docker for managing deployment
- Airflow for scheduling pipeline execution

# Checklist
Please use this checklist to make sure you have everything necessary to participate in the Kedro training.

- [ ] You have Python 3 (3.6, 3.7 or 3.8) installed in your laptop (check with `python --version` or `python3 --version`)
- [ ] You have Anaconda installed. An alternative to Anaconda can be found [here](https://github.com/quantumblacklabs/kedro-examples/blob/master/kedro-training/docs/02_virtual-environment.md)
- [ ] You have an editor installed for writing Python code
- [ ] You have a Terminal installed

After you have installed above, please make sure that you are able to execute the following commands in your Terminal

- [ ] `git clone https://github.com/quantumblacklabs/kedro-examples` will download this training Github repository (or download a zip file from the link).

- [ ] `conda create --name=training python=3.6 -y && conda activate training` will create an virtual environment called "training" and activate the environment.

- [ ] `pip install kedro` will install Kedro in your conda environment.

- [ ]  `kedro --version` will show [the latest Kedro version](https://pypi.org/project/kedro/).


If you are able to complete all of the above points, you are ready for the workshop! In case you have any problems or questions in any of the above checklist, please contact an instructor and resolve the issue before the training.

# Installation prerequisites

Kedro supports macOS, Linux and Windows (7 / 8 / 10 and Windows Server 2016+). If you encounter any problems on these platforms please engage Kedro community support on [Stack Overflow](https://stackoverflow.com/questions/tagged/kedro).

## Python

Kedro supports Python 3.5, 3.6 and 3.7. We recommend using [Anaconda](https://www.anaconda.com/download) (Python 3.7 version) to install Python packages. However, if Anaconda is not preferred then this [tutorial](https://realpython.com/installing-python/) can help you with installation and setup.

### Text editors & IDEs
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
