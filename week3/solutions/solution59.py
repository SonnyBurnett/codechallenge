from itertools import product, cycle

def keyGen():
    a, z = 97, 122
    for x in product(range(a, z+1), repeat=3):
        yield x


def decrypt(message, key):
    return [ x^y for x, y in zip(message, cycle(key)) ]
