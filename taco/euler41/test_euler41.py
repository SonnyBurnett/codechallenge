import unittest

from euler41 import make_string_from_digits
from euler41 import make_num_from_list
from euler41 import get_prime_permutations
from euler41 import get_max_num_from_list


class MyTestCase(unittest.TestCase):
    def test_string(self):
        self.assertEqual(make_string_from_digits(2), "12")
        self.assertEqual(make_string_from_digits(3), "123")
        self.assertEqual(make_string_from_digits(4), "1234")
        self.assertEqual(make_string_from_digits(9), "123456789")

    def test_make_num(self):
        self.assertEqual(make_num_from_list([1, 2]), 12)
        self.assertEqual(make_num_from_list([8, 9, 3, 2, 5, 1]), 893251)

    def test_prime_mutations(self):
        self.assertEqual(get_prime_permutations("1234"), [1423, 2143, 2341, 4231])

    def test_max_num(self):
        self.assertEqual(get_max_num_from_list([1, 3, 9, 44, 22, 1, 44]), 44)
        self.assertEqual(get_max_num_from_list([1, 0, 1, 53627]), 53627)
        self.assertEqual(get_max_num_from_list([-1, -3, -9, -44, -22, -1, -44]), -1)

    def test_nested_functions(self):
        self.assertEqual(get_prime_permutations(make_string_from_digits(4)),[1423, 2143, 2341, 4231])
        self.assertEqual(max(get_max_num_from_list([get_prime_permutations(make_string_from_digits(q)) for q in range(2, 10)])), 7652413)


if __name__ == '__main__':
    unittest.main()
