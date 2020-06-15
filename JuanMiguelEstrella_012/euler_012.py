from functools import reduce
import itertools


def factor_count(n):
    if n == 0:
        return 0

    midpoint = int(n**0.5)
    list_of_factors = ([factor, n//factor] for factor in range(1, midpoint+1) if n % factor == 0)
    total_factors = reduce((lambda a, b: a+b), list_of_factors)
    count = len(set(total_factors))

    return count


def get_triangle(n):
    return sum(range(0, n+1))


number_of_divisors = 500
for i in itertools.count():
    triangle_number = get_triangle(i)
    number_of_factors = factor_count(triangle_number)
    if number_of_factors > number_of_divisors:
        print(triangle_number)
        print(number_of_factors)
        break
