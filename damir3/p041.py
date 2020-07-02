'''
https://projecteuler.net/problem=41

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
'''
from typing import List, Optional
from itertools import permutations


class Pandigit():
  @staticmethod
  def get_max_pandigital_prime_for_n_base(n_base: int) -> Optional[int]:
    if not isinstance(n_base, int):
      raise TypeError('Integer larger than 2 expected')
    if n_base <= 2:
      raise ValueError('Integer larger than 2 expected')

    longest_pandigitals = Pandigit.get_longest_pandigital_primes(n_base)
    if len(longest_pandigitals) > 0:
      return max(longest_pandigitals)
    return None

  @staticmethod
  def get_pandigital_primes(pandigital_number: int) -> List[int]:
    if not isinstance(pandigital_number, int):
      raise TypeError('Integer longer than 2 digits expected')
    if len(str(pandigital_number)) <= 2:
      raise ValueError('Integer longer than 2 digits expected')

    pandigital_permutations = [int(''.join(y)) for y in permutations(str(pandigital_number), len(str(pandigital_number))) if y[-1] in '1379']
    return [x for x in pandigital_permutations if Pandigit.is_prime(x)]

  @staticmethod
  def get_longest_pandigital_primes(n_base: int) -> List[int]:
    if not isinstance(n_base, int):
      raise TypeError('Integer larger than 2 expected')
    if n_base <= 2:
      raise ValueError('Integer larger than 2 expected')

    pandigits = []
    for i in range(n_base, 2, -1):
      pandigit_i_base_long = int(''.join([str(x) for x in range(i + 1)]))
      pandigits += Pandigit.get_pandigital_primes(pandigit_i_base_long)
      if len(pandigits) > 0:
        break
    return pandigits

  @staticmethod
  def is_prime(n: int) -> bool:
    if not isinstance(n, int):
      raise TypeError('Integer expected')

    if n in (2, 3):
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

  @staticmethod
  def euler_solution() -> Optional[int]:
    return Pandigit.get_max_pandigital_prime_for_n_base(9)


def main():
  '''
  main function
  '''
  print('Solution for the Euler 041 problem:')
  # prints: 7652413
  print(Pandigit.euler_solution())


if __name__ == "__main__":
  main()
