# EulerProject  - problem 54

* url: [problem 54](https://projecteuler.net/problem=54)

## Problem: how many hands does Player1 win? 

* result = ...

## Method used to solve the problem

The program is structured as follow:
* `p054_pocker.txt` file is read and converted as a Pandas DataFrame representing both user's hands
* a `get_score` method is applied on the dataFrame and return the score
    * the score is a DataFrame with 5 columns, each row being a game:
        - the rank of Player1
        - the score the for current hand of Player1 (1=win, 0=lost)
        - the rank of Player2
        - the score of Player2
        - the original hand of both players

* The scores are saved into a `results.csv` comma-separated file
* the number of won hands fo Player1 is finally displayed

## Test 

* Unit tests are performed using pytest
* test file is test.py       

 
 