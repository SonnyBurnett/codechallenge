# POKER WINNER
This application determines, out of two hands of cards, which hand has the most points and is the winner.

## Run the application
This application has no dependencies so can be ran from the command-line:
```
python solution\solution54.py
```
Requirement is that there is a file called *poker.txt* in the same directory as where the solution54.py files resides.
This file must adhere to the following layout:
- each line contains data for two hands of cards, looking like: 2H 2D 4C 4D 4S 3C 3D 3S 9S 9D
- cards per line must be existing playcards and no jokers
- cards per line may occur only once

## Test the application
In order to test the application one can run
```
pytest --cov-config=tox.ini
```

## Development

- Install python 3: `sudo apt install python3` or whatever works for your environment.
- Create a virtual env: `python3 -m venv .env`
- Activate the virtual env using [VS Code](https://code.visualstudio.com/docs/python/environments)
  or CLI: `source .env/bin/activate`
- Pip install the required libs: `pip install -r requirements-ci.txt`
- Unit test are done using the [pytest](http://doc.pytest.org/en/latest/getting-started.html) framework, setup [VS Code](https://code.visualstudio.com/docs/python/testing) or run: `pytest` *
- Coverage is calculated with [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/), run `pytest --cov-config=tox.ini`
- Linting is done with [pylama](https://pylama.readthedocs.io/en/latest/) setup in [VS Code](https://code.visualstudio.com/docs/python/linting) or run: `pylama` *
- Setup the document formatter in [VS code](https://code.visualstudio.com/docs/python/editing#_formatting) to autopep8 *

\* Config for all of these are in the tox.ini file
