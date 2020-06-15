'''
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
'''

'''
To solve this we need to multiply all the numbers from 1 till 20
this gives - 2432902008176640000 - not so small number
Better solution is to calculate a least common multiple of all the numbers that are in the 
range from 1 till 20.
Least common multiple (lcm) lambda function in combination with the reduce method 
makes sure that we get lcm for all the numbers in the range
'''
from math import gcd
from functools import reduce

RANGE = 20
TEST_RANGE = list(range(1, RANGE + 1))

print("Searching for a number that can be divided by following numbers:")
print(TEST_RANGE)

print(reduce(lambda x, y: (x * y) // gcd(x, y), TEST_RANGE))
