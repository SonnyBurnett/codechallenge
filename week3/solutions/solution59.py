from itertools import product, cycle

def keyGen():
    a, z = 97, 122
    return product(range(a, z+1), repeat=3)


def XOR(message, key):
    return [ x^y for x, y in zip(message, cycle(key)) ]


def convertToAscii(message):
    return [ chr(x) for x in message ]


def decryptMessage(encrypted, key):
    return ''.join(convertToAscii(XOR(encrypted, key)))