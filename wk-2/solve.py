import functools


def processFileLines(func, file):
    with open(file) as f:
        for line in f:
            func(line.rstrip())


def lineToHands(line):
    return (line[:14], line[15:])


def handToCards(hand):
    ranks = "23456789TJQKA"
    return list(map(lambda x: (ranks.index(x[0]), x[1]), hand.split(' ')))


def score(hand):
    cards = handToCards(hand)

    ranks = sorted([card[0] for card in cards])
    suits = [card[1] for card in cards]

    rankOccurrence = [0 for i in range(13)]
    for rank in ranks:
        rankOccurrence[rank] += 1

    singles, pairs, triples, quads = [
        [i for i in range(13) if rankOccurrence[i] == j] for j in range(1, 5)]

    flush = all(suit == suits[0] for suit in suits[1:])
    fourOfAKind = len(quads) == 1
    threeOfAKind = len(triples) == 1
    twoPair = len(pairs) == 2
    pair = len(pairs) == 1
    fullHouse = pair and threeOfAKind
    highCard = len(singles) == 5
    straight = len(singles) == 5 and ranks[4] == ranks[0] + 4

    if flush and straight:
        if singles[4] == 12:
            return 10
        else:
            return 9
    if fourOfAKind:
        return 8
    if fullHouse:
        return 7
    if flush:
        return 6
    if straight:
        return 5
    if threeOfAKind:
        return 4
    if twoPair:
        return 3
    if pair:
        return 2
    if highCard:
        return 1
    raise Exception("could not score hand {}".format(hand))
