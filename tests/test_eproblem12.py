import unittest
import sys

sys.path.insert(1, '../eproblems')  # Weird this is needed for pipelines to resolve the path.

from eproblems.eproblem12 import prime_factors


class Tep12(unittest.TestCase):
    def test_prime_factors(self):
        self.assertEqual(prime_factors(28), [1, 2, 2, 7, 28])

