#
# url: https://projecteuler.net/problem=54
#

import pandas as pd
from collections import Counter
from enum import Enum


class Rank(Enum):
    Nothing = 0         # No rank
    HighCard = 1        # Highest value card
    OnePair = 2         # Two cards of the same value
    TwoPairs = 3        # Two different pairs
    ThreeOfAKind = 4    # Three cards of the same value
    Straight = 5        # All cards are consecutive values
    Flush = 6           # All cards of the same suit
    FullHouse = 7       # Three of a kind and a pair
    FourOfAKind = 8     # Four cards of the same value
    StraightFlush = 9   # All cards are consecutive values of same suit
    RoyalFlush = 10     # Ten, Jack, Queen, King, Ace, in same suit

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented

    def max(self, other):
        if self.__class__ is other.__class__:
            if self.value > other.value:
                return self.value
            else:
                return other.value
        return NotImplemented


def rank(hands):
    """
    Calculate the rank for each player's hand

    Rules:
    If two players have the same ranked hands then the rank made up of the highest value wins;
    for example, a pair of eights beats a pair of fives (see example 1 below).
    But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared;
    if the highest cards tie then the next highest cards are compared, and so on.


    :param hands:
    :return:
    """

    # rank of each player
    player1 = Rank.Nothing
    player2 = Rank.Nothing
    score1 = 0
    score2 = 0

    # Get each player hand as a list of tuples [(value, suit), ]
    # and convert card character-based value to numeric
    hand1 = [(convert_card_value(x[:1]), x[1:]) for x in hands[:5]]
    hand2 = [(convert_card_value(x[:1]), x[1:]) for x in hands[5:]]

    # To detect one/two pairs or three/four of a kind or full house
    # we count the number of values per hand and get the two most commons
    p1_count_by_value = Counter([v for v, _ in hand1]).most_common(2)
    p2_count_by_value = Counter([v for v, _ in hand2]).most_common(2)

    v10, c10 = p1_count_by_value[0]
    v11, c11 = p1_count_by_value[1]
    v20, c20 = p2_count_by_value[0]
    v21, c21 = p2_count_by_value[1]

    # Player1 check four of a kind
    if c10 == 4:
        player1 = Rank.FourOfAKind
    # check full house
    elif c10 == 3 and c11 == 2:
        player1 = max(player1, Rank.FullHouse)
    # check three of a kind
    elif c10 == 3:
        player1 = max(player1, Rank.ThreeOfAKind)
    # check two pairs
    elif c10 == 2 and c11 == 2:
        player1 = max(player1, Rank.TwoPairs)
    # check one pair
    elif c10 == 2:
        player1 = max(player1, Rank.OnePair)

    # Player2 check four of a kind
    if c20 == 4:
        player2 = Rank.FourOfAKind
    # check full house
    elif c20 == 3 and c21 == 2:
        player2 = max(player2, Rank.FullHouse)
    # check three of a kind
    elif c20 == 3:
        player2 = max(player2, Rank.ThreeOfAKind)
    # check two pairs
    elif c20 == 2 and c21 == 2:
        player2 = max(player2, Rank.TwoPairs)
    # check one pair
    elif c20 == 2:
        player2 = max(player2, Rank.OnePair)

    # To detect flushes, we need to order the cards by suit

    # Detect the Straight

    # Detect the High Cards

    # if ranks tie...
    if player1 == player2:
        if player1.TwoPairs or player1.FullHouse:
            if max(v10, v11) > max(v20, v21):
                score1 = 1
            else:
                score2 = 1
        else:
            if v10 > v20:
                score1 = 1
            else:
                score2 = 1
    elif player1 > player2:
        score1 = 1
    else:
        score2 = 1

    return hands.append(pd.Series([player1, score1, player2, score2]))


def convert_card_value(val):
    """
    give a numeric value to higher card values (10, J, Q, K, A)
    :param val: card value 2-9, T, J, Q, K, A
    :return: card value as numeric 2 - 14
    """
    if val == 'T':
        return 10
    elif val == 'J':
        return 11
    elif val == 'Q':
        return 12
    elif val == 'K':
        return 13
    elif val == 'A':
        return 14
    else:
        return int(val)


def main():

    input_file = r'p054_poker.txt'
    df = pd.read_csv(input_file, sep=' ', header=None)
    df.columns = ["c11", "c12", "c13", "c14", "c15", "c21", "c22", "c23", "c24", "c25"]
    score = df.apply(rank, axis=1, result_type='expand')
    score.columns = ["c11", "c12", "c13", "c14", "c15", "c21", "c22", "c23", "c24", "c25",
                     "player1", "score1", "player2", "score2"]
    print(score.head(10))
    print(f'Player1 wins: {score["score1"].sum()} hands')


if __name__ == "__main__":
    main()
