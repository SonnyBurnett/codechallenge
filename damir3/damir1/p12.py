# This program solves the https://projecteuler.net/problem=12

from functools import reduce
from itertools import combinations
from typing import List


class PrimeCalc():
  @staticmethod
  def calc_prime_factors(number: int) -> List[int]:
    '''
    function to get all prime factors of a number

    Parameters
    ----------
    number: int
      a number to calculate prime factors for

    Returns
    -------
    list
      array of prime factors
    '''
    if not isinstance(number, int):
      raise TypeError("Expected int number as a parameter!")
    ret: List[int] = []
    if (number is None or number < 2):
      return ret
    for x in range(2, number + 1):
      while (number % x == 0):
        ret.append(x)
        number = int(number / x)
        if (number == 1):
          return ret
    return ret

  @staticmethod
  def combine_prime_factors(primes: List[int]) -> List[int]:
    '''
    combine and multiply all prime factors
    '''
    if not isinstance(primes, list):
      raise TypeError('primes parameter expects a list of integer prime factors!')
    if not all(isinstance(n, int) for n in primes):
      raise TypeError('primes parameter expects a list of integer prime factors!')
    combined_primes = []
    if (len(primes) >= 2):
      for k in reversed(range(len(primes))):
        # combinations creates iterator with all possible combinations of elements in
        # primes array, size is determined by second parameter
        temp_var = list(combinations(primes, k + 1))
        for r, _ in enumerate(temp_var):
          combined_primes.append(reduce(lambda x, y: x * y, temp_var[r]))
    else:
      combined_primes = primes

    combined_primes.insert(0, 1)
    combined_primes = sorted(list(set(combined_primes)))
    return combined_primes

  def euler_solution(self) -> int:
    i = 1
    triangle = 0
    current_max = 0

    while True:
      triangle += i
      factors = self.calc_prime_factors(triangle)
      answers = self.combine_prime_factors(factors)

      if (len(answers) > current_max):
        current_max = len(answers)

      if (len(answers) > 500):
        break

      i += 1

    return triangle


def main():
  '''
  main function
  '''
  print('Solution for the Euler 012 problem:')
  _primeFactors = PrimeCalc()
  print('Triangle number: {euler}'.format(euler=_primeFactors.euler_solution()))


if __name__ == "__main__":
  main()
