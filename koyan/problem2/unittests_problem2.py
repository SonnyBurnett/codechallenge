import problem2 as phw
import unittest


# Some of these scenarios should never happen in a real game, but I don't know how the provided txt file is generated.
class TestPokerHand(unittest.TestCase):
    def test_cards_to_numbers_conversion(self):
        card = "TD"
        result = phw.convert_cards_to_numbers(card)
        self.assertEqual(10.1, result)

    def test_straight(self):
        hand = [8, 7, 6, 5, 4]
        straight = phw.check_for_straight(hand)
        self.assertTrue(straight)

    def test_flush(self):
        hand = [9.1, 4.1, 8.1, 10.1, 14.1]
        flush = phw.check_for_flush(hand)
        self.assertTrue(flush)

    def test_score(self):
        hand = ["8D", "2H", "4S", "5D", "7C"]
        score = phw.calculate_hand_score(hand)
        self.assertEqual(1.0807050402, score)

    def test_check_sets(self):
        nothing = phw.check_for_sets([11, 9, 8, 7, 2])
        pair = phw.check_for_sets([11, 11, 8, 7, 2])
        three = phw.check_for_sets([11, 11, 11, 7, 2])
        four = phw.check_for_sets([11, 11, 11, 11, 2])
        two = phw.check_for_sets([11, 11, 8, 8, 2])
        full = phw.check_for_sets([11, 11, 11, 7, 7])
        self.assertEqual([False, False, False, False], nothing)
        self.assertEqual([True, False, False, False], pair)
        self.assertEqual([True, True, False, False], three)
        self.assertEqual([True, True, True, False], four)
        self.assertEqual([True, False, True, False], two)
        self.assertEqual([True, True, False, True], full)

    def test_straight_score(self):
        hand = ["8D", "6H", "4S", "5D", "7C"]
        score = phw.calculate_hand_score(hand)
        self.assertEqual(5.0807060504, score)

    def test_flush_score(self):
        hand = ["8D", "2D", "4D", "5D", "7D"]
        score = phw.calculate_hand_score(hand)
        self.assertEqual(6.0807050402, score)

    def test_flush_two_pair_score(self):
        hand = ["8D", "8D", "4D", "4D", "2D"]
        score = phw.calculate_hand_score(hand)
        self.assertEqual(6.0808040402, score)

    def test_flush_four_of_a_kind_score(self):
        hand = ["8D", "8D", "8D", "8D", "2D"]
        score = phw.calculate_hand_score(hand)
        self.assertEqual(8.0808080802, score)

    def test_straight_flush_score(self):
        hand = ["8D", "6D", "4D", "5D", "7D"]
        score = phw.calculate_hand_score(hand)
        self.assertEqual(9.0807060504, score)

    def test_same_hand_combinations(self):
        line = "TD TC TS TH 2C 9C 9D 9S 9H 2C"
        winner = phw.check_hand_winner(line)
        self.assertEqual(True, winner)

    def test_high_card_winner(self):
        line = "TD TC TS 9H 2C TC TD TH 8H 2C"
        winner = phw.check_hand_winner(line)
        self.assertEqual(True, winner)

    def test_second_high_card_winner(self):
        line = "TD TC TS 9H 3C TC TD TH 9S 2C"
        winner = phw.check_hand_winner(line)
        self.assertEqual(True, winner)

    def test_equal_hands(self):
        line = "TD TC TS 9H 3C TC TD TH 9H 3C"
        winner = phw.check_hand_winner(line)
        self.assertEqual(False, winner)

    def test_wrong_input(self):
        short_line = "TD TC TS 9H 3C TC TD TH 9H"
        long_line = "TD TC TS 9H 3C TC TD TH 9H 3C 8C"
        wrong_card_notation = "10X"
        wrong_card_notation_line = "TD TC TS 9H 3C TC TD TH 9H 3X"
        self.assertRaises(ValueError, phw.check_hand_winner, short_line)
        self.assertRaises(ValueError, phw.check_hand_winner, long_line)
        self.assertEqual(0.0, phw.convert_cards_to_numbers(wrong_card_notation))
        self.assertTrue(phw.check_hand_winner(wrong_card_notation_line))

    def test_correct_answer(self):
        file = "p054_poker.txt"
        answer = phw.calculate_number_of_wins(file)
        self.assertEqual(376, answer)


if __name__ == "__main__":
    unittest.main()
