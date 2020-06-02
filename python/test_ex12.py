import ex12


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


def divisors(n):
    return [1]


def test_divisors():
    assert divisors(1) == [1]
