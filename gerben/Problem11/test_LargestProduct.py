import unittest
from LargestProduct import get_maximum_product, main as LP_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        LP_main()
        sys.stdout = sys.__stdout__
        self.assertIn("70600674",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(get_maximum_product(4),70600674)
        self.assertEqual(get_maximum_product(1),99)
        self.assertEqual(get_maximum_product(20),3392646331113534069313388937216)

    def test_value_errors(self):
        self.assertRaises(ValueError, get_maximum_product, 0)
        self.assertRaises(ValueError, get_maximum_product, 21)

    def test_type_errors(self):
        self.assertRaises(TypeError, get_maximum_product, "Test")
        self.assertRaises(TypeError, get_maximum_product, 3+5j)

if __name__ == '__main__':
    unittest.main()