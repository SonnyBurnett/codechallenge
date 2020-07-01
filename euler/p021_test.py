import unittest
from .p021 import PrimeCalc


class Test_p021(unittest.TestCase):
  def test_euler(self):
    _el_primo = PrimeCalc()
    res = _el_primo.sum_amicables(10000)
    self.assertEqual(res, 31626)
