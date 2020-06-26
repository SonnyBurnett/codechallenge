import unittest
from .p041 import Pandigit


class Test_p041(unittest.TestCase):
  def test_euler(self):
    _pandigit = Pandigit()
    result = _pandigit.get_primes_in_range(100, 1000)
    result = _pandigit.euler_solution()
    self.assertEqual(result, 0)
