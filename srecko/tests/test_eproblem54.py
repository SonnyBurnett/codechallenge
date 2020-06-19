from unittest import TestCase
from collections import Counter

from eproblems.eproblem54 import get_list_id
from eproblems.eproblem54 import get_sublist_id
from eproblems.eproblem54 import sequence
from eproblems.eproblem54 import ranked_as
from eproblems.eproblem54 import eproblem54
from eproblems.eproblem54 import is_subranked


class Tep52(TestCase):
    def test_eproblem54(self):
        self.assertEqual(eproblem54('../data/z054_poker.txt'), 1)
        self.assertEqual(eproblem54('../data/t054_poker.txt'), 3)
        self.assertEqual(eproblem54('../data/c054_poker.txt'), 3)
        self.assertEqual(eproblem54('../data/e054_poker.txt'), 2)

    def test_ranked_as(self):
        self.assertEqual(ranked_as(Counter({3: 1, 2: 1, 4: 1, 5: 1, 6: 1}), Counter({'S': 3, 'D': 2})),
                         ((5, [6]), [6, 5, 4, 3, 2]))

    def test_get_list_id(self):
        self.assertEqual(get_list_id('NONE'), 0)

    def test_get_sublist_id(self):
        self.assertEqual(get_sublist_id('High Card'), 1)

    def test_sequence(self):
        self.assertEqual(sequence([1, 2, 3, 4, 5, 7, 6]), True)

    def test_is_subranked(self):
        self.assertEqual(is_subranked((1, 1, 1, 1, 1)), True)
        self.assertEqual(is_subranked((3, 2)), False)

    def test_sol54(self):
        self.assertEqual(eproblem54('../data/p054_poker.txt'), 376)