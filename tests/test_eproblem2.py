from unittest import TestCase

from eproblems.eproblem2 import sum_fibo_div3
from eproblems.eproblem2 import eproblem2


class Tep2(TestCase):
    def test_sum_fibo_div3(self):
        self.assertEqual(sum_fibo_div3(143), 89)
        self.assertEqual(sum_fibo_div3(144), 377)
        self.assertEqual(sum_fibo_div3(145), 377)

    def test_eproblem2(self):
        self.assertEqual(eproblem2(0), 0)
        self.assertEqual(eproblem2(1), 0)
        self.assertEqual(eproblem2(2), 2)
        self.assertEqual(eproblem2(3), 2)
        self.assertEqual(eproblem2(4), 2)
        self.assertEqual(eproblem2(5), 2)
        self.assertEqual(eproblem2(6), 2)
        self.assertEqual(eproblem2(7), 2)
        self.assertEqual(eproblem2(8), 10)
        self.assertEqual(eproblem2(9), 10)
        self.assertEqual(eproblem2(35), 44)
        self.assertEqual(eproblem2(143), 44)
        self.assertEqual(eproblem2(144), 188)
        self.assertEqual(eproblem2(145), 188)
        self.assertEqual(eproblem2(250), 188)
        self.assertEqual(eproblem2(232), 188)
        self.assertEqual(eproblem2(233), 188)
        self.assertEqual(eproblem2(234), 188)
        self.assertEqual(eproblem2(376), 188)
        self.assertEqual(eproblem2(377), 188)
        self.assertEqual(eproblem2(378), 188)
        self.assertEqual(eproblem2(609), 188)
        self.assertEqual(eproblem2(610), 798)
        self.assertEqual(eproblem2(1000), 798)

    def test_sol2(self):
        self.assertEqual(eproblem2(4000000), 4613732)
