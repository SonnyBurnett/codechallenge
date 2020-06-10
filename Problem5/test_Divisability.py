import unittest
from Divisability import divisability

class TestFunction(unittest.TestCase):
    def test_function(self):
        self.assertEqual(divisability(5),60)
        self.assertEqual(divisability(10),2520)

    def test_value_errors(self):
        self.assertRaises(ValueError, divisability, 1)
        self.assertRaises(ValueError, divisability, 26)

    def test_type_errors(self):
        self.assertRaises(TypeError, divisability, "Test")
        self.assertRaises(TypeError, divisability, 3+5j)

if __name__ == '__main__':
    unittest.main()