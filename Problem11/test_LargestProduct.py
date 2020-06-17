import unittest
from LargestProduct import main as LP_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        LP_main()
        sys.stdout = sys.__stdout__
        self.assertIn("70600674",capturedOutput.getvalue())

if __name__ == '__main__':
    unittest.main()