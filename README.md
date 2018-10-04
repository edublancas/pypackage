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