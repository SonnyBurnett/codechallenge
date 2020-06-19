import unittest
from solution54 import *


class HighestHandTestCases(unittest.TestCase):
    def test_highest_hand_one_highest(self):
        hand_player1 = ['2H', '2C', '4S', '4S', '6S']
        self.assertEqual(find_highest_card(hand_player1), 6)

    def test_highest_hand_two_highest(self):
        hand_player1 = ['2H', '2C', '4S', '6S', '6S']
        self.assertEqual(find_highest_card(hand_player1), 6)


class GenericFunctionsTestCases(unittest.TestCase):
    def test_find_suite_occurrences(self):
        hand_player1 = ['2H', '2C', '4S', '6S', '6S']
        self.assertEqual(find_suite_occurrences(hand_player1), [['H', 1], ['S', 3], ['C', 1]])

    def test_is_all_consecutive_true(self):
        hand_player1 = ['2H', '3C', '4S', '5S', '6S']
        self.assertEqual(is_all_consecutive(hand_player1), True)


class OnePairTestCases(unittest.TestCase):
    def test_highest_only_one_pair(self):
        hand_player1 = ['2H', '2C', '3S', '4S', '6S']
        self.assertEqual(find_value_occurrences(hand_player1), [[2, 2], [3, 1], [4, 1], [6, 1]])


class TwoPairTestCases(unittest.TestCase):
    def test_highest_only_one_pair(self):
        hand_player1 = ['2H', '2C', '3S', '3C', '6S']
        self.assertEqual(is_two_pairs(hand_player1), True)


class ThreeOfAKindTestCases(unittest.TestCase):
    def test_three_of_a_kind(self):
        hand_player1 = ['3D', '5C', '6H', '3S', '3C']
        self.assertEqual(is_three_of_a_kind(hand_player1), True)

    def test_not_three_of_a_kind(self):
        hand_player1 = ['3D', '5C', '6H', '3S', '5C']
        self.assertEqual(is_three_of_a_kind(hand_player1), False)


class determine_winner(unittest.TestCase):
    def both_same_value_pair_hand2_wins(self):
        game = "3D 6D 7H QD QS 4D 6S 9H QH QC"
        self.assertEqual(determine_winner(game), 2)

    def both_full_house_hand1_wins_with_4(self):
        game = "2H 2D 4C 4D 4S 3C 3D 3S 9S 9D"
        self.assertEqual(determine_winner(game), 1)


if __name__ == '__main__':
    unittest.main()
