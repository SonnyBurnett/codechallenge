import unittest
from PrimeCalculator import calculate_primes

class TestFunction(unittest.TestCase):
    def test_function(self):
        self.assertEqual(calculate_primes(6),13)

    def test_value_errors(self):
        self.assertRaises(ValueError, calculate_primes, 1)
        self.assertRaises(ValueError, calculate_primes, 100001)

    def test_type_errors(self):
        self.assertRaises(TypeError, calculate_primes, "Test")
        self.assertRaises(TypeError, calculate_primes, 3+5j)

if __name__ == '__main__':
    unittest.main()