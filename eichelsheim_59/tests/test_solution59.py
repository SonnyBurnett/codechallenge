import unittest
from solution import *


class Test(unittest.TestCase):

    def test_contains_all_words_in_line_of_text(self):
        list_of_words = ['a ', ' the ']
        line_of_text = 'a test is the best'
        self.assertEqual(contains_all_words(list_of_words, line_of_text), True)

    def test_contains_not_all_words_in_line_of_text(self):
        list_of_words = ['a ', ' the ', ' of ']
        line_of_text = 'a test is the best'
        self.assertEqual(contains_all_words(list_of_words, line_of_text), False)

    def test_sum_of_ascii_codes(self):
        line_of_text = 'a test is the best'
        self.assertEqual(sum_of_ascii_codes(line_of_text), 1644)

    def test_sum_of_ascii_codes_incorrect(self):
        line_of_text = 'a test is the bes'
        self.assertNotEqual(sum_of_ascii_codes(line_of_text), 1644)

    def test_decrypt_list(self):
        ascii_code_list = [15, 45, 25, 13, 15, 12]
        key = [98, 97, 95]
        self.assertEqual(decrypt_list_of_ascii_codes(key, ascii_code_list), 'mLFonS')
