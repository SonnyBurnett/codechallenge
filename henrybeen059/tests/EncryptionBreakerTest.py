import sys
import unittest

sys.path.append('../')
from classes.EncryptionBreaker import EncryptionBreaker


class EncryptionBreakerTest(unittest.TestCase):
    def test_problem(self):
        encryption_breaker = EncryptionBreaker('../euler059.txt')
        solution = encryption_breaker.run()

        self.assertEqual('101,120,112', solution.get_key())

    def test_hii(self):
        encryption_breaker = EncryptionBreaker('../test_hii.txt')
        solution = encryption_breaker.run()

        self.assertEqual('104,105,105', solution.get_key())


if __name__ == '__main__':
    unittest.main()
