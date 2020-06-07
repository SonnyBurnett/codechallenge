# Project Euler Problems

Project Euler Problems in Jupyter Notebooks and using Python 3.8+

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for calculating project
 Euler problem assignments. 

### Prerequisites

In the [requirements.txt](requirements.txt) all specific Anaconda modules are listed as reference.

### Installing

For a local install, install the following:
 * Anaconda with the following default modules:
   * Anaconda Navigator 1.9.12 (or above)
   * JupyterLab 1.2.6 (or above)
   * Notebook 6.0.3 (or above)

(*Note: any python install with a working notebook application library will work, but this is not tested.*)

Set-up the code by either clone the repertory or download it as a whole and extract into a directory of your own choosing.

## Running the notebooks

The notebooks contain a directed step to step explaining the how the problem is solved, executes the solution and even
 loads the python file to show it.

##### Current problems notebooks

```
Beginner problems:
1. \notebooks\Project Euler Problem 1.ipymb 
    is for guiding you through the solution for the first project Euler assignment. 

Expert problems:
12. \notebooks\Project Euler Problem 2.ipymb 
    is for guiding you through the solution for the twelfth project Euler assignment.
```

## Deployment

No additional notes about how to deploy this on a live system, follow the installation instruction above.
GitHub directly support the working Jupyter Notebook in the browser of your choosing supported by GitHub.
The project is structured as following:

```
├── LICENSE
├── README.md          This top-level README for developers using this project.
|
├── data               This is the data directory needed for the eproblems.
│   └── none.txt        Contains the todo for reusable text in the future.
|
├── docs               A documentation directory for reusable documentation text in the future.
│   └── none.txt        Contains the todo for reusable text in the future.
|
├── eproblems          Sources for use in this project for the solutions, 
|   |                     Naming convention is a tailing number behind "eproblem".
|   |                     This number is not a version, but indicates the project Euler problem identification.
│   ├── __init__.py     Makes eproblems a Python module.
│   └── eproblem##.py   One or more numbered python scripts for the specific project Euler problem.
|
├── example             A directory for automatically running the project Euler problems using either
|   |                     examples given in the assignments and/or using the correct parameters for the solutions.
│   └── none.txt        Contains the todo for example in the future.
|
├── notebooks          Jupyter notebooks. Naming convention is a tailing number behind "Project Euler Problem ".ipymb,
│                         the project euler problem identification.
│
├── src                Sources for use in this project other than used for the solutions, but for notebooks.
│   ├── __init__.py     Makes src a Python module.
│   └── toggle_cell.py  Script to create exploratory and results oriented visualizations
|
├── tests              A directory for reusable tests in the future.
│   └── none.txt        Contains the todo for tests in the future.
|
└── requirements.txt   The requirements file for reproducing the environment, e.g.
                          generated with `conda list` and appended with PyCharm feedback.
```

## Built With

* [Anaconda individual edition](https://www.anaconda.com/products/individual) - Python distribution platform.
* [Jupyter Notebook](https://jupyter.org/) - The Jupyter Notebook.
* [JetBrains PyCharm](https://www.jetbrains.com/pycharm/) - PC PyCharm - The Python IDE for Professional Developers.
* [GitHub](https://github.com/) - A Git repository hosting service.

## Contributing

Anybody who has access can contribute to this git repository, please contact me when you have contributions.

## Versioning

Current versions and additions are directly added to the GitHub repository.

## Authors

* **Srećko Sužnjević** - *Sre14* 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
The Project Euler https://projecteuler.net/ is owning the problem assignment,
 therefore they impose additional restrictions that your are allowed to do with the solutions. 
You are compelled to comply to these restrictions, when you have access to this repository.

## Acknowledgments

Building this framework to demonstrate the solutions was a challenge on its own, next to solving the assignments. I would like to acknowledge the following internet resources for inspiration and guidance:
* https://projecteuler.net/
* https://jupyter-notebook.readthedocs.io/en/stable/index.html
* https://ipython-books.github.io/27-writing-high-quality-python-code/
* https://docs.python-guide.org/writing/structure/#
* https://www.python.org/dev/peps/pep-0008/
* https://drivendata.github.io/cookiecutter-data-science/
* https://www.jetbrains.com/help/pycharm/
