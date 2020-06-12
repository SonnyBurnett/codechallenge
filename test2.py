import unittest
from euler54 import get_rank, get_score, Rank, convert_card_value
import itertools

hands1 = [
    [Rank.Nothing, ['4D', '2S', '9H', 'JH', 'QC']],
    [Rank.OnePair, ['5H', '5C', '6S', '7S', 'KD']],
    [Rank.TwoPairs, ['5H', '5C', '6S', '6S', 'KD']],
    [Rank.ThreeOfAKind, ['5H', '5C', '5S', '6S', 'KD']],
    [Rank.Straight, ['5H', '4C', '6S', '7S', '3D']],
    [Rank.Flush, ['KH', '4H', '6H', '7H', '3H']],
    [Rank.FullHouse, ['KH', 'KC', 'KD', '7H', '7S']],
    [Rank.FourOfAKind, ['KH', 'KC', 'KD', '7H', 'KS']],
    [Rank.StraightFlush, ['KH', 'QH', 'JH', 'TH', '9H']],
    [Rank.RoyalFlush, ['KH', 'QH', 'JH', 'TH', 'AH']]
]
hands2 = [
    [Rank.Nothing, ['4C', '6H', '7H', 'JD', 'QS']],
    [Rank.OnePair, ['4H', '4C', '6S', '7S', 'KD']],
    [Rank.TwoPairs, ['8H', '8C', '9S', '9S', 'KD']],
    [Rank.ThreeOfAKind, ['6H', '6C', '6S', '5S', 'KD']],
    [Rank.Straight, ['5S', '4S', '6H', '7C', '8D']],
    [Rank.Flush, ['KC', '4C', '6C', '7C', '3C']],
    [Rank.FullHouse, ['QH', 'QC', 'QD', '8H', '8S']],
    [Rank.FourOfAKind, ['JH', 'JC', 'JD', '5H', 'JS']],
    [Rank.StraightFlush, ['KC', 'QC', 'JC', 'TC', '9C']],
    [Rank.RoyalFlush, ['KC', 'QC', 'JC', 'TC', 'AC']]
]

win1 = [
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0
]

win2 = [
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]


def test_all_combinations():
    hands = itertools.product(hands1, hands2)
    i = 0
    for h in hands:
        score = get_score(h[0][1]+h[1][1])
        expected_result = [
            h[0][0], win1[i], h[1][0], win2[i], h[0][1]+h[1][1]
        ]
        print(i, end='.')
        assert score == expected_result
        i += 1


if __name__ == '__main__':
    unittest.main()
