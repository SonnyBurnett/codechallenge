import unittest
import solutions.solution59 as testSubject

class solution59TestCase(unittest.TestCase):

    def testKeyGen(self):
        keygen = testSubject.keyGen()
        
        self.assertIsNotNone(keygen)
        self.assertEqual((97, 97, 97), next(keygen))
        self.assertEqual((97, 97, 98), next(keygen))

    def testXOR(self):
        eulerExamplesXorMessage = [65, 107]
        eulerExamplesXorKey = [42]

        self.assertEqual([107, 65], testSubject.XOR(eulerExamplesXorMessage, eulerExamplesXorKey))

    def testConvertToAscii(self):
        eulerExamples = [65, 42, 107]
        self.assertEqual(['A', '*', 'k'], testSubject.convertToAscii(eulerExamples))

    def testDecryptMessage(self):
        deGrasseIpsum = """The history of exploration across nations and across time is not one where nations said,
         'Let's explore because it's fun.' It was, 'Let's explore so that we can claim lands for our country,
          so that we can open up new trade routes; let's explore so we can become more powerful.'"""
        converted = [ ord(x) for x in deGrasseIpsum ]
        encypted = testSubject.XOR(converted, (97, 97, 97))
        
        self.assertEqual(deGrasseIpsum, testSubject.decryptMessage(encypted, (97, 97, 97)))