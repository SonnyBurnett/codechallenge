'''
Score 4.5
   Does it run 0.5 not optimal solution, but OK
   Names OK: 1
   Linted: 0.5   Lost half a mark because had lots of comments to explain things: if you need comments... rewrite the code
   Language: 0.5 Used while/break (bad) but also used for loops. List Comprehensions would be much better
   Single Responsibility: 1 Some effort but still a lot going on
   DeepSource: 1  <--- Taco please check
   Tests:0

   '''

# This program solves the https://projecteuler.net/problem=12

from functools import reduce
from itertools import combinations
from time import time

start_time = time()

i = 1
triangle = 0
current_max = 0

#function to get all prime factors of a number
def _calc_prime_factors(number):
  ret = []
  if (None == number or number < 2):
    return ret
  for x in range(2, number + 1):
    while (number % x == 0):
      ret.append(x)
      number = int(number / x)
      if (number == 1):
        #reached the end of the divisions, no need to loop further
        return ret
  return ret

#combine and multiply all prime factors
def _combine_prime_factors(primes):
  combined_primes = []
  if (len(primes) >= 2):
    for k in reversed(range(len(primes))):
      #combinations creates iterator with all possible combinations of elements in
      #primes array, size is determined by second parameter
      temp_var = list(combinations(primes, k + 1))
      for r in range(len(temp_var)):
        #reduce is used to apply the function to all items in the sequence
        combined_primes.append(reduce(lambda x, y: x * y, temp_var[r]))
  else:
    combined_primes = primes

  #insert 1 to the answers
  combined_primes.insert(0, 1)
  #eliminate duplicates and sort the list of factors
  combined_primes = sorted(list(set(combined_primes)))
  return combined_primes

while True:
  triangle += i

  factors = _calc_prime_factors(triangle)
  answers = _combine_prime_factors(factors)

  #track max number of combined factors
  if (len(answers) > current_max): 
    current_max = len(answers)
    print("Current status: ", i, triangle, current_max)

  #got the number that has more than 500 factors
  if (len(answers) > 500): 
    print("Current factors: ", answers)
    break
  
  i += 1

print("Done in %s seconds!" % (time() - start_time))
