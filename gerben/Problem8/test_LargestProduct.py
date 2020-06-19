import unittest
from LargestProduct import calculate_max_product, main as LP_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        LP_main()
        sys.stdout = sys.__stdout__
        self.assertIn("23514624000",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(calculate_max_product(4),5832)

    def test_value_errors(self):
        self.assertRaises(ValueError, calculate_max_product, 1)
        self.assertRaises(ValueError, calculate_max_product, 25)

    def test_type_errors(self):
        self.assertRaises(TypeError, calculate_max_product, "Test")
        self.assertRaises(TypeError, calculate_max_product, 3+5j)

if __name__ == '__main__':
    unittest.main()