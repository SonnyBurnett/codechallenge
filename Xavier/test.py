import unittest
import pytest
from euler54 import get_rank
import itertools

# test hands representing each rank cases
hands1 = [
    ['4D', '2S', '9H', 'JH', 'QC'],
    ['5H', '5C', '6S', '7S', 'KD'],
    ['5H', '5C', '6S', '6S', 'KD'],
    ['5H', '5C', '5S', '6S', 'KD'],
    ['5H', '4C', '6S', '7S', '3D'],
    ['KH', '4H', '6H', '7H', '3H'],
    ['KH', 'KC', 'KD', '7H', '7S'],
    ['KH', 'KC', 'KD', '7H', 'KS'],
    ['KH', 'QH', 'JH', 'TH', '9H'],
    ['KH', 'QH', 'JH', 'TH', 'AH']
]
hands2 = [
    ['4C', '6H', '7H', 'JD', 'QS'],
    ['4H', '4C', '6S', '7S', 'KD'],
    ['8H', '8C', '9S', '9S', 'KD'],
    ['6H', '6C', '6S', '5S', 'KD'],
    ['5S', '4S', '6H', '7C', '8D'],
    ['KC', '4C', '6C', '7C', '3C'],
    ['QH', 'QC', 'QD', '8H', '8S'],
    ['JH', 'JC', 'JD', '5H', 'JS'],
    ['KC', 'QC', 'JC', 'TC', '9C'],
    ['KC', 'QC', 'JC', 'TC', 'AC']
]

# Combine (scalar product) the two hands to have the 100 possible combinations from the above hands
comb_hand = itertools.product(hands1, hands2)

# Expected player1 winning pattern for the hands combination
win1 = [
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1,
    0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0
]


# Merge hands and expected result in one single parameter, passed to the test suite
# the decorator will call the test routine as much time as we have items in the combination
@pytest.mark.parametrize('hands', list(zip(comb_hand, win1)))
def test_all_combinations(hands):
    # decompose back the hand in player1, player2 and expected player1 result
    hand1, hand2 = hands[0]
    win = hands[1]
    # test the code for that combination
    assert (get_rank(hand1) > get_rank(hand2)) == win


if __name__ == '__main__':
    unittest.main()
