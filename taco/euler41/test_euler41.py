import unittest

from euler41 import make_string_from_digits
from euler41 import get_max_prime_from_permutations


class MyTestCase(unittest.TestCase):
    def test_string(self):
        self.assertEqual(make_string_from_digits(2), "12")
        self.assertEqual(make_string_from_digits(3), "123")
        self.assertEqual(make_string_from_digits(4), "1234")
        self.assertEqual(make_string_from_digits(9), "123456789")

    def test_prime_mutations(self):
        self.assertEqual(get_max_prime_from_permutations("1234"), 4231)


if __name__ == '__main__':
    unittest.main()

