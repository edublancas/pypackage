# Templates

In order to run each part independently, especially when
different teams are working on different parts of the pipeline, we
need to separate each step.


## Approach 1: Python scripts

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

## Approach 1b: Jupyter notebooks

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

## Approach 2: Python package

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


