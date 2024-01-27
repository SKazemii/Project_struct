# Data Science Structure

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._



### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------
    cookiecutter -c master https://github.com/SKazemii/Project_struct.git


[![asciicast](https://asciinema.org/a/244658.svg)](https://asciinema.org/a/244658)


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
Project Organization
    |
    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── configs            <- The centrized configs that were using in this project.
    ├── data
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   ├── raw            <- The original, immutable data dump.
    |   └── models         <- Trained and serialized models, model predictions, or model summaries
    │
    ├── manuscripts
    │   ├── docs           <- A default Sphinx project; see sphinx-doc.org for details
    |   ├── references     <- Data dictionaries, manuals, and all other explanatory materials.
    |   ├── figures        <- Generated graphics and figures to be used in reporting
    |   └── src            <- Latex files of project
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    │
    ├── logs               <- Generated logs.
    │   
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```


### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------
    py.test tests
