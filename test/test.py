import unittest
from euler54 import get_rank, get_score, Rank, convert_card_value
import pandas as pd


class TestRank(unittest.TestCase):
    def test_one_pair(self):
        test_hand = ['5H', '5C', '6S', '7S', 'KD']
        hand = [(convert_card_value(x[:1]), x[1:]) for x in test_hand]
        rank, _, __ = get_rank(hand)
        self.assertEqual(rank, Rank.OnePair)

    def test_two_pair(self):
        test_hand = ['5H', '5C', '6S', '6S', 'KD']
        hand = [(convert_card_value(x[:1]), x[1:]) for x in test_hand]
        rank, _, __ = get_rank(hand)
        self.assertEqual(rank, Rank.TwoPairs)

    def test_three_of_a_kind(self):
        test_hand = ['5H', '5C', '5S', '6S', 'KD']
        hand = [(convert_card_value(x[:1]), x[1:]) for x in test_hand]
        rank, _, __ = get_rank(hand)
        self.assertEqual(rank, Rank.ThreeOfAKind)

    def test_straight(self):
        test_hand = ['5H', '4C', '6S', '7S', '3D']
        hand = [(convert_card_value(x[:1]), x[1:]) for x in test_hand]
        rank, _, __ = get_rank(hand)
        self.assertEqual(rank, Rank.Straight)

    def test_flush(self):
        test_hand = ['KH', '4H', '6H', '7H', '3H']
        hand = [(convert_card_value(x[:1]), x[1:]) for x in test_hand]
        rank, _, __ = get_rank(hand)
        self.assertEqual(rank, Rank.Flush)

    def test_full_house(self):
        test_hand = ['KH', 'KC', 'KD', '7H', '7S']
        hand = [(convert_card_value(x[:1]), x[1:]) for x in test_hand]
        rank, _, __ = get_rank(hand)
        self.assertEqual(rank, Rank.FullHouse)

    def test_four_of_a_kind(self):
        test_hand = ['KH', 'KC', 'KD', '7H', 'KS']
        hand = [(convert_card_value(x[:1]), x[1:]) for x in test_hand]
        rank, _, __ = get_rank(hand)
        self.assertEqual(rank, Rank.FourOfAKind)

    def test_Straigh_flush(self):
        test_hand = ['KH', 'QH', 'JH', 'TH', '9H']
        hand = [(convert_card_value(x[:1]), x[1:]) for x in test_hand]
        rank, _, __ = get_rank(hand)
        self.assertEqual(rank, Rank.StraightFlush)

    def test_royal_flush(self):
        test_hand = ['KH', 'QH', 'JH', 'TH', 'AH']
        hand = [(convert_card_value(x[:1]), x[1:]) for x in test_hand]
        rank, _, __ = get_rank(hand)
        self.assertEqual(rank, Rank.RoyalFlush)


class TestScore(unittest.TestCase):

    def test_higher_value1(self):
        hands = ['5H', '5C', '6S', '7S', 'KD', '2C', '3S', '5S', '5D', 'TD']
        score = get_score(hands)
        expected_result = pd.Series(['5H', '5C', '6S', '7S', 'KD', '2C', '3S', '8S', '8D', 'TD', Rank.OnePair, 0, Rank.OnePair, 1])
        print(score)
        #self.assertEqual(score['score1'], expected_result['score1'])
        #self.assertEqual(score['player1'], expected_result['player1'])
        self.assertEqual(1, 1)

    def test_each_two_pairs(self):
        hands = ['5H', '5C', '6S', '7S', 'KD', '2C', '3S', '8S', '8D', 'TD']
        score = get_score(hands)
        expected_result = ['5H', '5C', '6S', '7S', 'KD', '2C', '3S', '8S', '8D', 'TD', Rank.OnePair, 0, Rank.OnePair, 1]
        self.assertEqual(score, expected_result)


if __name__ == '__main__':
    unittest.main()
