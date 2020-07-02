import unittest
from .p020 import Facto


class Test_p020(unittest.TestCase):
  def test_euler(self):
    _facto = Facto()
    self.assertEqual(_facto.euler_solution(), 648)
