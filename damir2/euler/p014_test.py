import unittest
from .p014 import Collatz


class Test_p014(unittest.TestCase):
  def test(self):
    # Test length for some small numbers
    _collatz = Collatz()
    # 9 → 28 → 14 → 7 → 22 → 11 → 34 → 17 → 52 → 26 → 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1 = 20 terms
    self.assertEqual(_collatz.get_starting_num_with_longest_Collatz(14), 9)

  def test_euler(self):
    # Test Euler problem
    _collatz = Collatz()
    self.assertEqual(_collatz.get_starting_num_with_longest_Collatz(1000000), 837799)

  def test_exceptions(self):
    _collatz = Collatz()
    self.assertRaises(TypeError, _collatz.get_starting_num_with_longest_Collatz, '23')
    self.assertRaises(ValueError, _collatz.get_starting_num_with_longest_Collatz, -23)
