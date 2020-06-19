# POKER WINNER
This application determines, out of two hands of cards, which hand has the most points and is the winner.

## Run the application
This application has no dependencies so can be ran from the command-line:
```
python solution54.py
```
Requirement is that there is a file called *poker.txt* in the same directory as where the solution54.py files resides.
This file must adhere to the following layout:
- each line contains data for two hands of cards, looking like: 2H 2D 4C 4D 4S 3C 3D 3S 9S 9D
- cards per line must be existing playcards and no jokers
- cards per line may occur only once

## Test the application
In order to test the application one can run
```
pytest tests\test_solution54.py
```