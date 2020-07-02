import unittest
from typing import List
from .p041 import Pandigit


class Test_p041(unittest.TestCase):
  def test_euler(self):
    result = Pandigit.euler_solution()
    self.assertEqual(result, 7652413)

  def test_prime(self):
    self.assertTrue(Pandigit.is_prime(5))
    self.assertTrue(Pandigit.is_prime(7652413))
    self.assertTrue(Pandigit.is_prime(13))

  def test_pandigits(self):
    n_digit = 3
    expected_result: List[int] = []
    result = Pandigit.get_longest_pandigital_primes(n_digit)
    self.assertEqual(expected_result, result)
    self.assertEqual(Pandigit.get_max_pandigital_prime_for_n_base(n_digit), None)

    n_digit = 4
    expected_result = [1423, 2143, 2341, 4231]
    result = Pandigit.get_longest_pandigital_primes(n_digit)
    self.assertEqual(expected_result, result)
