import unittest

import Euler4


class TestEuler4(unittest.TestCase):

    def test_isIntegerPalindrome(self):
        self.assertTrue(Euler4.is_integer_palindrome(9009))
        self.assertTrue(Euler4.is_integer_palindrome(123454321))
        self.assertFalse(Euler4.is_integer_palindrome(123456789))

    def test_findLargestPalindrome(self):
        self.assertEqual(Euler4.find_largest_palindrome(2), 9009)
