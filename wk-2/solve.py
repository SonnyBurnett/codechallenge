import functools


def processFileLines(func, file):
    with open(file) as f:
        for line in f:
            func(line.rstrip())


def parseLineToHands(line):
    ranks = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }
    cards = list(
        map(lambda x: (ranks[x[:len(x)-1]], x[len(x)-1:]), line.split(' ')))
    return (cards[:5], cards[5:])


def score(hand):
    ranks = [card[0] for card in hand]
    suits = [card[1] for card in hand]

    rankOccurrence = [0 for i in range(14)]
    for rank in ranks:
        rankOccurrence[rank] += 1

    flush = all(suit == suits[0] for suit in suits[1:])

    fourOfAKind = len([i for i in range(14) if rankOccurrence[i] == 4]) > 0

    if fourOfAKind:
        return 8
    if flush:
        return 6
    return 1
