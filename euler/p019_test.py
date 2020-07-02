import unittest
from .p019 import Days


class Test_p019(unittest.TestCase):
  def test_euler(self):
    sundays = Days.euler_solution()
    self.assertEqual(sundays, 171)
