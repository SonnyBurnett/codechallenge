import ex12
import sys


def test_natural_generator():
    N = ex12.naturals()
    assert next(N) == 1
    assert next(N) == 2
    assert next(N) == 3
    assert next(N) == 4


def test_triangle_numbers_generator():
    T = ex12.triangle_numbers()
    assert next(T) == 1
    assert next(T) == 3
    assert next(T) == 6
    assert next(T) == 10


# note that this test is flaky due to use of internal state that should not only be private but is also influenced by
# the order of the tests - fine for now though
def test_factor_recording():
    # 1 is not considered prime, so don't record it as a factor
    ex12.record_factors(1)
    assert len(ex12.factors) == 0

    # see factor recording of 4: going down its greatest dividers until arriving at primes
    ex12.record_factors(4)
    assert ex12.factors == {
        2: [2],
        4: [2, 2]
    }

    # see factor recording of 28: the structure for that is added
    ex12.record_factors(28)
    assert ex12.factors == {
        2: [2],
        4: [2, 2],
        7: [7],
        14: [7, 2],
        28: [14, 2]
    }

    # running it again does not change the factor cache
    ex12.record_factors(28)
    assert ex12.factors == {
        2: [2],
        4: [2, 2],
        7: [7],
        14: [7, 2],
        28: [14, 2]
    }


def test_prime_factors():
    assert ex12.prime_factors(1) == None
    assert ex12.prime_factors(2) == [2]
    assert ex12.prime_factors(3) == [3]
    assert ex12.prime_factors(4) == [2, 2]
    assert ex12.prime_factors(28) == [2, 2, 7]


def test_nr_of_divisors():
    assert ex12.nr_of_divisors(1) == 1
    assert ex12.nr_of_divisors(3) == 2
    assert ex12.nr_of_divisors(6) == 4
    assert ex12.nr_of_divisors(10) == 4
    assert ex12.nr_of_divisors(15) == 4
    assert ex12.nr_of_divisors(21) == 4
    assert ex12.nr_of_divisors(28) == 6
