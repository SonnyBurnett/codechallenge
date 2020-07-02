'''
https://projecteuler.net/problem=20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''
import math


class Facto():
  def __init__(self, factorial_number=1):
    self.__factorial_number = factorial_number

  def get_factorial(self, factorial_number):
    return math.factorial(factorial_number)

  def get_sum_of_digits(self, number):
    return sum([int(x) for x in str(number)])

  def euler_solution(self):
    return self.get_sum_of_digits(self.get_factorial(100))


def main():
  '''
  main function
  '''
  print('Solution for the Euler 020 problem:')
  # prints: 648
  _facto = Facto()
  print(_facto.euler_solution())


if __name__ == "__main__":
  main()
