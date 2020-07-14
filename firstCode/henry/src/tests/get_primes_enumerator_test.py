import sys
import unittest

sys.path.append('../')
from functions import get_primes_enumerator as functions


class TestGetPrimeNumbers(unittest.TestCase):

    def test_first_prime(self):
        primes_generator = functions.get_primes_enumerator()
        next_prime = next(primes_generator)
        self.assertEqual(2, next_prime)

    def test_second_prime(self):
        primes_generator = functions.get_primes_enumerator()

        next(primes_generator)
        next_prime = next(primes_generator)
        self.assertEqual(3, next_prime)

    def test_hundredth_prime(self):
        primes_generator = functions.get_primes_enumerator()

        for prime in range(99):
            next(primes_generator)

        next_prime = next(primes_generator)
        self.assertEqual(541, next_prime)

    def test_thousandth_prime(self):
        primes_generator = functions.get_primes_enumerator()

        for prime in range(999):
            next(primes_generator)

        next_prime = next(primes_generator)
        self.assertEqual(7919, next_prime)

if __name__ == '__main__':
    unittest.main()