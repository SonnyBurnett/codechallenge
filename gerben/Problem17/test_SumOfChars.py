import unittest
from SumOfChars import count_alphabetic_chars_in_numbers, main as SOC_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        SOC_main()
        sys.stdout = sys.__stdout__
        self.assertIn("21124",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(count_alphabetic_chars_in_numbers(2,4),8)
        self.assertEqual(count_alphabetic_chars_in_numbers(101,102),16)

    def test_value_errors(self):
        self.assertRaises(ValueError, count_alphabetic_chars_in_numbers, -1000000,-99999)
        self.assertRaises(ValueError, count_alphabetic_chars_in_numbers, 99999,1000000)
        self.assertRaises(ValueError, count_alphabetic_chars_in_numbers, 1,0)

    def test_type_errors(self):
        self.assertRaises(TypeError, count_alphabetic_chars_in_numbers, 1,"Test")
        self.assertRaises(TypeError, count_alphabetic_chars_in_numbers, 3+5j,2)
        self.assertRaises(TypeError, count_alphabetic_chars_in_numbers, 1,0,1)

if __name__ == '__main__':
    unittest.main()