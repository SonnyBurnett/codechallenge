import unittest
from SumSquareDifference import sum_square_difference

class TestFunction(unittest.TestCase):
    def test_function(self):
        self.assertEqual(sum_square_difference(10),2640)

    def test_value_errors(self):
        self.assertRaises(ValueError, sum_square_difference, 1)
        self.assertRaises(ValueError, sum_square_difference, 251)

    def test_type_errors(self):
        self.assertRaises(TypeError, sum_square_difference, "Test")
        self.assertRaises(TypeError, sum_square_difference, 3+5j)

if __name__ == '__main__':
    unittest.main()