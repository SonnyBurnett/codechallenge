def processFileLines(func, file):
    with open(file) as f:
        for line in f:
            func(line.rstrip())


def processLine(line):
    hands = lineToHands(line)
    return score(hands[0]) > score(hands[1])


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

    isFlush = all(suit == suits[0] for suit in suits[1:])
    isFourOfAKind = len(quads) == 1
    isThreeOfAKind = len(triples) == 1
    isTwoPair = len(pairs) == 2
    isPair = len(pairs) == 1
    isFullHouse = isPair and isThreeOfAKind
    isHighCard = len(singles) == 5
    isStraight = len(singles) == 5 and ranks[4] == ranks[0] + 4

    if isFlush and isStraight:
        if singles[4] == 12:
            return (10, 0, 0)
        else:
            return (9, ranks[4], 0)
    if isFourOfAKind:
        return (8, quads[0], singles[0])
    if isFullHouse:
        return (7, triples[0], pairs[0])
    if isFlush:
        return (6, ranks[4], ranks[3])
    if isStraight:
        return (5, ranks[4], 0)
    if isThreeOfAKind:
        return (4, triples[0], max(singles))
    if isTwoPair:
        return (3, max(pairs), min(pairs))
    if isPair:
        return (2, pairs[0], max(singles))
    if isHighCard:
        return (1, ranks[4], ranks[3])
    raise Exception("could not score hand {}".format(hand))
