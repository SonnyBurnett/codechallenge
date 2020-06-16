# EulerProject  - problem 54

[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/xmayeur/euler54/?ref=repository-badge)
[![Build Status](https://dev.azure.com/xmayeur/Euler54/_apis/build/status/xmayeur.euler54?branchName=master)](https://dev.azure.com/xmayeur/Euler54/_build/latest?definitionId=15&branchName=master)

## Problem reference:
* url: [problem 54](https://projecteuler.net/problem=54)

## Problem: how many hands does Player1 win? 

* result = 376

## Method used to solve the problem
The file `p054_poker.txt` contains the hands of both players
The card values are first mapped to its numeric values 2-14 corresponding to 2-9, T, J, Q, K

In the method `get_rank`, we converts the hands into score/value tuples representing the frequency of the card value: 

e.g. if hand = ['KH', '4H', '6H', '7H', '3H'], the calculated score tuple is
((1,1,1,1,1), (13, 7, 6, 4, 3)). The first tuple is the frequency of each value in the hand, the second tuple is the cards values in descending order.


Getting the score for straight & flush is a little bit more cumbersome. 

In the main module, finding the winner of a hand is as easy as comparing the score tuple. When scores tie, the second item in the tuples is used in the comparison to find the winner.

* the number of won hands fo Player1 is finally displayed after summing the score for player 1.

## Tests 

* Unit tests are performed using pytest.
* test file is test.py, asserting 100 combinations of each ranking type   
* It uses the `@pytest.mark.parametrize` decorator in order to pass each hands combination as a parameter to the test routine  
* pytest execution is automated in the [Azure DevOps](pipeline https://dev.azure.com/xmayeur/Euler54)

* Tests results: [results](https://dev.azure.com/xmayeur/Euler54/_build/results?buildId=238&view=ms.vss-test-web.build-test-results-tab) 