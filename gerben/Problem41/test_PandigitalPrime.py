import unittest
from PandigitalPrime import calculate_pandigital_prime, main as PP_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        PP_main()
        sys.stdout = sys.__stdout__
        self.assertIn("7652413",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(calculate_pandigital_prime(),'7652413')

    def test_type_errors(self):
        self.assertRaises(TypeError, calculate_pandigital_prime, "Test")
        self.assertRaises(TypeError, calculate_pandigital_prime, 3+5j)
        self.assertRaises(TypeError, calculate_pandigital_prime, 1,0,1)

if __name__ == '__main__':
    unittest.main()