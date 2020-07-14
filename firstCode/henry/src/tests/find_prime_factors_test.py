import sys
import unittest

sys.path.append('../')
from functions import find_prime_factors as functions


class TestGetPrimeNumbers(unittest.TestCase):

    def test_two(self):
        primes = functions.find_prime_factors(2)

        self.assertEqual(1, len(primes))
        self.assertEqual(1, primes[2])

    def test_three(self):
        primes = functions.find_prime_factors(3)

        self.assertEqual(1, len(primes))
        self.assertEqual(1, primes[3])

    def test_nine(self):
        primes = functions.find_prime_factors(9)

        self.assertEqual(1, len(primes))
        self.assertEqual(2, primes[3])

    def test_1080(self):
        primes = functions.find_prime_factors(1080)

        self.assertEqual(3, len(primes))
        self.assertEqual(3, primes[2])
        self.assertEqual(3, primes[3])
        self.assertEqual(1, primes[5])


if __name__ == '__main__':
    unittest.main()