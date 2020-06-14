import unittest
from PythogareanTriplets import SpecialTriplet

class TestFunction(unittest.TestCase):
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