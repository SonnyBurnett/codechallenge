import sys
import unittest

sys.path.append('../')
from functions import count_divisors as functions


class TestGetPrimeNumbers(unittest.TestCase):

    def test_naive_6(self):
        result = functions.count_divisors_naive(6)
        self.assertEqual(4, result)

    def test_naive_100(self):
        result = functions.count_divisors_naive(100)
        self.assertEqual(9, result)

    def test_naive_1000(self):
        result = functions.count_divisors_naive(1000)
        self.assertEqual(16, result)

    def test_naive_383333(self):
        result = functions.count_divisors_naive(383333)
        self.assertEqual(4, result)

    def test_reduced_by_pairs_6(self):
        result = functions.count_divisors_reduced_by_pairs(6)
        self.assertEqual(4, result)

    def test_reduced_by_pairs_100(self):
        result = functions.count_divisors_reduced_by_pairs(100)
        self.assertEqual(9, result)

    def test_reduced_by_pairs_1000(self):
        result = functions.count_divisors_reduced_by_pairs(1000)
        self.assertEqual(16, result)

    def test_reduced_by_pairs_383333(self):
        result = functions.count_divisors_reduced_by_pairs(383333)
        self.assertEqual(4, result)

    def test_reduced_by_primes_6(self):
        result = functions.count_divisors_reduced_by_primes(6)
        self.assertEqual(4, result)

    def test_reduced_by_primes_100(self):
        result = functions.count_divisors_reduced_by_primes(100)
        self.assertEqual(9, result)

    def test_reduced_by_primes_1000(self):
        result = functions.count_divisors_reduced_by_primes(1000)
        self.assertEqual(16, result)

    def test_reduced_by_primes_383333(self):
        result = functions.count_divisors_reduced_by_primes(383333)
        self.assertEqual(4, result)

if __name__ == '__main__':
    unittest.main()