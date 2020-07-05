import unittest
import solutions.solution59 as testSubject

class solution59TestCase(unittest.TestCase):

    def testPasswordKeyGen(self):
        keygen = testSubject.KeyGen()
        self.assertIsNotNone(keygen)
        self.assertEqual((97, 97, 97), next(keygen))
        self.assertEqual((97, 97, 98), next(keygen))