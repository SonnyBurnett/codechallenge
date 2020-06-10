import unittest
from PalindromeNumbers import highest_palindrome

class TestFunction(unittest.TestCase):
    def test_function(self):
        self.assertEqual(highest_palindrome(2),9009)
        self.assertEqual(highest_palindrome(3),906609)

    def test_value_errors(self):
        self.assertRaises(ValueError, highest_palindrome, 1)
        self.assertRaises(ValueError, highest_palindrome, 10)

    def test_type_errors(self):
        self.assertRaises(TypeError, highest_palindrome, "Test")
        self.assertRaises(TypeError, highest_palindrome, 3+5j)

if __name__ == '__main__':
    unittest.main()