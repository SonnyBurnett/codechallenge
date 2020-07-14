#
# Euler Problem 1
#
# Author: Taco Bakker
#
# Find the sum of all the multiples of 3 or 5 below 1000.
#
import time


__version__ = 1.0

MAX_NUMBER = 1000

#
# Simple version
#
start1 = time.time()
answer1 = 0
for x in range(MAX_NUMBER):
    if x % 3 == 0 or x % 5 == 0:
        answer1 += x
print("Answer1:", answer1, "it took me ", time.time() - start1, " seconds")

#
# list version long
#
start3 = time.time()
all_multiples = []
for x in range(MAX_NUMBER):
    if x % 3 == 0 or x % 5 == 0:
        all_multiples.append(x)
answer3 = sum(all_multiples)
print("Answer3:", answer3, "it took me ", time.time() - start3, " seconds")

#
# list version short
#
start4 = time.time()
answer4 = sum([x for x in range(MAX_NUMBER) if x % 3 == 0 or x % 5 == 0])
print("Answer4:", answer4, "it took me ", time.time() - start4, " seconds")

#
# Another list version
#
start5 = time.time()
list3 = [x for x in range(3, MAX_NUMBER, 3)]
list5 = [x for x in range(5, MAX_NUMBER, 5)]
answer5 = sum(set(list3+list5))
print("Answer5:", answer5, "it took me ", time.time() - start5, " seconds")

#
# Yet Another list version
#
start6 = time.time()
answer6 = sum(set([x for x in range(3, MAX_NUMBER, 3)]+[x for x in range(5, MAX_NUMBER, 5)]))
print("Answer6:", answer6, "it took me ", time.time() - start6, " seconds")

#
# One line of code version
#
start2 = time.time()
print("Answer2:",
      sum(map(lambda x: x if x % 3 == 0 or x % 5 == 0 else 0, range(MAX_NUMBER))),
      "it took me ", time.time() - start2, " seconds")


#
# Using predicate without lambda
#
start10 = time.time()

def is_division_of_3_or_5(x):
    return x % 3 == 0 or x % 5 == 0
result = sum(filter(is_division_of_3_or_5, range(MAX_NUMBER)))
print("Answer10:", result,  "it took me ", time.time() - start10, " seconds")


#
# Solution using a predicate in combination with lambda
#
start11 = time.time()
result = sum(filter(lambda x : x % 3 == 0 or x % 5 == 0, range(MAX_NUMBER)))
print("Answer11:", result,  "it took me ", time.time() - start11, " seconds")
