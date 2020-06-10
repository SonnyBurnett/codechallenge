import unittest
from EvenFibonacci import calculate_fibonacci as cf

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(cf(10), [1, 2, 3, 5, 8])

    def test_value_errors(self):
        self.assertRaises(ValueError, cf, 1)

    def test_type_errors(self):
        self.assertRaises(TypeError, cf, "Test")
        self.assertRaises(TypeError, cf, 3+5j)

if __name__ == '__main__':
    unittest.main()