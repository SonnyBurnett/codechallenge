import unittest
from SundayFirst import countSundays, main as SF_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        SF_main()
        sys.stdout = sys.__stdout__
        self.assertIn("171",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(countSundays(1901,1911),17)

    def test_value_errors(self):
        self.assertRaises(ValueError, countSundays, -1000000,-99999)
        self.assertRaises(ValueError, countSundays, 1,1000000)
        self.assertRaises(ValueError, countSundays, 0,2020)
        self.assertRaises(ValueError, countSundays, 2000,1900)

    def test_type_errors(self):
        self.assertRaises(TypeError, countSundays, 1,"Test")
        self.assertRaises(TypeError, countSundays, 3+5j,2)
        self.assertRaises(TypeError, countSundays, 1,0,1)

if __name__ == '__main__':
    unittest.main()