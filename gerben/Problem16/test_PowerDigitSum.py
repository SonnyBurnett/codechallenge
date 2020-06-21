import unittest
from PowerDigitSum import calculate_digit_sum, main as PDS_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        PDS_main()
        sys.stdout = sys.__stdout__
        self.assertIn("1366",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(calculate_digit_sum(2),2)
        self.assertEqual(calculate_digit_sum(35),8)

    def test_value_errors(self):
        self.assertRaises(ValueError, calculate_digit_sum, -1)
        self.assertRaises(ValueError, calculate_digit_sum, 0)

    def test_type_errors(self):
        self.assertRaises(TypeError, calculate_digit_sum, "Test")
        self.assertRaises(TypeError, calculate_digit_sum, 3+5j)
        self.assertRaises(TypeError, calculate_digit_sum, 1,0,1)

if __name__ == '__main__':
    unittest.main()