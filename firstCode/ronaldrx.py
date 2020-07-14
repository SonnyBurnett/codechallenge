'''
Score 3.5
   Does it run 0.5. Yes but very slowly
   Names OK: 1
   Linted: 1
   Language: 0 Roll your own for loops
   Single Responsibility: 0 
   DeepSource: 1
   Tests: 0
'''
limit = 500
triangle = 1
x = 1

import math

def factors(num):
    result_list = []
    max_val = int(math.sqrt(num))
    i = max_val
    while max_val >= i >= 1:
        if i == math.sqrt(num):
            result_list.append(i)
        elif num % i == 0:
            result_list.insert(0, i)
            result_list.append(int(num / i))
        i -= 1
    return (result_list)

while len(factors(triangle)) <= limit:
    x += 1
    triangle = triangle + x

print(triangle)
