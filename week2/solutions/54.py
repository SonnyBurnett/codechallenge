from collections import Counter


class Hand:

    def __init__(self, cards):
        self.suited = True
        suit = cards[0][1]
        reformat = []
        for card in cards:
            reformat.append(int(card[0].replace('T', '10')
                                       .replace('J', '11')
                                       .replace('Q', '12')
                                       .replace('K', '13')
                                       .replace('A', '14')))
            if suit != card[1]:
                self.suited = False
        self.cards = Counter(sorted(reformat, reverse=True))
        self.__determineStraight()
        self.__determineRank()

    def __determineStraight(self):
        self.straight = True
        cards = [*self.cards]
        card = cards[0]
        for x in cards[1:]:
            if x != card - 1:
                self.straight = False
            card = x

    def __determineRank(self):
        counts = self.cards.values()
        if 4 in counts:
            self.rank = 8
        elif 3 in counts and 2 in counts:
            self.rank = 7
        elif 3 in counts:
            self.rank = 4
        elif 2 in Counter(counts).values():
            self.rank = 3
        elif 2 in counts:
            self.rank = 2
        elif self.straight & self.suited:
            self.rank = 9
        elif self.suited:
            self.rank = 6
        elif self.straight:
            self.rank = 5
        else:
            self.rank = 1

    def __compareEqualRank(self, hand2):
        sorted1 = sorted(self.cards.items(), key=lambda x: x[1], reverse=True)
        sorted2 = sorted(hand2.cards.items(), key=lambda x: x[1], reverse=True)
        for i, card in enumerate(sorted1):
            if card != sorted2[i]:
                return card > sorted2[i]
        return False

    def __gt__(self, hand2):
        if self.rank == hand2.rank:
            result = self.__compareEqualRank(hand2)
        else:
            result = self.rank > hand2.rank
        return result


def compareHands(file):
    result = 0
    for line in file:
        hand1 = Hand(line.split()[:5])
        hand2 = Hand(line.split()[5:])
        if hand1 > hand2:
            result += 1
    return result


def main():
    with open('../tests/poker.txt') as file:
        print(compareHands(file))


if __name__ == '__main__':
    main()
