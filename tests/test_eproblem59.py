from unittest import TestCase

from eproblems.eproblem59 import eproblem59
from eproblems.eproblem59 import all_combos
from eproblems.eproblem59 import concatenate
from eproblems.eproblem59 import chr_tuple2int_tuple
from eproblems.eproblem59 import cipher
from eproblems.eproblem59 import expand_cipher
from eproblems.eproblem59 import read_by_chars

lower_case_letters = "abcdefghijklmnopqrstuvwyxz"


class Tep59(TestCase):
    def test_all_combos(self):
        self.assertEqual([('a',),
                          ('b',),
                          ('c',),
                          ('d',),
                          ('e',),
                          ('f',),
                          ('g',),
                          ('h',),
                          ('i',),
                          ('j',),
                          ('k',),
                          ('l',),
                          ('m',),
                          ('n',),
                          ('o',),
                          ('p',),
                          ('q',),
                          ('r',),
                          ('s',),
                          ('t',),
                          ('u',),
                          ('v',),
                          ('w',),
                          ('y',),
                          ('x',),
                          ('z',)]
                         , list(all_combos(1)))

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

    def test_eproblem59(self):
        self.assertEqual(": 0", str(eproblem59('../data/t059_cipher.txt', '***', 3)))
        self.assertEqual("exp: 129448", str(eproblem59('../data/p059_cipher.txt', 'exp', 3)))

    def test_sol59(self):
            self.assertEqual("exp: 129448", str(eproblem59('../data/p059_cipher.txt', '', 3)))
