import unittest
from PalindromeNumbers import highest_palindrome, main as PN_main
from io import StringIO
import sys

class TestFunction(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        PN_main()
        sys.stdout = sys.__stdout__
        self.assertIn("906609",capturedOutput.getvalue())

    def test_function(self):
        self.assertEqual(highest_palindrome(2),9009)
        self.assertEqual(highest_palindrome(3),906609)

    def test_value_errors(self):
        self.assertRaises(ValueError, highest_palindrome, 1)
        self.assertRaises(ValueError, highest_palindrome, 6)

    def test_type_errors(self):
        self.assertRaises(TypeError, highest_palindrome, "Test")
        self.assertRaises(TypeError, highest_palindrome, 3+5j)

if __name__ == '__main__':
    unittest.main()