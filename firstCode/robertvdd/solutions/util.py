"""
Stuff we are probably going to need more.
"""


def list_factors(num):
    """ 
    Returns a set of all factors of a number (num)
    """ 
    # we can default add 1 and the number itself.
    factors = {1}
    factors.add(num)
    # then we can loop from 2 to the currently other found factor. (which starts as the number itself)
    limit = num
    i = 2
    while i < limit:
        if num % i == 0:
            factors.add(i)
            limit = num/i # also add the other factor which becomes our new search limit
            factors.add(limit) 
        i += 1
    return factors
