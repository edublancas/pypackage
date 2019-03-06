# Python templates

This repository shows different approaches for developing scientific applications with Python.

Scientific codebases are often constructed of several steps that are run one after the other (i.e. in a Machine Learning application we might have scripts for loading data, cleaning, building features, training models and evaluation).

For example, a Machine Learning pipeline could from a bash session:

```shell
my_ml_project data_load PATH_TO_RAW_DATA
my_ml_project data_clean
my_ml_project build_features FEATURES_TO_USE
my_ml_project models_train
my_ml_project models_evaluate PATH_TO_MODEL_REPORTS
```

...or from a Python session like this:

```python
import my_ml_project

my_ml_project.data_load(PATH_TO_RAW_DATA)
my_ml_project.data_clean()
my_ml_project.build_features()
my_ml_project.models_train()
my_ml_project.models_evaluate(PATH_TO_MODEL_REPORTS)
```

Splitting the pipeline on independent steps ensures that our pipeline can be easily extended (i.e. add one more intermediate step) and interfaced with other software. (i.e. run the pipleine with Apache Airflow).

A robust pipeline should have the following characteristics:


1. Simple to setup: once the data is available, the pipeline should run after running a `git clone` and just a few extra setup commands
2. Provide an accesible interface: after setup, each pipeline step should be *easily* accesible from the command line or a Python session
3. Hierarchically organized: source files should be organized according to their function to keep the codebase clear (as opposed to a flat structure with 100 scripts inside a single folder)
4. Semantically organized: each source file should only contain code that performs related tasks (as opposed to have a single long file that performs all sorts of tasks)


The approach that complies with all four characteristics is a Python package. More information about a Python package is available on the [Python Packaging Authority website](https://packaging.python.org/).

## Why a Python package?

A Python package complies with the four characteristics:

1. Simple to setup: Python packages are setup in a single `pip install my_package` command
2. Provide an accesible interface: once installed, packages can provide a command line interface via `python -m` (i.e. `python -m my_package.my_module.my_function`), a custom command (i.e. `my_package my_function`) or a Python session (`i.e. from my_package.my_module import my_function; my_function()`)
3. Hierchically organized: a package gives us freedom to organize our source code in an arbitrary folder structure that is accesible via import statements (i.e. `from my_package.module1 import a_function`)
2. Semantically organized: since the source code is available through module imports, we can organized split our code in small files

## Example

## Other approaches

### Python scripts 

A common anti-pattern is to organize a scientific codebase in *.py source files (a Python package it is also a collection of *.py files but with a specific structure and requirements).

Assume we are building a project to perform mathematical operations (see code under the `scripts/` folder. Our core functions are located in `script/lib/math.py` and

```shell
python script/power.py 2 3
```

Pros:

* Easy to implement, just organize the scripts under the same folder

Cons:

* Import issues (you can only import the lib if script is your current directory):

```python
# cd to ds-project-template/_templates and start python interpreter

# this is gonna break with a "ImportError: No module named 'lib'
from script import power
```

You can overcome this if everything is contained in a single `.py` file
but if the step is very complicated, putting a lot of code in a single
file is not recommended.

Recommended use case: when the step is simple (one small to medium `.py` file)
and want to avoid more setup.

### Approach 1b: Jupyter notebooks

Similar to the first approach but this time we will have a parametrized notebooks. For this to work install [papermill](https://github.com/nteract/papermill) (`pip install papermill`)

Then you can run the notebook as:

```python
import papermill as pm

# note you have to be insice the _templates/notebook

pm.execute_notebook(
   'power.ipynb',
   'power_output.ipynb',
   parameters=dict(x=2, y=3)
)
```

Or from the shell:

```shell
papermill power.ipynb power_output.ipynb -p x 2  -p y 3
```

Pros:

* Easy to implement, especially when you like working with notebooks

Cons:

* Same as 1), import issues

You can overcome this if everything is contained in a single `.ipynb` notebook
but if the step is very complicated, putting a lot of code in a single
notebook is not recommended.

Recommended use case: when the step is simple (one small to medium
`.ipynb` file) and want to avoid more setup.

### Approach 2: Python package

The recommended alternative is to bundle your code as a Python package, it only requires a `setup.py` file.

```shell
# install package using pip
pip install --editable package/

# note: the --editable will install the package
# on editable mode, this means that changes
# made in the source code will take effect
# next time you open a Python session,
# very useful for development
```

Once installed you can import your code like this:

```python
# you can import this everywhere since it is added to your python
# environment
from package import math

math.power(2, 3)
```

To run the CLI (from any directory):

```shell
python -m package.power 2 3
```

You can also provide a specific command to run your code, uncomment lines 86-88 from the sample `setup.py` file:

```python
entry_points = {
    'console_scripts': [
        'power = package.power:main',
    ]
},
```

Re-install (this is required when you update `setup.py`): `pip install --editable package`

Then you can run your function like this:

```shell
power 2 3
```

## Challenges
