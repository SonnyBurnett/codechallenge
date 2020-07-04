import id41   # The code to test
import unittest   # The test framework

class Test_Problem41(unittest.TestCase):
    def test_verify_prime_true(self):
        self.assertTrue(id41.is_prime(2143))

    def test_verify_prime_false(self):
        self.assertFalse(id41.is_prime(4))

    def test_fast_verify_prime_true(self):
        self.assertTrue(id41.fast_prime_verification(2143))

    def test_fast_verify_prime_false(self):
        self.assertFalse(id41.fast_prime_verification(4))
if __name__ == '__main__':
    unittest.main()