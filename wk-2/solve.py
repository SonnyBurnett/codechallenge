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

    flush = all(suit == suits[0] for suit in suits[1:])

    rankOccurrence = [0 for i in range(14)]
    for rank in ranks:
        rankOccurrence[rank] += 1

    singles, pairs, triples, quads = [
        [i for i in range(14) if rankOccurrence[i] == j] for j in range(1, 5)]

    fourOfAKind = len(quads) == 1
    threeOfAKind = len(triples) == 1
    twoPair = len(pairs) == 2
    highCard = len(singles) == 5

    if fourOfAKind:
        return 8
    if flush:
        return 6
    if threeOfAKind:
        return 4
    if twoPair:
        return 3
    if pairs:
        return 2
    if highCard:
        return 1
    raise Exception("could not score hand {}".format(hand))
