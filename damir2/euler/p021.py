'''
https://projecteuler.net/problem=21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
from functools import reduce
from itertools import combinations
from typing import List


class PrimeCalc():
  @staticmethod
  def calc_prime_factors(number: int) -> List[int]:
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
        temp_var = list(combinations(primes, k + 1))
        for r, _ in enumerate(temp_var):
          combined_primes.append(reduce(lambda x, y: x * y, temp_var[r]))
    else:
      combined_primes = primes

    combined_primes.insert(0, 1)
    combined_primes = sorted(list(set(combined_primes)))
    return combined_primes

  def sum_divisors(self, divisors, n):
    return sum([x for x in divisors if x < n])

  def sum_amicables(self, max_n):
    amicables = {k: self.sum_divisors(PrimeCalc.combine_prime_factors(PrimeCalc.calc_prime_factors(k)), k) for k in range(max_n)}
    return sum({k: v for (k, v) in amicables.items() if k != v and v in amicables.keys() and amicables.get(v) == k}.values())

  def euler_solution(self):
    return self.sum_amicables(10000)


def main():
  '''
  main function
  '''
  print('Solution for the Euler 021 problem:')
  # prints: 31626
  _el_primo = PrimeCalc()
  print(_el_primo.euler_solution())


if __name__ == "__main__":
  main()
