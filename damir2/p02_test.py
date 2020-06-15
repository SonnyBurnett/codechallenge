import unittest
from p02 import sum_fibonacci_with_limit_and_mod_number

class Test_p02(unittest.TestCase):
  def test(self):
    #Test sum of first 10 even fibonacci numbers
    self.assertEqual(sum_fibonacci_with_limit_and_mod_number(100, 2), 44)
    #Test sum of all Fibonacci numbers less than 9
    self.assertEqual(sum_fibonacci_with_limit_and_mod_number(9, 1), 20)
  
  def test_euler(self):
    #Test Euler problem
    self.assertEqual(sum_fibonacci_with_limit_and_mod_number(4000000, 2), 4613732)

  def test_type_errors(self):
    self.assertRaises(TypeError, sum_fibonacci_with_limit_and_mod_number, 100, '2')
    self.assertRaises(TypeError, sum_fibonacci_with_limit_and_mod_number, '100', '2')
    self.assertRaises(TypeError, sum_fibonacci_with_limit_and_mod_number, 100.99, '2')

  def test_value_errors(self):
    self.assertRaises(ValueError, sum_fibonacci_with_limit_and_mod_number, 100, -2)
    self.assertRaises(ValueError, sum_fibonacci_with_limit_and_mod_number, 0, 3)
    self.assertRaises(ValueError, sum_fibonacci_with_limit_and_mod_number, -100, 3)
