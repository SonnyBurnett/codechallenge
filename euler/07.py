'''
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
from itertools import count, takewhile
from time import time

                                       # ideone.com/aVndFM
def postponed_sieve():                 # postponed sieve, by Will Ness      
  yield 2; yield 3; yield 5; yield 7;  # original code David Eppstein, 
  sieve = {}                           # Alex Martelli, ActiveState Recipe 2002
  ps = postponed_sieve()               # a separate base Primes Supply:
  p = next(ps) and next(ps)            # (3) a Prime to add to dict
  q = p*p                              # (9) its sQuare 
  for c in count(9,2):                 # the Candidate
    if c in sieve:             # c's a multiple of some base prime
      s = sieve.pop(c)         # i.e. a composite ; or
    elif c < q:  
      yield c                  # a prime
      continue              
    else:   # (c==q):          # or the next base prime's square:
      s=count(q+2*p,2*p)       #    (9+6, by 6 : 15,21,27,33,...)
      p=next(ps)               #    (5)
      q=p*p                    #    (25)
    for m in s:                # the next multiple 
      if m not in sieve:       # no duplicates
        break
    sieve[m] = s               # original test entry: ideone.com/WFv4f

n = 10001
counter = 1
start_time = time()
for prime in postponed_sieve():
  #print(prime)
  if counter < n:
    counter += 1
  else:
    break

print("done in {}".format(time() - start_time))
print(prime)
