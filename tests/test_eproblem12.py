import unittest

from eproblems.eproblem12 import prime_factors


class Tep12(unittest.TestCase):
    def test_prime_factors(self):
        self.assertEqual(prime_factors(28), [1, 2, 2, 7, 28])


if __name__ == '__main__':
    unittest.main()
