import unittest
from PythagoreanTriplets import SpecialTriplet, main as PT_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        PT_main()
        sys.stdout = sys.__stdout__
        self.assertIn("31875000",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(SpecialTriplet(1000),[200, 375, 425])
        self.assertEqual(SpecialTriplet(1),[])

    def test_value_errors(self):
        self.assertRaises(ValueError, SpecialTriplet, 0)
        self.assertRaises(ValueError, SpecialTriplet, 10001)

    def test_type_errors(self):
        self.assertRaises(TypeError, SpecialTriplet, "Test")
        self.assertRaises(TypeError, SpecialTriplet, 3+5j)

if __name__ == '__main__':
    unittest.main()