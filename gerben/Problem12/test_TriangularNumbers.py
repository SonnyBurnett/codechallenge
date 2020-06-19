import unittest
from TriangularNumbers import triangular_exceeding_divisors, main as TN_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        TN_main()
        sys.stdout = sys.__stdout__
        self.assertIn("76576500",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(triangular_exceeding_divisors(5),28)

    def test_value_errors(self):
        self.assertRaises(ValueError, triangular_exceeding_divisors, 0)
        self.assertRaises(ValueError, triangular_exceeding_divisors, 750)

    def test_type_errors(self):
        self.assertRaises(TypeError, triangular_exceeding_divisors, "Test")
        self.assertRaises(TypeError, triangular_exceeding_divisors, 3+5j)

if __name__ == '__main__':
    unittest.main()