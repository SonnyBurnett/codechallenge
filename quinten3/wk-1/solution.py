import itertools


def naturals():
    """
    Generator for natural numbers.
    """
    return itertools.count(1, 1)


def triangle_numbers():
    """
    Generator for triangle numbers.

    The sequence of triangle numbers is generated by adding the natural numbers.
    So the 7th triangle number is 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms are:
    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
    """
    t = 0
    for n in naturals():
        t += n
        yield t


class FactorCache:
    def __init__(self):
        self.factors = {}

    def record_factors(self, n):
        if n < 2:
            return
        if n in self.factors:
            return
        for i in itertools.count(2, 1):
            divided = n / i
            if divided.is_integer():
                d = int(divided)
                # note that if n is prime, d will be 1
                if d == 1:
                    self.factors[n] = [i]
                else:
                    self.factors[n] = [d, i]
                    self.record_factors(i)
                    self.record_factors(d)
                return

    def prime_factors(self, n):
        if n < 2:
            return
        if n not in self.factors:
            self.record_factors(n)
        fs = self.factors[n]
        if len(fs) == 1:
            return fs
        else:
            smallers = self.prime_factors(fs[0]) + self.prime_factors(fs[1])
            smallers.sort()
            return smallers


def nr_of_divisors(n, factor_cache=FactorCache()):
    if n == 1:
        return 1

    primes = factor_cache.prime_factors(n)

    nr_of_divisors = 1
    former_prime = 1
    nr_of_current_prime = 0

    for p in primes:
        nr_of_current_prime += 1
        if p != former_prime:
            nr_of_divisors *= (nr_of_current_prime + 1)
            nr_of_current_prime = 0
            former_prime = p

    return nr_of_divisors


def first_triangle_with_more_divisors_than(n, factor_cache=FactorCache()):
    for t in triangle_numbers():
        if nr_of_divisors(t, factor_cache) > n:
            return t


print("The first triangle number with over 500 divisors is {}".format(
    first_triangle_with_more_divisors_than(500)))
