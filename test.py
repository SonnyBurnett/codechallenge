import unittest
from euler54 import get_rank, get_score, Rank, convert_card_value


def test_one_pair():
    test_hand = ['5H', '5C', '6S', '7S', 'KD']
    hand = [(convert_card_value(x[:1]), x[1:]) for x in test_hand]
    rank, _, __ = get_rank(hand)
    assert rank == Rank.OnePair


def test_two_pair():
    test_hand = ['5H', '5C', '6S', '6S', 'KD']
    hand = [(convert_card_value(x[:1]), x[1:]) for x in test_hand]
    rank, _, __ = get_rank(hand)
    assert rank == Rank.TwoPairs


def test_three_of_a_kind():
    test_hand = ['5H', '5C', '5S', '6S', 'KD']
    hand = [(convert_card_value(x[:1]), x[1:]) for x in test_hand]
    rank, _, __ = get_rank(hand)
    assert rank == Rank.ThreeOfAKind


def test_straight():
    test_hand = ['5H', '4C', '6S', '7S', '3D']
    hand = [(convert_card_value(x[:1]), x[1:]) for x in test_hand]
    rank, _, __ = get_rank(hand)
    assert rank == Rank.Straight


def test_flush():
    test_hand = ['KH', '4H', '6H', '7H', '3H']
    hand = [(convert_card_value(x[:1]), x[1:]) for x in test_hand]
    rank, _, __ = get_rank(hand)
    assert rank == Rank.Flush


def test_full_house():
    test_hand = ['KH', 'KC', 'KD', '7H', '7S']
    hand = [(convert_card_value(x[:1]), x[1:]) for x in test_hand]
    rank, _, __ = get_rank(hand)
    assert rank == Rank.FullHouse


def test_four_of_a_kind():
    test_hand = ['KH', 'KC', 'KD', '7H', 'KS']
    hand = [(convert_card_value(x[:1]), x[1:]) for x in test_hand]
    rank, _, __ = get_rank(hand)
    assert rank == Rank.FourOfAKind


def test_Straigh_flush():
    test_hand = ['KH', 'QH', 'JH', 'TH', '9H']
    hand = [(convert_card_value(x[:1]), x[1:]) for x in test_hand]
    rank, _, __ = get_rank(hand)
    assert rank == Rank.StraightFlush


def test_royal_flush():
    test_hand = ['KH', 'QH', 'JH', 'TH', 'AH']
    hand = [(convert_card_value(x[:1]), x[1:]) for x in test_hand]
    rank, _, __ = get_rank(hand)
    assert rank == Rank.RoyalFlush


def test_higher_value1():
    hands = ['5H', '5C', '6S', '7S', 'KD', '2C', '3S', '5S', '5D', 'TD']
    score = get_score(hands)
    assert score == [Rank.OnePair, 1, Rank.OnePair, 0, hands]


def test_each_two_pairs():
    hands = ['4D', '6S', '9H', 'QH', 'QC', '3D', '6D', '7H', 'QD', 'QS']
    score = get_score(hands)
    expected_result = [Rank.OnePair, 1, Rank.OnePair, 0, hands]
    assert score == expected_result


def test_higher_value_same_high_card():
    hands = ['4D', '2S', '9H', 'JH', 'QC', '4C', '6H', '7H', 'JD', 'QS']
    score = get_score(hands)
    expected_result = [Rank.Nothing, 1, Rank.Nothing, 0, hands]
    assert score == expected_result


def test_each_full_house():
    hands = ['2H', '2D', '4C', '4D', '4S', '3C', '3D', '3S', '9S', '9D']
    score = get_score(hands)
    expected_result = [Rank.FullHouse, 1, Rank.FullHouse, 0, hands]
    assert score == expected_result


if __name__ == '__main__':
    unittest.main()
