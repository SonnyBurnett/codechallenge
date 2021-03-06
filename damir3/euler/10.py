'''
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from itertools import count
from typing import Any, Dict

n = 2000000


def postponed_sieve():                 # ideone.com/aVndFM
  yield 2                              # postponed sieve, by Will Ness
  yield 3
  yield 5
  yield 7                              # original code David Eppstein,
  sieve: Dict[Any, Any] = {}                           # Alex Martelli, ActiveState Recipe 2002
  ps = postponed_sieve()               # a separate base Primes Supply:
  p = next(ps) and next(ps)            # (3) a Prime to add to dict
  q = p * p                            # (9) its sQuare
  for c in count(9, 2):                # the Candidate
    if c in sieve:               # c's a multiple of some base prime
      s = sieve.pop(c)           # i.e. a composite ; or
    elif c < q:
      yield c                    # a prime
      continue
    else:   # (c==q):            # or the next base prime's square:
      s = count(q + 2 * p, 2 * p)  # (9+6, by 6 : 15,21,27,33,...)
      p = next(ps)                 # (5)
      q = p * p                    # (25)
    for m in s:                  # the next multiple
      if m not in sieve:         # no duplicates
        break
    sieve[m] = s               # original test entry: ideone.com/WFv4f


prime_sum = 0
for prime in postponed_sieve():
  if prime < n:
    prime_sum += prime
  else:
    break

print('Sum of primes below {} is {}'.format(n, prime_sum))
