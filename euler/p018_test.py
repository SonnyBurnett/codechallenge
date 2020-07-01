import unittest
from .p018 import Triangle


class Test_p018(unittest.TestCase):
  def test_euler(self):
    _triangle = Triangle()
    self.assertEqual(_triangle.euler_solution(), 1074)
