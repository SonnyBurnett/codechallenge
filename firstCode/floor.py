'''
Score 4.5
   Does it run 0.5 not optimal solution, but OK
   Names OK: 1
   Linted: 0.5   Lost half a mark because had lots of comments to explain things: if you need comments... rewrite the code
   Language: 0.5 Used for /break (bad) but also used for loops. List Comprehensions would be much better
   Single Responsibility: 1 Some effort but still a lot going on
   DeepSource: 1  <--- Taco please check
   Tests:0
   '''


import math

def nr_of_divisors(number):
    
    sqrt = math.sqrt(number)
    nr_divisors = 0;
    for i in range(1, int(sqrt) + 1):
        if(number % i == 0):
            if (i == sqrt):
                nr_divisors += 1
            else:
                nr_divisors += 2 # 2 divisors if you find 1 (2*4 = 8 so both 2 and 4 are divisors of 8)
    
    return nr_divisors

triangle_number = 0
for i in range(1,20001):
    triangle_number += i
        
    if (nr_of_divisors(triangle_number) >= 500):
        print('{}th triangle number is the first triangle number with at least 500 divisors'.format(i) )
        break
