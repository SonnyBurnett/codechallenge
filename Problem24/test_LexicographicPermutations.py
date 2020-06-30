import unittest
from LexicographicPermutations import calculate_xth_permutation, main as LP_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        LP_main()
        sys.stdout = sys.__stdout__
        self.assertIn("2783915460",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(calculate_xth_permutation(5),'0123456978')

    def test_value_errors(self):
        self.assertRaises(ValueError, calculate_xth_permutation, -1)
        self.assertRaises(ValueError, calculate_xth_permutation, 10**8)

    def test_type_errors(self):
        self.assertRaises(TypeError, calculate_xth_permutation, "Test")
        self.assertRaises(TypeError, calculate_xth_permutation, 3+5j)
        self.assertRaises(TypeError, calculate_xth_permutation, 1,0,1)

if __name__ == '__main__':
    unittest.main()