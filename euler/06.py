'''
https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,

1^2+2^2+...+10^2=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)^2=55^2=3025
Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the
first one hundred natural numbers and the square of the sum.
'''
'''
Solution: Using brute force
'''
from functools import reduce
from time import time

N = 100
start_time = time()

sum_of_sqr = sum([x**2 for x in range(1, N +1)])
sqr_of_sum = sum(range(1, N + 1))**2
print("sum of sqr = {} sqr of sums = {} difference = {}".format(sum_of_sqr, sqr_of_sum, sqr_of_sum - sum_of_sqr))
print("done in {}".format(time() - start_time))

'''
Solution using mathematical formulas
sum of first n squares = (n*(n+1)*(2*n+1))/6
sum of first n numbers = n*(n+1)/2
'''
start_time = time()
sum_of_sqr = int((N*(N+1)*(2*N+1))/6)
sqr_of_sum = int(N*(N+1)/2)**2
print("difference using formulas: {}".format(sqr_of_sum - sum_of_sqr))
print("done in {}".format(time() - start_time))
