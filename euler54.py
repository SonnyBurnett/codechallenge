from collections import Counter


hands = (line.split() for line in open('p054_poker.txt'))
values = {r: i for i, r in enumerate('23456789TJQKA', 2)}
straights = [(v, v - 1, v - 2, v - 3, v - 4) for v in range(14, 5, -1)] + [(14, 5, 4, 3, 2)]
ranks = [(1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1), (3, 1, 1), (), (), (3, 2), (4, 1)]


def get_rank(hand):
    # counter returns a dictionary where the key is card face-value and
    # the value the number of occurrences
    # e.g. [(1, 2), (2, 9),...] 1 time a "2" value, 2 times a "9" value
    counter = Counter(x[0] for x in hand)

    # remap the tuples to have one item with the occurrence and one
    # item with the values --> (1,2,1,1), (2, 9, 6, 13, 14)
    hand_tuple = [(num, values[key]) for key, num in counter.items()]

    # sort and merge so we obtain a tuple with the rank and with the value
    # by decreasing order, so we can manage rank tie
    # --> (2, 1, 1, 1), (14, 13, 9, 6, 2)
    # and finally convert the ranks into score value
    score = list(zip(*sorted(hand_tuple, reverse=True)))
    score[0] = ranks.index(score[0])

    # And here some specific handling for straights
    if len(set(card[1] for card in hand)) == 1:
        score[0] = 5  # flush
    if score[1] in straights:
        score[0] = 8 if score[0] == 5 else 4  # str./str. flush

    # return the score tuple
    return score


def main():
    # Compare the scores and count player1 won hands
    player1_win = sum(get_rank(hand[:5]) > get_rank(hand[5:]) for hand in hands)
    print(f"P1 wins {player1_win}")


if __name__ == "__main__":
    main()
