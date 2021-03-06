# Project Euler Problems

Project Euler Problems in Jupyter Notebooks and using Python 3.8+

## Table of contents
* [Getting Started](#Getting-Started)
    * [Prerequisites](#Prerequisites)
    * [Installing](#Installing)
* [Running the notebooks](#Running-the-notebooks)
    * [Current problems notebooks](#Current-problems-notebooks)
    * [Beginner problems](#Beginner-problems)
    * [Expert problems](#Expert-problems)
* [Deployment](#Deployment)
* [Build With](#Build-With)
* [Tests](#Tests)
* [Contributing](#Contributing)
* [Versioning](#Versioning)
* [Authors](#Authors)
* [License](#License)
* [Acknowledgments](#Acknowledgments)

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
 loads the python file in GitHub you already see the preview. Here below the direct links have been added.

### Current problems notebooks

You can use the relative link to jump to the Jupyler Notebook preview, no local installation is needed on GitHub.

#### Beginner problems:  
1\. [Project Euler Problem 1 notebook](notebooks/Project%20Euler%20Problem%201.ipynb): 'notebooks\Project Euler Problem 1.ipymb'
    is for guiding you through the solution for the first project Euler assignment.  
2\. [Project Euler Problem 2 notebook](notebooks/Project%20Euler%20Problem%202.ipynb): 'notebooks\Project Euler Problem 2.ipymb'
    is for guiding you through the solution for the second project Euler assignment.  
41\. [Project Euler Problem 41 notebook](notebooks/Project%20Euler%20Problem%2041.ipynb): 'notebooks\Project Euler Problem 41.ipymb'
    is for guiding you through the solution for the third project Euler assignment. 

#### Expert problems:  
12\. [Project Euler Problem 12 notebook](notebooks/Project%20Euler%20Problem%2012.ipynb): 'notebooks\Project Euler Problem 12.ipymb'
    is for guiding you through the solution for the twelfth project Euler assignment.  
54\. [Project Euler Problem 54 notebook](notebooks/Project%20Euler%20Problem%2054.ipynb): 'notebooks\Project Euler Problem 54.ipymb'
    is for guiding you through the solution for the fifty-fourth project Euler assignment.  
59\. [Project Euler Problem 59 notebook](notebooks/Project%20Euler%20Problem%2059.ipynb): 'notebooks\Project Euler Problem 59.ipymb'
    is for guiding you through the solution for the fifty-fourth project Euler assignment.

## Deployment

No additional notes about how to deploy this on a live system, follow the installation instruction above.
GitHub directly support the Jupyter Notebook for a preview in the browser of your choosing supported by GitHub.
The project is structured as following if you want to run the cells in the notebook:

```
├── LICENSE
├── README.md               This top-level README for developers using this project.
|
├── data                    This is the data directory needed for the eproblems.
│   └── #054_poker.txt          These are the data files for Eukel problem 54 prefix p is the real data and the others
|                                 are test data (prefix c, e, t and z).
|
├── eproblems               Sources for use in this project for the solutions, 
|   |                         Naming convention is a tailing number behind "eproblem".
|   |                         This number is not a version, but indicates the project Euler problem identification.
│   ├── __init__.py             Makes eproblems a Python module.
│   └── eproblem##.py           One or more numbered python scripts for the specific project Euler problem.
|
├── notebooks               Jupyter notebooks. Naming convention is a tailing number behind "Project Euler Problem ".ipymb,
│                             the project euler problem identification.
│
├── src                     Sources for use in this project other than used for the solutions, but for notebooks.
│   ├── __init__.py             Makes src a Python module.
│   └── toggle_cell.py          Script to create exploratory and results oriented visualizations
|
├── tests                   A directory for re-usable tests in the future.
│   └── test_eproblem##.py      One or more numbered unittest python scripts for the specific project Euler problem.
|
└── requirements.txt        The requirements file for reproducing the environment, e.g.
                              generated with `conda list` and appended with PyCharm feedback.
```
## Build With

Anything that was used to write, compile, execute and stored for this project:
* [Anaconda individual edition](https://www.anaconda.com/products/individual) - Python distribution platform.
* [Jupyter Notebook](https://jupyter.org/) - The Jupyter Notebook.
* [JetBrains PyCharm](https://www.jetbrains.com/pycharm/) - PC PyCharm - The Python IDE for Professional Developers.
* [GitHub](https://github.com/) - A Git repository hosting service.
* [deepsource](https://deepsource.io/) - Find and fix issues during code reviews.
* [Azure Pipelines](https://azure.microsoft.com/en-us/services/devops/pipelines/) - Continuously build, test,
 and deploy to any platform and cloud.

## Tests

The tests where executed with PyCharm:
  * Configure the configuration by adding a Python Test > Unittests by target module name for the test_eproblem##.py
     you want to test.
  * Last test line of the test include the solution of the Euler problem assignment as method test_sol## where ## 
    indicates the project Euler ID number, with the correct found answer.

The CI on the unittests is executed by using Azure Pipelines:
[Pipeline sre14-ep](https://dev.azure.com/SreckoSuznjevic0449/sre14-ep)  
*Note: some additional sys to fix the unittest in the Pipeline test files required sys.path.insert(1, '../eproblems') 
to resolve the eproblems path import of the python programs. Second issue is that the unittest discovery and Azure 
logging did not match, therefore the tests needed to be added one by one in the Pipeline definition (TODO: for now as 
part of this assignment is fine, but for real automation it should be investigated).*

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
* https://reproducible-science-curriculum.github.io/sharing-RR-Jupyter/01-sharing-github/
* https://www.jetbrains.com/help/pycharm/testing-your-first-python-application.html
* https://docs.python.org/3/library/unittest.html
* https://docs.python.org/3/library/collections.html#collections.Counter
* https://en.wikipedia.org/wiki/Divisibility_rule
* https://docs.python.org/3/library/itertools.html#itertools.permutation
* https://deepsource.io/docs/
* https://techcomm.nz/Story?Action=View&Story_id=106
* https://medium.com/@wolfgarbe/the-average-word-length-in-english-language-is-4-7-35750344870f
