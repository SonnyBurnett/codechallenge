import unittest
import solutions.solution59 as testSubject

class solution59TestCase(unittest.TestCase):

    def testKeyGen(self):
        keygen = testSubject.keyGen()
        
        self.assertIsNotNone(keygen)
        self.assertEqual((97, 97, 97), next(keygen))
        self.assertEqual((97, 97, 98), next(keygen))

    def testDecrypt(self):
        eulerExamplesXorMessage = [65, 107]
        eulerExamplesXorKey = [42]

        self.assertEqual([107, 65], testSubject.decrypt(eulerExamplesXorMessage, eulerExamplesXorKey))

    def testConvertToAscii(self):
        eulerExamples = [65, 42, 107]
        self.assertEqual(['A', '*', 'k'], testSubject.convertToAscii(eulerExamples))