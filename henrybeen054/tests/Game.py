import sys
import unittest

sys.path.append('../')

from classes.Hand import Hand
from classes.Hand import SCORE_SHIFTERS


class TestCard(unittest.TestCase):
    def test_when_receiving_straight_from_seven_then_return_correct_score(self):
        hand = Hand(0, ["3H", "7C", "4H", "6H", "5H"])

        hand_scores = [3, 1, 3]
        hand_score = sum(hand_scores)

        expected_scores = [hand_score, 7, 6, 5, 4, 3]
        expected_score = sum([a * b for a, b in zip(SCORE_SHIFTERS, expected_scores)])

        score = hand.get_score()

        self.assertEqual(expected_score, score)

    def test_when_receiving_eight_high(self):
        hand = Hand(0, ["3H", "8C", "4H", "6H", "5H"])

        hand_scores = [2, 1, 1]
        hand_score = sum(hand_scores)

        expected_scores = [hand_score, 8, 6, 5, 4, 3]
        expected_score = sum([a * b for a, b in zip(SCORE_SHIFTERS, expected_scores)])

        score = hand.get_score()

        self.assertEqual(expected_score, score)

    def test_when_receiving_pair_of_fives(self):
        hand = Hand(0, ["3H", "5C", "4H", "6H", "5H"])

        hand_scores = [3, 1, 3]
        hand_score = sum(hand_scores)

        expected_scores = [hand_score, 5, 6, 4, 3]
        expected_score = sum([a * b for a, b in zip(SCORE_SHIFTERS, expected_scores)])

        score = hand.get_score()

        self.assertEqual(expected_score, score)


if __name__ == '__main__':
    unittest.main()
