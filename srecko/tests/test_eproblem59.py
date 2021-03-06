from unittest import TestCase
import sys

sys.path.insert(1, '../eproblems')  # Weird this is needed for pipelines to resolve the path.

from eproblem59 import eproblem59
from eproblem59 import all_combos
from eproblem59 import concatenate
from eproblem59 import chr_tuple2int_tuple
from eproblem59 import cipher
from eproblem59 import expand_cipher
from eproblem59 import read_by_chars
from eproblem59 import the_test
from eproblem59 import decrypt_text

lower_case_letters = "abcdefghijklmnopqrstuvwyxz"


class Tep59(TestCase):
    def test_all_combos(self):
        self.assertEqual(
            [('a',), ('b',), ('c',), ('d',), ('e',), ('f',), ('g',), ('h',), ('i',), ('j',), ('k',), ('l',), ('m',),
             ('n',), ('o',), ('p',), ('q',), ('r',), ('s',), ('t',), ('u',), ('v',), ('w',), ('y',), ('x',), ('z',)],
            list(all_combos(1)))

    def test_concatenate(self):
        self.assertEqual("abc", concatenate(['a', 'b', 'c']))

    def test_chr_tuple2int_tuple(self):
        self.assertEqual((97, 98, 99,), chr_tuple2int_tuple(('a', 'b', 'c',)))

    def test_cipher(self):
        self.assertEqual(65, cipher(107, 42))

    def test_expand_cipher(self):
        self.assertEqual([(97, 98, 99), (97, 98, 99)], expand_cipher(('a', 'b', 'c',), 3))

    def test_read_by_chars(self):
        self.assertEqual([(97,), (98,), (99,)], read_by_chars([97, 98, 99], 1))

    def test_decrypt_text(self):
        self.assertEqual("(195, 'AAA')", str(decrypt_text(3, [((107, 107, 107), (42, 42, 42))])))

    def test_the_test(self):
        self.assertEqual(False, the_test(3,[((107, 107, 107), (42, 42, 42))]))
        self.assertEqual(False, the_test(3, [((107, 107, 107), (42, 42, 42)),((107, 107, 107), (42, 42, 42))]))

    def test_eproblem59(self):
        self.assertEqual(": 0", str(eproblem59('../data/t059_cipher.txt', '***', 3)))
        self.assertEqual("***: 642", str(eproblem59('../data/c059_cipher.txt', '***', 3)))
        self.assertEqual("exp: 129448", str(eproblem59('../data/p059_cipher.txt', 'exp', 3)))

    def test_sol59(self):
        self.assertEqual("exp: 129448", str(eproblem59('../data/p059_cipher.txt', '', 3)))
