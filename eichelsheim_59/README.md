# XOR decryption
This application will try to decrypt a cypher. The keys used for attempting to decrypt the cipher, consists of all possible combinations of three lowercase characters.
For every decryption attempt it is checked if the plaintext contains common English words.
Once this is the case, the sum of all the ascii codes of each character in this plaintext is printed.   

## Run the application
This application has no dependencies so can be ran from the command-line:
```
python solution\solution59.py
```
Requirement is that there is a file called *p059_cipher.txt* in the same directory as where the solution59.py files resides.


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
