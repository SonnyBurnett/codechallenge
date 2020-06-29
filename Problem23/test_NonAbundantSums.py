import unittest
from NonAbundantSums import main as NAS_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        NAS_main()
        sys.stdout = sys.__stdout__
        self.assertIn("4179871",capturedOutput.getvalue())

if __name__ == '__main__':
    unittest.main()