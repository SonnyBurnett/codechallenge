import solution
import sys


def test_natural_generator():
    N = solution.naturals()
    assert next(N) == 1
    assert next(N) == 2
    assert next(N) == 3
    assert next(N) == 4


def test_triangle_numbers_generator():
    T = solution.triangle_numbers()
    assert next(T) == 1
    assert next(T) == 3
    assert next(T) == 6
    assert next(T) == 10


def test_factor_recording():
    # 1 is not considered prime, so don't record it as a factor
    factor_cache = solution.FactorCache()
    factor_cache.record_factors(1)
    assert len(factor_cache.factors) == 0

    # see factor recording of 4: going down its greatest dividers until arriving at primes
    factor_cache = solution.FactorCache()
    factor_cache.record_factors(4)
    assert factor_cache.factors == {
        2: [2],
        4: [2, 2]
    }

    # see factor recording of 28: the structure for that is added
    factor_cache = solution.FactorCache()
    factor_cache.record_factors(28)
    assert factor_cache.factors == {
        2: [2],
        7: [7],
        14: [7, 2],
        28: [14, 2]
    }

    # running it again does not change the factor cache (and is extremely quick)
    factor_cache.record_factors(28)
    assert factor_cache.factors == {
        2: [2],
        7: [7],
        14: [7, 2],
        28: [14, 2]
    }


def test_prime_factors():
    factor_cache = solution.FactorCache()
    assert factor_cache.prime_factors(1) == None
    assert factor_cache.prime_factors(2) == [2]
    assert factor_cache.prime_factors(3) == [3]
    assert factor_cache.prime_factors(4) == [2, 2]
    assert factor_cache.prime_factors(28) == [2, 2, 7]


def test_nr_of_divisors():
    assert solution.nr_of_divisors(1) == 1
    assert solution.nr_of_divisors(3) == 2
    assert solution.nr_of_divisors(6) == 4
    assert solution.nr_of_divisors(10) == 4
    assert solution.nr_of_divisors(15) == 4
    assert solution.nr_of_divisors(21) == 4
    assert solution.nr_of_divisors(28) == 6

    # and reusing a cache is possible for efficiency:
    factor_cache = solution.FactorCache()
    assert solution.nr_of_divisors(28, factor_cache) == 6
    assert solution.nr_of_divisors(28, factor_cache) == 6


def test_first_triangle_with_more_divisors_than():
    assert solution.first_triangle_with_more_divisors_than(1) == 3
    assert solution.first_triangle_with_more_divisors_than(2) == 6
    assert solution.first_triangle_with_more_divisors_than(5) == 28

    # and reusing a cache is possible for efficiency:
    factor_cache = solution.FactorCache()
    assert solution.first_triangle_with_more_divisors_than(
        5, factor_cache) == 28
    assert solution.first_triangle_with_more_divisors_than(
        5, factor_cache) == 28
