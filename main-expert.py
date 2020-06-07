'''
Author: Mike van den Berge
Date: 06-Jun-2020
'''
import math

def triangles(n):
    # see https://nl.wikipedia.org/wiki/Driehoeksgetal
    return (n * (n + 1) / 2)

def NumberOfDivisors(n):
    divisors = 0
    max_range = int(math.ceil(math.sqrt(n)))
    #slow code for i in range(1, n + 1):
    for i in range(1, max_range):
        if n % i == 0:
            divisors += 2
    return divisors

div_search = int(input("Number of divisors: "))
div = 0
i = 1
print("Calculating, please standby")
while True:
    triangle = triangles(i);
    div = NumberOfDivisors(triangle)
    if div >= div_search:
        break
    i += 1
print("Found triangle: " + str(int(triangle)))