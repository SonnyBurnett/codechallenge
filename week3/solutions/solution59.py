from itertools import product

def KeyGen():
    a, z = 97, 122
    for x in product(range(a, z+1), repeat=3):
        yield x