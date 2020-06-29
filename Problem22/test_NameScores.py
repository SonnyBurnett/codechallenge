import unittest
from NameScores import wordvalue, main as NS_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        NS_main()
        sys.stdout = sys.__stdout__
        self.assertIn("871198282",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(wordvalue("COLIN"),53)

    def test_type_errors(self):
        self.assertRaises(TypeError, wordvalue, 1,"Test")
        self.assertRaises(TypeError, wordvalue, 3+5j)
        self.assertRaises(TypeError, wordvalue, 1)

if __name__ == '__main__':
    unittest.main()