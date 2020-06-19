import unittest
from EvenFibonacci import calculate_fibonacci as cf, main as EF_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        EF_main()
        sys.stdout = sys.__stdout__
        self.assertIn("4613732",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(cf(10), [1, 2, 3, 5, 8])

    def test_value_errors(self):
        self.assertRaises(ValueError, cf, 1)

    def test_type_errors(self):
        self.assertRaises(TypeError, cf, "Test")
        self.assertRaises(TypeError, cf, 3+5j)

if __name__ == '__main__':
    unittest.main()