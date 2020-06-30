import unittest
from NDigitFibonacci import calculate_first_to_n_fibonacci, main as F2N_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        F2N_main()
        sys.stdout = sys.__stdout__
        self.assertIn("4782",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(calculate_first_to_n_fibonacci(3),12)
        self.assertEqual(calculate_first_to_n_fibonacci(1),0)

    def test_value_errors(self):
        self.assertRaises(ValueError, calculate_first_to_n_fibonacci, -1)
        self.assertRaises(ValueError, calculate_first_to_n_fibonacci, 0)
        self.assertRaises(ValueError, calculate_first_to_n_fibonacci, 10**8)

    def test_type_errors(self):
        self.assertRaises(TypeError, calculate_first_to_n_fibonacci, "Test")
        self.assertRaises(TypeError, calculate_first_to_n_fibonacci, 3+5j)
        self.assertRaises(TypeError, calculate_first_to_n_fibonacci, 1,0,1)

if __name__ == '__main__':
    unittest.main()