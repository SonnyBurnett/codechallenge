import unittest
import sys
import solutions.solution54 as testSubject


class problem54TestCase(unittest.TestCase):

    def setUp(self):
        sys.path.append(".")

    def test_StraightFlush(self):
        hand1 = testSubject.Hand(['AD', 'KD', 'QD', 'JD', 'TD'])
        hand2 = testSubject.Hand(['2D', '3D', '4D', '5D', '9D'])
        self.assertEqual(9, hand1.rank)
        self.assertTrue(hand1 > hand2, "hand1 should win")

    def test_FourOfAKind(self):
        hand1 = testSubject.Hand(['AD', 'AC', 'AH', 'AS', 'KD'])
        hand2 = testSubject.Hand(['QD', 'QC', 'QH', 'QS', 'KD'])
        hand3 = testSubject.Hand(['AD', 'AC', 'AH', 'AS', 'QD'])

        self.assertEqual(8, hand1.rank)
        self.assertTrue(hand1 > hand2, "hand1 should win")
        self.assertTrue(hand1 > hand3, "hand1 should win")

    def test_FullHouse(self):
        hand1 = testSubject.Hand(['AD', 'AC', 'AH', 'KD', 'KC'])
        hand2 = testSubject.Hand(['QD', 'QC', 'QH', 'KD', 'KC'])
        hand3 = testSubject.Hand(['AD', 'AC', 'AH', 'QD', 'QC'])

        self.assertEqual(7, hand1.rank)
        self.assertTrue(hand1 > hand2, "hand1 should win")
        self.assertTrue(hand1 > hand3, "hand1 should win")

    def test_Flush(self):
        hand1 = testSubject.Hand(['AD', 'KD', 'QD', 'JD', '2D'])
        hand2 = testSubject.Hand(['3D', 'KD', 'QD', 'JD', '2D'])
        self.assertEqual(6, hand1.rank)
        self.assertTrue(hand1 > hand2, "hand1 should win")

    def test_Straight(self):
        hand1 = testSubject.Hand(['TC', '9C', '8C', '7C', '6H'])
        hand2 = testSubject.Hand(['2C', '3C', '4C', '5C', '6H'])
        self.assertEqual(5, hand1.rank)
        self.assertTrue(hand1 > hand2, "hand1 should win")

    def test_ThreeOfAKind(self):
        hand1 = testSubject.Hand(['AD', 'AC', 'AH', 'KD', 'QD'])
        hand2 = testSubject.Hand(['2D', '2C', '2H', 'KD', 'QD'])
        hand3 = testSubject.Hand(['AD', 'AC', 'AH', '2D', '3D'])
        self.assertEqual(4, hand1.rank)
        self.assertTrue(hand1 > hand2, "hand1 should win")
        self.assertTrue(hand1 > hand3, "hand1 should win")

    def test_TwoPair(self):
        hand1 = testSubject.Hand(['AD', 'AC', 'KD', 'KC', '2H'])
        hand2 = testSubject.Hand(['QD', 'QC', 'JD', 'JC', '2H'])
        self.assertEqual(3, hand1.rank)
        self.assertTrue(hand1 > hand2, "hand1 should win")

        hand3 = testSubject.Hand(['3D', '3C', 'AD', 'AC', '2H'])
        hand4 = testSubject.Hand(['4H', '4S', 'KD', 'KC', '2H'])
        self.assertTrue(hand3 > hand4, "hand3 should win")

        hand5 = testSubject.Hand(['AD', 'AC', 'KD', 'KC', '3H'])
        hand6 = testSubject.Hand(['AH', 'AS', 'KH', 'KS', '2H'])
        self.assertTrue(hand5 > hand6, "hand5 should win")

    def test_OnePair(self):
        hand1 = testSubject.Hand(['AD', 'AC', 'KD', 'QD', 'TD'])
        hand2 = testSubject.Hand(['2D', '2C', 'KD', 'QD', 'TD'])
        hand3 = testSubject.Hand(['AH', 'AS', '2D', '3D', '4D'])
        self.assertEqual(2, hand1.rank)
        self.assertTrue(hand1 > hand2, "hand1 should win")
        self.assertTrue(hand1 > hand3, "hand1 should win")

    def test_HighCard(self):
        hand1 = testSubject.Hand(['AD', 'KC', 'QH', 'JC', '2D'])
        hand2 = testSubject.Hand(['3D', 'KC', 'QH', 'JC', '2D'])
        self.assertEqual(1, hand1.rank)
        self.assertTrue(hand1 > hand2, "hand1 should win")

        hand3 = testSubject.Hand(['2D', 'JC', 'QH', 'KC', 'AD'])
        self.assertTrue(hand3 > hand2, "hand3 should win")

    def test_EulerExample(self):
        with open('resources/example54.txt') as f:
            self.assertEqual(3, testSubject.compareHands(f))

    def test_EulerOfficial(self):
        with open('resources/poker.txt') as f:
            self.assertEqual(376, testSubject.compareHands(f))
