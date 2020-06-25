from unittest import TestCase

from eproblems.eproblem59 import eproblem59


class Tep59(TestCase):
    def test_eproblem59(self):
        self.assertEqual('', str(eproblem59('../data/t059_cipher.txt', '***')))

    def test_sol59(self):
        self.assertEqual(str(['e', 'x', 'p']), str(eproblem59('../data/p059_cipher.txt', 'exp')))
