import unittest
from LongestCollatzSequence import calculate_longest_sequence, main as LCS_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        LCS_main()
        sys.stdout = sys.__stdout__
        self.assertIn("837799",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(calculate_longest_sequence(14),9)
        self.assertEqual(calculate_longest_sequence(1000),871)

    def test_value_errors(self):
        self.assertRaises(ValueError, calculate_longest_sequence, 1)
        self.assertRaises(ValueError, calculate_longest_sequence, 10000000)

    def test_type_errors(self):
        self.assertRaises(TypeError, calculate_longest_sequence, "Test")
        self.assertRaises(TypeError, calculate_longest_sequence, 3+5j)

if __name__ == '__main__':
    unittest.main()