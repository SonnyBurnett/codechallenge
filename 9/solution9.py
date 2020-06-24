import math
from functools import reduce
product = reduce((lambda x, y: x * y), [[a,b,c] for a in range(100, 500) for b in range(101, 500) for c in range(102, 500) if
                                        (a < b < c == math.sqrt(a ** 2 + b ** 2) and a + b + c == 1000)][0])
print("Product = {}".format(product))