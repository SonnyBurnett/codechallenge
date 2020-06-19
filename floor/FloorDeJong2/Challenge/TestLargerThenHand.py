import unittest

from Challenge import Challenge_54 as ch


class TestLargerThenHand(unittest.TestCase):

    def test_largerThenHand_RoyalFlush_straightFlush(self):
        hand1 = ch.Hand(["AD", "JD", "TD", "QD", "KD"])
        hand2 = ch.Hand(["8D", "JD", "TD", "9D", "7D"])

        self.assertTrue(hand1 > hand2)

    def test_largerThenHand_straightFlush_FourOfAKind(self):
        hand1 = ch.Hand(["8D", "JD", "TD", "9D", "7D"])
        hand2 = ch.Hand(["4D", "4C", "4H", "4S", "KD"])

        self.assertTrue(hand1 > hand2)

    def test_largerThenHand_FullHouse_FourOfAKind(self):
        hand1 = ch.Hand(["4D", "4C", "4H", "4S", "KD"])
        hand2 = ch.Hand(["4D", "KC", "4H", "4S", "KD"])

        self.assertTrue(hand1 > hand2)

    def test_largerThenHand_FullHouse_flush(self):
        hand1 = ch.Hand(["4D", "JD", "2D", "7D", "KD"])
        hand2 = ch.Hand(["4D", "KC", "4H", "4S", "KD"])

        self.assertTrue(hand2 > hand1)

    def test_largerThenHand_flush_straight(self):
        hand1 = ch.Hand(["4D", "JD", "2D", "7D", "KD"])
        hand2 = ch.Hand(["8S", "JD", "TH", "9C", "7D"])

        self.assertTrue(hand1 > hand2)

    def test_largerThenHand_threeOfAKind_straight(self):
        hand1 = ch.Hand(["4D", "8C", "4H", "4S", "KD"])
        hand2 = ch.Hand(["8S", "JD", "TH", "9C", "7D"])

        self.assertTrue(hand2 > hand1)

    def test_largerThenHand_threeOfAKind_twoPair(self):
        hand1 = ch.Hand(["4D", "8C", "4H", "4S", "KD"])
        hand2 = ch.Hand(["9S", "JD", "7H", "9C", "7D"])

        self.assertTrue(hand1 > hand2)

    def test_largerThenHand_pair_twoPair(self):
        hand1 = ch.Hand(["4D", "8C", "QH", "4S", "KD"])
        hand2 = ch.Hand(["9S", "JD", "7H", "9C", "7D"])

        self.assertTrue(hand2 > hand1)

    def test_largerThenHand_pair_highCard(self):
        hand1 = ch.Hand(["4D", "8C", "QH", "4S", "KD"])
        hand2 = ch.Hand(["2S", "JD", "7H", "9C", "QD"])

        self.assertTrue(hand2 < hand1)

    def test_largerThenHand_pair_highCard(self):
        hand1 = ch.Hand(["4D", "8C", "QH", "4S", "KD"])
        hand2 = ch.Hand(["2S", "JD", "7H", "9C", "QD"])

        self.assertTrue(hand2 < hand1)

