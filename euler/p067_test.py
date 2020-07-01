import unittest
from .p067 import Triangle


class Test_p067(unittest.TestCase):
  def test_euler(self):
    _triangle = Triangle()
    self.assertEqual(_triangle.euler_solution(), 7273)
