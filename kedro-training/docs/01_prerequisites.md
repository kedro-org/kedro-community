# Installation prerequisites

Kedro supports macOS, Linux and Windows (7 / 8 / 10 and Windows Server 2016+). If you encounter any problems on these platforms please engage Kedro community support on [Stack Overflow](https://stackoverflow.com/questions/tagged/kedro).

## Python

Kedro supports Python 3.5, 3.6 and 3.7. We recommend using [Anaconda](https://www.anaconda.com/download) (Python 3.7 version) to install Python packages. However, if Anaconda is not preferred then this [tutorial](https://realpython.com/installing-python/) can help you with installation and setup.

### `PySpark`

[Java](https://www.oracle.com/technetwork/java/javase/downloads/index.html) will need to be installed if `PySpark` is a workflow requirement.

## Operating system specifications


### Windows

Windows users will require admin rights to install [Anaconda](https://www.anaconda.com/download) and [Java](https://www.oracle.com/technetwork/java/javase/downloads/index.html).

### Build tools

On Unix-like operating systems, you will need to install a C compiler and related build tools for your platform. This is due to the inclusion of the [memory-profiler](https://pypi.org/project/memory-profiler/) library in our dependencies. If your operating system is not mentioned, please refer to its documentation.

#### macOS
To install Command Line Tools for Xcode, run the following from the terminal:

```bash
xcode-select --install
```

#### GNU / Linux

##### Debian / Ubuntu

The following command (run with root permissions) will install the `build-essential` metapackage for Debian-based distributions:

```bash
apt-get update && apt-get install build-essential
```

##### Red Hat Enterprise Linux / Centos
The following command (run with root permissions) will install the "Develop Tools" group of packages on RHEL/Centos:

```bash
yum groupinstall 'Development Tools'
```

## Optional tools

### Git
Git is a version control software that records changes to a file or set of files. Git is especially helpful for software developers as it allows changes to be tracked (including who and when) when working on a project.

To download `git`, go to the following link and choose the correct version for your operating system: https://git-scm.com/downloads.

#### Windows
Download the [`git` for Windows installer](https://gitforwindows.org/). Make sure to select **Use `git` from the Windows command prompt** this will ensure that `git` is permanently added to your PATH.

Also select **Checkout Windows-style, commit Unix-style line endings** selected and click on **Next**.

This will provide you both `git` and `git bash`. We might have a few exercises using the command line quite a lot during the workshop so using `git bash` is a good option.

### GitHub
GitHub is a web-based service for version control using Git. You will need to set up an account at: https://github.com.

Basic GitHub accounts are free and you can now also have private repositories.

### Text editors & IDEs
Text editors are tools with powerful features designed to optimize writing code. There are many text editors that you can choose from. Here are some we recommend:

- [PyCharm](https://www.jetbrains.com/pycharm/download/)
- [VS Code](https://code.visualstudio.com/)
- [Atom](https://atom.io/)

### Docker
Docker is a tool that makes it easier to create, deploy and run applications. It uses containers to package an application along with its dependencies and then runs the application in an isolated virtualised environment.

If Docker is a tool that you use internally then make sure to carefully read the prerequisites and instructions here: https://docs.docker.com/install/.
