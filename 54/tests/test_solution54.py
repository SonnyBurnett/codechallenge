import unittest
from solution54 import *

class HighestHandTestCases(unittest.TestCase):
    def test_highest_hand_one_highest(self):
        hand_player1 = ['2H', '2C', '4S', '4S', '6S']
        self.assertEqual(find_highest_card(hand_player1),[6])

    def test_highest_hand_two_highest(self):
        hand_player1 = ['2H', '2C', '4S', '6S', '6S']
        self.assertEqual(find_highest_card(hand_player1),[6])

class OnePairTestCases(unittest.TestCase):
    def test_highest_only_one_pair(self):
        hand_player1 = ['2H', '2C', '3S', '4S', '6S']
        self.assertEqual(find_value_occurrences(hand_player1),[[2, 2], [3, 1], [4,1], [6, 1]])


class TwoPairTestCases(unittest.TestCase):
    def test_highest_only_one_pair(self):
        hand_player1 = ['2H', '2C', '3S', '3C', '6S']
        self.assertEqual(find_value_occurrences(hand_player1),[[2, 2], [3, 2], [6, 1]])


if __name__ == '__main__':
    unittest.main()
