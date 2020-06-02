import ex12


def test_natural_generator():
    N = ex12.naturals()
    assert next(N) == 1
    assert next(N) == 2
    assert next(N) == 3
    assert next(N) == 4
