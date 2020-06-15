import sys
from importlib import import_module

sys.path.append("../solutions")
testSubject = import_module('2')


print("TEST EULER EXAMPLE")
result = testSubject.sumEvenFibonacci(100)
assert 44 == result, "got %s, expected 44" % result


print("OFFICIAL EULER LIMIT")
result = testSubject.sumEvenFibonacci(4000000)
assert 4613732 == result, "got %s, expected 4613732" % result
