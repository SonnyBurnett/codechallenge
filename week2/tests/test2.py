import unittest
import solutions.solution2 as testSubject


class problem2TestCase(unittest.TestCase):

    def test_EulerExample(self):
        self.assertEqual(44, testSubject.sumEvenFibonacci(100))

    def test_EulerOfficial(self):
        self.assertEqual(4613732, testSubject.sumEvenFibonacci(4000000))
