from unittest import TestCase

from eproblems.eproblem59 import eproblem59


class Tep59(TestCase):
    def test_eproblem59(self):
        self.assertEqual(": 0", str(eproblem59('../data/t059_cipher.txt', '***', 3)))
        self.assertEqual(str(['e', 'x', 'p']) + ": 129448", str(eproblem59('../data/p059_cipher.txt', 'exp', 3)))

    def test_sol59(self):
        self.assertEqual(str(['e', 'x', 'p']) + ": 129448", str(eproblem59('../data/p059_cipher.txt', '', 3)))
