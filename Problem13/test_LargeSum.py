import unittest
from LargeSum import calculate_sum, main as LS_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        LS_main()
        sys.stdout = sys.__stdout__
        self.assertIn("5537376230",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(calculate_sum([1,2,3]),6)
        self.assertEqual(calculate_sum([-1,-2,3]),0)

    def test_type_errors(self):
        self.assertRaises(TypeError, calculate_sum, "Test")
        self.assertRaises(TypeError, calculate_sum, 3+5j)
        self.assertRaises(TypeError, calculate_sum, ["Test"])
        #self.assertRaises(TypeError, calculate_sum, [3+5j]) This test passes, isn't that funny?!

if __name__ == '__main__':
    unittest.main()