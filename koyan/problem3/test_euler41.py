import unittest
from euler41 import *


class TestEuler41(unittest.TestCase):
    def test_is_prime(self):
        primes = [3, 31, 619, 1033]
        non_primes = [1, -3, 10, 1000]
        for number in primes:
            self.assertTrue(is_prime(number))
        for number in non_primes:
            self.assertFalse(is_prime(number))

    def test_generate_possible_permutation_keys(self):
        limit9 = generate_possible_permutation_keys(9)
        limit4 = generate_possible_permutation_keys(4)
        self.assertEqual(["987654321", "87654321", "7654321", "654321", "54321", "4321", "321", "21", "1"], limit9)
        self.assertEqual(["4321", "321", "21", "1"], limit4)

    def test_right_answer(self):
        calculated_answer = calculate_pandigital_prime()
        right_answer = 7652413
        self.assertEqual(right_answer, calculated_answer)
