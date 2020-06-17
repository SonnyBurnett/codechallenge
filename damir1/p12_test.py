import unittest
from .p12 import PrimeCalc


class Test_p12(unittest.TestCase):
  def test_prime_factors(self):
    # Test 7th triangle number = 28
    # Prime factors are = 1, 2, 4, 7, 14, 28
    _prime_calc = PrimeCalc()
    _prime_factors = _prime_calc._calc_prime_factors(28)
    self.assertEqual(_prime_factors, [2, 2, 7])

  def test_combined_prime_factors(self):
    _prime_calc = PrimeCalc()
    self.assertEqual(_prime_calc._combine_prime_factors([2, 2, 7]), [1, 2, 4, 7, 14, 28])

  def test_euler(self):
    # Test Euler problem
    _prime_calc = PrimeCalc()
    self.assertEqual(_prime_calc.euler_solution(), 76576500)

  def test_type_errors(self):
    _prime_calc = PrimeCalc()
    self.assertRaises(TypeError, _prime_calc._combine_prime_factors, 100)
    self.assertRaises(TypeError, _prime_calc._combine_prime_factors, [2, 2, '7'])
    self.assertRaises(TypeError, _prime_calc._calc_prime_factors, [2, 2, '7'])
    self.assertRaises(TypeError, _prime_calc._calc_prime_factors, '7')

  def test_value_errors(self):
    # self.assertRaises(ValueError, sum_fibonacci_with_limit_and_mod_number, 100, -2)
    # self.assertRaises(ValueError, sum_fibonacci_with_limit_and_mod_number, 0, 3)
    # self.assertRaises(ValueError, sum_fibonacci_with_limit_and_mod_number, -100, 3)
    pass
