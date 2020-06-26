'''
https://projecteuler.net/problem=41

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
'''
from typing import Any, Dict
from itertools import count, takewhile, permutations


class PrimeGenerator():
  @staticmethod
  def postponed_sieve():                 # postponed sieve, by Will Ness
    yield 2
    yield 3
    yield 5
    yield 7                              # original code David Eppstein,
    sieve: Dict[Any, Any] = {}           # Alex Martelli, ActiveState Recipe 2002
    ps = PrimeGenerator.postponed_sieve()               # a separate base Primes Supply:
    p = next(ps) and next(ps)            # (3) a Prime to add to dict
    q = p * p                            # (9) its sQuare
    for c in count(9, 2):                # the Candidate
      if c in sieve:                 # c's a multiple of some base prime
        s = sieve.pop(c)             # i.e. a composite ; or
      elif c < q:
        yield c                      # a prime
        continue
      else:   # (c==q):              # or the next base prime's square:
        s = count(q + 2 * p, 2 * p)  # (9+6, by 6 : 15,21,27,33,...)
        p = next(ps)                 # (5)
        q = p * p                    # (25)
      for m in s:                # the next multiple
        if m not in sieve:       # no duplicates
          break
      sieve[m] = s               # original test entry: ideone.com/WFv4f


class Pandigit():
  def __init__(self):
    self.__min_prime = 0
    self.__max_prime = 0

  def is_number_pandigital(self, number: int) -> bool:
    if len(set(str(number))) == len(str(number)):
      return True
    return False

  def __leg_max_prime(self, number: int) -> bool:
    return number <= self.__max_prime

  def get_primes_in_range(self, min_prime: int, max_prime: int):
    self.__min_prime = min_prime
    self.__max_prime = max_prime
    return [x for x in takewhile(self.__leg_max_prime, PrimeGenerator.postponed_sieve()) if x >= self.__min_prime]

  def get_pandigital_primes_in_range(self, min_prime, max_prime):
    return [x for x in self.get_primes_in_range(min_prime, max_prime) if self.is_number_pandigital(x)]

  def get_max_pandigital_prime_in_range(self, min_prime, max_prime):
    return max(self.get_pandigital_primes_in_range(min_prime, max_prime))

  def get_pandigital_prime_list(self, number):
    a = [x for x in [(lambda y: int(''.join(y))) for y in permutations(str(number), len(str(number)))] if self.is_prime(x)]
    return a
    # return [int(''.join(x)) for x in permutations(str(number), len(str(number))) if self.is_prime(int(''.join(x)))]

  def get_max_pandigital_prime_in_range_new(self, number):
    return max(self.get_pandigital_prime_list(number))

  def is_prime(self, n):
    if n == 2 or n == 3:
      return True
    if n < 2 or n % 2 == 0:
      return False
    if n < 9:
      return True
    if n % 3 == 0:
      return False
    r = int(n**0.5)
    f = 5
    while f <= r:
      if n % f == 0:
        return False
      if n % (f + 2) == 0:
        return False
      f += 6
    return True

  def euler_solution(self):
    return self.get_max_pandigital_prime_in_range_new(987654321)


def main():
  '''
  main function
  '''
  _pandigit = Pandigit()
  print('Solution for the Euler 041 problem:')
  # prints: ???
  print(_pandigit.euler_solution())


if __name__ == "__main__":
  main()
