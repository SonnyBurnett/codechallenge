import unittest
import sys

sys.path.insert(1, '../eproblems')  # Weird this is needed if the original python file has a local include.

from eproblems.eproblem41 import convert
from eproblems.eproblem41 import last_prime
from eproblems.eproblem41 import eproblem41


class Tep41(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(convert((0,)), 0)
        self.assertEqual(convert((1, 0,)), 10)
        self.assertEqual(convert((1, 0, 0,)), 100)
        self.assertEqual(convert((1, 0, 1,)), 101)
        self.assertEqual(convert((1, 1, 0,)), 110)
        self.assertEqual(convert((1, 1, 1,)), 111)

    def test_last_prime(self):
        self.assertEqual(last_prime([(1,), (13,)]), 13)
        self.assertEqual(last_prime([(1,), (13,), (7,)]), 7)

    def test_eproblem41(self):
        self.assertEqual(eproblem41(1), 1)
        self.assertEqual(eproblem41(2), 1)
        self.assertEqual(eproblem41(3), 1)
        self.assertEqual(eproblem41(4), 4231)
        self.assertEqual(eproblem41(5), 4231)
        self.assertEqual(eproblem41(6), 4231)
        self.assertEqual(eproblem41(7), 7652413)
        self.assertEqual(eproblem41(10), "Not implemented above n-digit 9!")

    def test_sol54(self):
        self.assertEqual(eproblem41(9), 7652413)


if __name__ == '__main__':
    unittest.main()
