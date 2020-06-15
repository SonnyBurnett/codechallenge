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
    cards = list(map(lambda x: (ranks[x[:len(x)-1]], x[len(x)-1:]), line.split(' ')))
    return (cards[:5], cards[5:])

