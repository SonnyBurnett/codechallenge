import unittest
import numpy as numpy
from SumOfMultiples import multiples

class TestFunction(unittest.TestCase):
    def test_function(self):
        self.assertEqual(sum(multiples(10,[3,5])),23)

    def test_value_errors(self):
        self.assertRaises(ValueError, multiples, 1,[1,1])

    def test_type_errors(self):
        self.assertRaises(TypeError, multiples, ("Test",[2,3]))
        self.assertRaises(TypeError, multiples, (10,["Test",1]))

if __name__ == '__main__':
    unittest.main()