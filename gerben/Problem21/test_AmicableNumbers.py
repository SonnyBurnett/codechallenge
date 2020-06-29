import unittest
from AmicableNumbers import sum_of_amicable_numbers, main as AN_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        AN_main()
        sys.stdout = sys.__stdout__
        self.assertIn("31626",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(sum_of_amicable_numbers(6),0)
        self.assertEqual(sum_of_amicable_numbers(500),504)

    def test_value_errors(self):
        self.assertRaises(ValueError, sum_of_amicable_numbers, -1)
        self.assertRaises(ValueError, sum_of_amicable_numbers, 0)

    def test_type_errors(self):
        self.assertRaises(TypeError, sum_of_amicable_numbers, "Test")
        self.assertRaises(TypeError, sum_of_amicable_numbers, 3+5j)
        self.assertRaises(TypeError, sum_of_amicable_numbers, 1,0,1)

if __name__ == '__main__':
    unittest.main()