# This program solves the https://projecteuler.net/problem=12

from functools import reduce
from itertools import combinations
from time import time

start_time = time()

i = 1
triangle = 0
current_max = 0

def _calc(big): #function to get all prime factors of a number
  ret = []
  if (None == big or big < 2):
    return ret
  for x in range(2, big + 1):
    while (big % x == 0):
      ret.append(x)
      big = int(big / x)
      if (big == 1):
        #reached the end of the divisions, no need to loop further
        return ret
  return ret
  

while True:
  triangle += i
  factors = _calc(triangle)
  results = sorted(factors)

  answers = []
  #combine and multiply all prime factors
  if (len(results) >= 2):
    for k in reversed(range(len(results))):
      #combinations creates iterator with all possible combinations of elements in
      #results array, size is determined by second parameter
      temp_var = list(combinations(results, k + 1))
      for r in range(len(temp_var)):
        #reduce is used to apply the function to all items in the sequence
        answers.append(reduce(lambda x, y: x * y, temp_var[r]))

  answers.insert(0, 1) #insert 1 to the answers, the triangle number was added by multiplication of prime factors
  answers = sorted(list(set(answers))) #eliminate duplicates and sort the list of factors

  if (len(answers) > current_max): #track current max number of factors
    current_max = len(answers)
    print("Current status: ", i, triangle, current_max)

  if (len(answers) > 500): #got the number that has more than 500 factors
    print("Current factors: ", answers)
    break
  
  i += 1

print("Done in %s seconds!" % (time() - start_time))