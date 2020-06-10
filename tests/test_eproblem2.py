from unittest import TestCase

from eproblems.eproblem2 import sum_fibo


class Tep2(TestCase):
    def test_sum_fibo(self):
        self.assertEqual(sum_fibo(1, 0), 2)
        self.assertEqual(sum_fibo(1, 1), 2)
        self.assertEqual(sum_fibo(1, 2), 3)
        self.assertEqual(sum_fibo(144, 2), 377)
