"""
Stuff we are probably going to need more.
"""


def list_factors(num):
    """ 
    Returns a set of all factors of a number (num)
    """ 
    factors = {1}
    factors.add(num)
    limit = num
    i = 2
    while i < limit:
        if num % i == 0:
            factors.add(i)
            limit = num/i
            factors.add(limit) 
        i += 1
    return factors


def fibonacci():
    """
    Fibonacci Generator
    """
    start, new = 0, 1
    while True:
        yield start
        start, new = new, start + new
        