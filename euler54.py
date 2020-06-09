#
# url: https://projecteuler.net/problem=54
#

import pandas as pd
from collections import Counter
from enum import Enum


class Rank(Enum):
    Nothing = 0  # No rank
    HighCard = 1  # Highest value card
    OnePair = 2  # Two cards of the same value
    TwoPairs = 3  # Two different pairs
    ThreeOfAKind = 4  # Three cards of the same value
    Straight = 5  # All cards are consecutive values
    Flush = 6  # All cards of the same suit
    FullHouse = 7  # Three of a kind and a pair
    FourOfAKind = 8  # Four cards of the same value
    StraightFlush = 9  # All cards are consecutive values of same suit
    RoyalFlush = 10  # Ten, Jack, Queen, King, Ace, in same suit

    # need to implement the comparison function to so that the max() function can work
    # see https://stackoverflow.com/questions/39268052/how-to-compare-enums-in-python
    # I use Enum instead of IntEnum for readability of the output, where ranks as expressed as topic and not values
    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented


def get_rank(hand):

    rank = Rank.Nothing
    # To detect one/two pairs or three/four of a kind or full house
    # we count the number of values per hand and get the two most commons
    count_by_value = Counter([v for v, _ in hand]).most_common(2)

    # get value and count for the two most commons, per player
    v10, c10 = count_by_value[0]
    v11, c11 = count_by_value[1]

    # Player1 check four of a kind
    if c10 == 4:
        rank = Rank.FourOfAKind
    # check full house
    elif c10 == 3 and c11 == 2:
        rank = max(rank, Rank.FullHouse)
    # check three of a kind
    elif c10 == 3:
        rank = max(rank, Rank.ThreeOfAKind)
    # check two pairs
    elif c10 == 2 and c11 == 2:
        rank = max(rank, Rank.TwoPairs)
    # check one pair
    elif c10 == 2:
        rank = max(rank, Rank.OnePair)

    # get all values of hand
    values = [v for v, _ in hand]
    values.sort()
    # Royal flush
    if values == list(range(10, 15)):
        rank = max(rank, Rank.RoyalFlush)
    # (Straight) Flush
    elif all(s == 'C' for _, s in hand) or \
            all(s == 'D' for _, s in hand) or \
            all(s == 'S' for _, s in hand) or \
            all(s == 'H' for _, s in hand):
        rank = max(rank, Rank.Flush)
        # Straight Flush
        if values == list(range(min(values), max(values) + 1)):
            rank = max(rank, Rank.StraightFlush)
    # Straight
    elif values == list(range(min(values), max(values) + 1)):
        rank = max(rank, Rank.Straight)

    return rank, v10, v11


def get_score(hands):
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

    score1 = 0
    score2 = 0

    # Get each player hand as a list of tuples [(value, suit), ]
    # and convert card character-based value to numeric
    hand1 = [(convert_card_value(x[:1]), x[1:]) for x in hands[:5]]
    hand2 = [(convert_card_value(x[:1]), x[1:]) for x in hands[5:]]

    rank1, v10, v11 = get_rank(hand1)
    rank2, v20, v21 = get_rank(hand2)

    # if ranks tie... and also detect the High Card rank
    # TODO solve the high rank
    if rank1 == rank2:
        if rank1 == Rank.TwoPairs or rank1 == Rank.FullHouse:
            if max(v10, v11) > max(v20, v21):
                score1 = 1
            else:
                score2 = 1
        else:
            if v10 > v20:
                score1 = 1
                if rank1 == Rank.Nothing:
                    rank1 = rank1.HighCard
            else:
                score2 = 1
                if rank2 == Rank.Nothing:
                    rank2 = rank2.HighCard
    elif rank1 > rank2:
        score1 = 1
    else:
        score2 = 1

    # return the hands, the ranks and the winner score as a pandas serie
    return hands.append(pd.Series([rank1, score1, rank2, score2]))


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
    # read the input file into a pandas dataframe
    # TODO use the real file, not test
    # input_file = r'p054_poker.txt'
    # TODO create a test file
    input_file = r'test.txt'
    df = pd.read_csv(input_file, sep=' ', header=None)
    df.columns = ["c11", "c12", "c13", "c14", "c15", "c21", "c22", "c23", "c24", "c25"]
    # calculate rank & winner for each row of hands
    score = df.apply(get_score, axis=1, result_type='expand')
    score.columns = ["c11", "c12", "c13", "c14", "c15", "c21", "c22", "c23", "c24", "c25",
                     "player1", "score1", "player2", "score2"]
    # publish results

    score.to_csv('results.csv', index=False)
    print(f'Player1 wins: {score["score1"].sum()} hands')


if __name__ == "__main__":
    main()
