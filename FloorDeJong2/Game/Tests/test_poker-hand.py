import unittest
import Game.PokerGame.pokerhand as pk


class TestPokerHand(unittest.TestCase):

    def test_isFlush_true(self):
        self.assertTrue(pk.is_flush(["2S", "KS", "4S", "6S", "TS"]))

    def test_isFlush_false(self):
        self.assertFalse(pk.is_flush(["2S", "KD", "4S", "6S", "TS"]))

    def test_isStraight_true(self):
        self.assertTrue(pk.is_straight([3, 6, 5, 2, 4]))

    def test_isStraight_false(self):
        self.assertFalse(pk.is_straight([3, 14, 5, 1, 4]))

    def test_replaceLetterCards_validValues(self):
        self.assertEqual(pk.replace_letter_cards("A"), 14)
        self.assertEqual(pk.replace_letter_cards("K"), 13)
        self.assertEqual(pk.replace_letter_cards("Q"), 12)
        self.assertEqual(pk.replace_letter_cards("J"), 11)
        self.assertEqual(pk.replace_letter_cards("T"), 10)
        self.assertEqual(pk.replace_letter_cards("9"), 9)
        self.assertEqual(pk.replace_letter_cards("8"), 8)
        self.assertEqual(pk.replace_letter_cards("7"), 7)
        self.assertEqual(pk.replace_letter_cards("6"), 6)
        self.assertEqual(pk.replace_letter_cards("5"), 5)
        self.assertEqual(pk.replace_letter_cards("4"), 4)
        self.assertEqual(pk.replace_letter_cards("3"), 3)
        self.assertEqual(pk.replace_letter_cards("2"), 2)
        self.assertEqual(pk.replace_letter_cards("1"), 1)

    def test_replaceLetterCards_invalidValue(self):
        card_value = "H"
        with self.assertRaises(SystemExit) as se:
            pk.replace_letter_cards(card_value)

        self.assertEqual(se.exception.args[0], "Card %s does not exists" % card_value)

    def test_getNrCardsPerValue(self):
        self.assertDictEqual(pk.get_nr_cards_per_value(["2D", "6S", "4D", "6H", "6C"]), {2: 1, 6: 3, 4: 1})

    def test_findKeyWithValue(self):
        self.assertCountEqual(pk.find_key_with_value({4: 2, 11: 1, 5: 2}, 2), [4, 5])
        self.assertCountEqual(pk.find_key_with_value({4: 2, 11: 1, 5: 2}, 1), [11])

    def test_getHighestCar_validAttempt(self):
        hand = pk.PokerHand(["4D", "AC", "7H", "9S", "KD"])
        self.assertEqual(hand.get_highest_card(1), 14)
        self.assertEqual(hand.get_highest_card(2), 13)
        self.assertEqual(hand.get_highest_card(3), 9)
        self.assertEqual(hand.get_highest_card(4), 7)
        self.assertEqual(hand.get_highest_card(5), 4)

    def test_getHighestCar_invalidAttempt(self):
        hand = pk.PokerHand(["4D", "AC", "7H", "9S", "KD"])
        with self.assertRaises(SystemExit) as se:
            hand.get_highest_card(6)

        self.assertEqual(se.exception.args[0], "Invalid variable: 1 <= attempts <= 5")

    def test_determineHand_royalFlush(self):
        hand = pk.PokerHand(["AD", "JD", "TD", "QD", "KD"])
        self.assertEqual(hand.get_hand(), 10)
        self.assertFalse(hand.get_hand_value())

    def test_determineHand_straightFlush(self):
        hand = pk.PokerHand(["8D", "JD", "TD", "9D", "7D"])
        self.assertEqual(hand.get_hand(), 9)
        self.assertFalse(hand.get_hand_value())

    def test_determineHand_fourOfAKind(self):
        hand = pk.PokerHand(["4D", "4C", "4H", "4S", "KD"])
        self.assertEqual(hand.get_hand(), 8)
        self.assertEqual(hand.get_hand_value(), [4])

    def test_determineHand_fullHouse(self):
        hand = pk.PokerHand(["4D", "KC", "4H", "4S", "KD"])
        self.assertEqual(hand.get_hand(), 7)
        self.assertEqual(hand.get_hand_value(), [4])

    def test_determineHand_Flush(self):
        hand = pk.PokerHand(["4D", "JD", "2D", "7D", "KD"])
        self.assertEqual(hand.get_hand(), 6)
        self.assertFalse(hand.get_hand_value())

    def test_determineHand_straight(self):
        hand = pk.PokerHand(["8S", "JD", "TH", "9C", "7D"])
        self.assertEqual(hand.get_hand(), 5)
        self.assertFalse(hand.get_hand_value())

    def test_determineHand_threeOfAKind(self):
        hand = pk.PokerHand(["4D", "8C", "4H", "4S", "KD"])
        self.assertEqual(hand.get_hand(), 4)
        self.assertEqual(hand.get_hand_value(), [4])

    def test_determineHand_twoPairs(self):
        hand = pk.PokerHand(["4D", "KC", "4H", "9S", "KD"])
        self.assertEqual(hand.get_hand(), 3)
        self.assertEqual(hand.get_hand_value(), [13, 4])

    def test_determineHand_pair(self):
        hand = pk.PokerHand(["4D", "KC", "2H", "9S", "KD"])
        self.assertEqual(hand.get_hand(), 2)
        self.assertEqual(hand.get_hand_value(), [13])

    def test_determineHand_highCars(self):
        hand = pk.PokerHand(["4D", "AC", "7H", "9S", "KD"])
        self.assertEqual(hand.get_hand(), 1)
        self.assertFalse(hand.get_hand_value())

    def test_largerThenHand_RoyalFlush_straightFlush(self):
        hand1 = pk.PokerHand(["AD", "JD", "TD", "QD", "KD"])
        hand2 = pk.PokerHand(["8D", "JD", "TD", "9D", "7D"])

        self.assertTrue(hand1 > hand2)

    def test_largerThenHand_straightFlush_FourOfAKind(self):
        hand1 = pk.PokerHand(["8D", "JD", "TD", "9D", "7D"])
        hand2 = pk.PokerHand(["4D", "4C", "4H", "4S", "KD"])

        self.assertTrue(hand1 > hand2)

    def test_largerThenHand_FullHouse_FourOfAKind(self):
        hand1 = pk.PokerHand(["4D", "4C", "4H", "4S", "KD"])
        hand2 = pk.PokerHand(["4D", "KC", "4H", "4S", "KD"])

        self.assertTrue(hand1 > hand2)

    def test_largerThenHand_FullHouse_flush(self):
        hand1 = pk.PokerHand(["4D", "JD", "2D", "7D", "KD"])
        hand2 = pk.PokerHand(["4D", "KC", "4H", "4S", "KD"])

        self.assertTrue(hand2 > hand1)

    def test_largerThenHand_flush_straight(self):
        hand1 = pk.PokerHand(["4D", "JD", "2D", "7D", "KD"])
        hand2 = pk.PokerHand(["8S", "JD", "TH", "9C", "7D"])

        self.assertTrue(hand1 > hand2)

    def test_largerThenHand_threeOfAKind_straight(self):
        hand1 = pk.PokerHand(["4D", "8C", "4H", "4S", "KD"])
        hand2 = pk.PokerHand(["8S", "JD", "TH", "9C", "7D"])

        self.assertTrue(hand2 > hand1)

    def test_largerThenHand_threeOfAKind_twoPair(self):
        hand1 = pk.PokerHand(["4D", "8C", "4H", "4S", "KD"])
        hand2 = pk.PokerHand(["9S", "JD", "7H", "9C", "7D"])

        self.assertTrue(hand1 > hand2)

    def test_largerThenHand_pair_twoPair(self):
        hand1 = pk.PokerHand(["4D", "8C", "QH", "4S", "KD"])
        hand2 = pk.PokerHand(["9S", "JD", "7H", "9C", "7D"])

        self.assertTrue(hand2 > hand1)

    def test_largerThenHand_pair_highCard(self):
        hand1 = pk.PokerHand(["4D", "8C", "QH", "4S", "KD"])
        hand2 = pk.PokerHand(["2S", "JD", "7H", "9C", "QD"])

        self.assertTrue(hand1 > hand2)
