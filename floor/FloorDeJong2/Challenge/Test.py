import unittest

from Challenge import Challenge_54 as ch


class TestHand(unittest.TestCase):

    def test_isFlush_true(self):
        self.assertTrue(ch.is_flush(["2S", "KS", "4S", "6S", "TS"]))

    def test_isFlush_false(self):
        self.assertFalse(ch.is_flush(["2S", "KD", "4S", "6S", "TS"]))

    def test_isStraight_true(self):
        self.assertTrue(ch.is_straight({6: 1, 5: 1, 4: 1, 3: 1, 2: 1}))

    def test_isStraight_false(self):
        self.assertFalse(ch.is_straight({14: 1, 5: 1, 4: 1, 3: 1, 1: 1}))
        self.assertFalse(ch.is_straight({3: 2, 14: 1, 5: 1, 1: 1}))

    def test_replaceLetterCards_validValues(self):
        self.assertEqual(ch.replace_letter_cards("A"), 14)
        self.assertEqual(ch.replace_letter_cards("K"), 13)
        self.assertEqual(ch.replace_letter_cards("Q"), 12)
        self.assertEqual(ch.replace_letter_cards("J"), 11)
        self.assertEqual(ch.replace_letter_cards("T"), 10)
        self.assertEqual(ch.replace_letter_cards("9"), 9)
        self.assertEqual(ch.replace_letter_cards("8"), 8)
        self.assertEqual(ch.replace_letter_cards("7"), 7)
        self.assertEqual(ch.replace_letter_cards("6"), 6)
        self.assertEqual(ch.replace_letter_cards("5"), 5)
        self.assertEqual(ch.replace_letter_cards("4"), 4)
        self.assertEqual(ch.replace_letter_cards("3"), 3)
        self.assertEqual(ch.replace_letter_cards("2"), 2)
        self.assertEqual(ch.replace_letter_cards("1"), 1)

    def test_replaceLetterCards_invalidValue(self):
        card_value = "H"
        with self.assertRaises(SystemExit) as se:
            ch.replace_letter_cards(card_value)

        self.assertEqual(se.exception.args[0], "Card %s does not exists" % card_value)


    # def test_getHighestCar_validAttempt(self):
    #     hand = ch.Hand(["4D", "AC", "7H", "9S", "KD"])
    #     self.assertEqual(hand.get_highest_card(0), 14)
    #     self.assertEqual(hand.get_highest_card(1), 13)
    #     self.assertEqual(hand.get_highest_card(2), 9)
    #     self.assertEqual(hand.get_highest_card(3), 7)
    #     self.assertEqual(hand.get_highest_card(4), 4)
    #
    # def test_getHighestCar_invalidAttempt(self):
    #     hand = ch.Hand(["4D", "AC", "7H", "9S", "KD"])
    #     with self.assertRaises(SystemExit) as se:
    #         hand.get_highest_card(6)
    #
    #     self.assertEqual(se.exception.args[0], "Invalid variable: 1 <= attempts <= 5")

    def test_determineHand_royalFlush(self):
        hand = ch.Hand(["AD", "JD", "TD", "QD", "KD"])
        self.assertEqual(hand.get_hand(), 10)

    def test_determineHand_straightFlush(self):
        hand = ch.Hand(["8D", "JD", "TD", "9D", "7D"])
        self.assertEqual(hand.get_hand(), 9)

    def test_determineHand_fourOfAKind(self):
        hand = ch.Hand(["4D", "4C", "4H", "4S", "KD"])
        self.assertEqual(hand.get_hand(), 8)

    def test_determineHand_fullHouse(self):
        hand = ch.Hand(["4D", "KC", "4H", "4S", "KD"])
        self.assertEqual(hand.get_hand(), 7)

    def test_determineHand_Flush(self):
        hand = ch.Hand(["4D", "JD", "2D", "7D", "KD"])
        self.assertEqual(hand.get_hand(), 6)

    def test_determineHand_straight(self):
        hand = ch.Hand(["8S", "JD", "TH", "9C", "7D"])
        self.assertEqual(hand.get_hand(), 5)

    def test_determineHand_threeOfAKind(self):
        hand = ch.Hand(["4D", "8C", "4H", "4S", "KD"])
        self.assertEqual(hand.get_hand(), 4)

    def test_determineHand_twoPairs(self):
        hand = ch.Hand(["4D", "KC", "4H", "9S", "KD"])
        print(hand.get_hand_value())
        print(hand.get_hand())
        self.assertEqual(hand.get_hand(), 3)

    def test_determineHand_pair(self):
        hand = ch.Hand(["4D", "KC", "2H", "9S", "KD"])
        print(hand.get_hand_value())
        print(hand.get_hand())
        self.assertEqual(hand.get_hand(), 2)

    # def test_determineHand_highCars(self):
    #     hand = ch.Hand(["4D", "AC", "7H", "9S", "KD"])
    #     self.assertEqual(hand.get_hand(), 1)

