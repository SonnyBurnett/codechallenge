'''
Author: Mike van den Berge
Date: 06-Jun-2020


 Score: 4.5
    Run 0.5 not the fastest method
    NamesOK 1. 
    Linted 0.5 inconsitant capitals in names.. ok maybe that should be in names but the place doesn't matter
    Libraries list / 0.5  Used While/break but For loop nice. Would like to see a list comprehension / filter but this was ok
    SingleResponsibility/1 some effort, but still a lot going on in each method
    Deepsource/1
    Testing 0/3
    
Score 5/10

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
