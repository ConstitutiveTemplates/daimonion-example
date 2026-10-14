# Installation

## Check your version of python

You will need python 3.11 or later. You can check your version of python by
typing into a terminal:

```
$ python3 --version
```

## Create the environment

It is recommended that you install into an isolated environment so this
installation will not interfere with any existing Python software:


```
$ uv sync                      # create .venv and install everything (incl. dev deps)
```


## Installing the library

You can now install the library and its dependencies:


```
$ pip install ConstitutiveTemplates-architekton-py-example
```


If you require a feature that is not currently released you can also install
from github:


```
$ pip install git+https://github.com/ConstitutiveTemplates/architekton-py-example.git
```


The library should now be installed and the commandline interface on your path.
You can check the version that has been installed by typing:

```
$ architekton-py-example --version
```
