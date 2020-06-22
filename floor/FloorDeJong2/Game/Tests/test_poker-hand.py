import unittest
import Game.PokerGame.pokerhand as ph


class TestPokerHand(unittest.TestCase):

    def test_isFlush_true(self):
        self.assertTrue(ph.is_flush(["2S", "KS", "4S", "6S", "TS"]))

    def test_isFlush_false(self):
        self.assertFalse(ph.is_flush(["2S", "KD", "4S", "6S", "TS"]))

    def test_isStraight_true(self):
        self.assertTrue(ph.is_straight({6: 1, 5: 1, 4: 1, 3: 1, 2: 1}))

    def test_isStraight_false(self):
        self.assertFalse(ph.is_straight({14: 1, 5: 1, 4: 1, 3: 1, 1: 1}))
        self.assertFalse(ph.is_straight({3: 2, 14: 1, 5: 1, 1: 1}))

    def test_replaceLetterCards_validValues(self):
        self.assertEqual(ph.replace_letter_cards("A"), 14)
        self.assertEqual(ph.replace_letter_cards("K"), 13)
        self.assertEqual(ph.replace_letter_cards("Q"), 12)
        self.assertEqual(ph.replace_letter_cards("J"), 11)
        self.assertEqual(ph.replace_letter_cards("T"), 10)
        self.assertEqual(ph.replace_letter_cards("9"), 9)
        self.assertEqual(ph.replace_letter_cards("8"), 8)
        self.assertEqual(ph.replace_letter_cards("7"), 7)
        self.assertEqual(ph.replace_letter_cards("6"), 6)
        self.assertEqual(ph.replace_letter_cards("5"), 5)
        self.assertEqual(ph.replace_letter_cards("4"), 4)
        self.assertEqual(ph.replace_letter_cards("3"), 3)
        self.assertEqual(ph.replace_letter_cards("2"), 2)
        self.assertEqual(ph.replace_letter_cards("1"), 1)

    def test_replaceLetterCards_invalidValue(self):
        card_value = "H"
        with self.assertRaises(SystemExit) as se:
            ph.replace_letter_cards(card_value)

        self.assertEqual(se.exception.args[0], "Card %s does not exists" % card_value)

    def test_determineHand_royalFlush(self):
        hand = ph.PokerHand(["AD", "JD", "TD", "QD", "KD"])
        self.assertEqual(hand.get_hand(), 10)

    def test_determineHand_straightFlush(self):
        hand = ph.PokerHand(["8D", "JD", "TD", "9D", "7D"])
        self.assertEqual(hand.get_hand(), 9)

    def test_determineHand_fourOfAKind(self):
        hand = ph.PokerHand(["4D", "4C", "4H", "4S", "KD"])
        self.assertEqual(hand.get_hand(), 8)

    def test_determineHand_fullHouse(self):
        hand = ph.PokerHand(["4D", "KC", "4H", "4S", "KD"])
        self.assertEqual(hand.get_hand(), 7)

    def test_determineHand_Flush(self):
        hand = ph.PokerHand(["4D", "JD", "2D", "7D", "KD"])
        self.assertEqual(hand.get_hand(), 6)

    def test_determineHand_straight(self):
        hand = ph.PokerHand(["8S", "JD", "TH", "9C", "7D"])
        self.assertEqual(hand.get_hand(), 5)

    def test_determineHand_threeOfAKind(self):
        hand = ph.PokerHand(["4D", "8C", "4H", "4S", "KD"])
        self.assertEqual(hand.get_hand(), 4)

    def test_determineHand_twoPairs(self):
        hand = ph.PokerHand(["4D", "KC", "4H", "9S", "KD"])
        self.assertEqual(hand.get_hand(), 3)

    def test_determineHand_pair(self):
        hand = ph.PokerHand(["4D", "KC", "2H", "9S", "KD"])
        self.assertEqual(hand.get_hand(), 2)

    def test_determineHand_highCars(self):
        hand = ph.PokerHand(["4D", "AC", "7H", "9S", "KD"])
        self.assertEqual(hand.get_hand(), 1)

    def test_largerThenHand_RoyalFlush_straightFlush(self):
        hand1 = ph.PokerHand(["AD", "JD", "TD", "QD", "KD"])
        hand2 = ph.PokerHand(["8D", "JD", "TD", "9D", "7D"])

        self.assertTrue(hand1 > hand2)

    def test_largerThenHand_straightFlush_FourOfAKind(self):
        hand1 = ph.PokerHand(["8D", "JD", "TD", "9D", "7D"])
        hand2 = ph.PokerHand(["4D", "4C", "4H", "4S", "KD"])

        self.assertTrue(hand1 > hand2)

    def test_largerThenHand_FullHouse_FourOfAKind(self):
        hand1 = ph.PokerHand(["4D", "4C", "4H", "4S", "KD"])
        hand2 = ph.PokerHand(["4D", "KC", "4H", "4S", "KD"])

        self.assertTrue(hand1 > hand2)

    def test_largerThenHand_FullHouse_flush(self):
        hand1 = ph.PokerHand(["4D", "JD", "2D", "7D", "KD"])
        hand2 = ph.PokerHand(["4D", "KC", "4H", "4S", "KD"])

        self.assertTrue(hand2 > hand1)

    def test_largerThenHand_flush_straight(self):
        hand1 = ph.PokerHand(["4D", "JD", "2D", "7D", "KD"])
        hand2 = ph.PokerHand(["8S", "JD", "TH", "9C", "7D"])

        self.assertTrue(hand1 > hand2)

    def test_largerThenHand_threeOfAKind_straight(self):
        hand1 = ph.PokerHand(["4D", "8C", "4H", "4S", "KD"])
        hand2 = ph.PokerHand(["8S", "JD", "TH", "9C", "7D"])

        self.assertTrue(hand2 > hand1)

    def test_largerThenHand_threeOfAKind_twoPair(self):
        hand1 = ph.PokerHand(["4D", "8C", "4H", "4S", "KD"])
        hand2 = ph.PokerHand(["9S", "JD", "7H", "9C", "7D"])

        self.assertTrue(hand1 > hand2)

    def test_largerThenHand_pair_twoPair(self):
        hand1 = ph.PokerHand(["4D", "8C", "QH", "4S", "KD"])
        hand2 = ph.PokerHand(["9S", "JD", "7H", "9C", "7D"])

        self.assertTrue(hand2 > hand1)

    def test_largerThenHand_pair_highCard(self):
        hand1 = ph.PokerHand(["4D", "8C", "QH", "4S", "KD"])
        hand2 = ph.PokerHand(["2S", "JD", "7H", "9C", "QD"])

        self.assertTrue(hand2 < hand1)

    def test_largerThenHand_highCard_highCard(self):
        hand1 = ph.PokerHand(["4D", "8C", "QH", "9S", "KD"])
        hand2 = ph.PokerHand(["3D", "8C", "QH", "9S", "KD"])
        self.assertTrue(hand1 > hand2)

        hand1 = ph.PokerHand(["4D", "8C", "QH", "9S", "KD"])
        hand2 = ph.PokerHand(["5D", "8C", "QH", "9S", "KD"])
        self.assertFalse(hand1 > hand2)

        hand1 = ph.PokerHand(["4D", "8C", "QH", "9S", "KD"])
        hand2 = ph.PokerHand(["3D", "8C", "QH", "9S", "TD"])
        self.assertTrue(hand1 > hand2)

        hand1 = ph.PokerHand(["4D", "8C", "QH", "9S", "KD"])
        hand2 = ph.PokerHand(["3D", "8C", "QH", "9S", "AD"])
        self.assertFalse(hand1 > hand2)
