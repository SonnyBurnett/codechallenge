import unittest
from ReciprocalCycles import longest_reciprocal_cycle, main as RC_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        RC_main()
        sys.stdout = sys.__stdout__
        self.assertIn("983",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(longest_reciprocal_cycle(10),7)
        self.assertEqual(longest_reciprocal_cycle(100),97)

    def test_value_errors(self):
        self.assertRaises(ValueError, longest_reciprocal_cycle, -1)
        self.assertRaises(ValueError, longest_reciprocal_cycle, 0)
        self.assertRaises(ValueError, longest_reciprocal_cycle, 10000)

    def test_type_errors(self):
        self.assertRaises(TypeError, longest_reciprocal_cycle, "Test")
        self.assertRaises(TypeError, longest_reciprocal_cycle, 3+5j)
        self.assertRaises(TypeError, longest_reciprocal_cycle, 1,0,1)

if __name__ == '__main__':
    unittest.main()