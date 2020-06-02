import itertools


def naturals():
    """
    Generator for natural numbers.

    I chose for itertools.count instead of writing that function myself, which would be something like:

    def naturals():
        x = 0
        while True:
            yield x
            x += 1
    """
    return itertools.count(1, 1)
