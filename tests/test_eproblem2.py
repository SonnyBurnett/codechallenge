from unittest import TestCase

from eproblems.eproblem2 import flip_mod3
from eproblems.eproblem2 import sum_fibo_div3
from eproblems.eproblem2 import eproblem2


class Tep2(TestCase):
    def test_flip_mod3(self):
        self.assertEqual(flip_mod3(0), 2)
        self.assertEqual(flip_mod3(1), 1)
        self.assertEqual(flip_mod3(2), 0)

    def test_sum_fibo_div3(self):
        self.assertEqual(sum_fibo_div3(143), 89)
        self.assertEqual(sum_fibo_div3(144), 377)
        self.assertEqual(sum_fibo_div3(145), 377)

    def test_eproblem2(self):
        self.assertEqual(eproblem2(89), 44)
        self.assertEqual(eproblem2(144), 188)
        self.assertEqual(eproblem2(250), 188)
        self.assertEqual(eproblem2(377), 188)
        self.assertEqual(eproblem2(610), 798)
        self.assertEqual(eproblem2(1000), 798)

    def test_sol2(self):
        self.assertEqual(eproblem2(4000000), 4613732)
