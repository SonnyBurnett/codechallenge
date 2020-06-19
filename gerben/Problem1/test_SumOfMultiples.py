import unittest
from SumOfMultiples import multiples, main as SOM_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        SOM_main()
        sys.stdout = sys.__stdout__
        self.assertIn("233168",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(sum(multiples(10,[3,5])),23)
        self.assertEqual(sum(multiples(10,[3,5,2])),37)

    def test_value_errors(self):
        self.assertRaises(ValueError, multiples, 1,[1,1])

    def test_type_errors(self):
        self.assertRaises(TypeError, multiples, ("Test",[2,3]))
        self.assertRaises(TypeError, multiples, (10,["Test",1]))

if __name__ == '__main__':
    unittest.main()