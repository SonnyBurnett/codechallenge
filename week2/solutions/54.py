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
        self.straight = self.isStraight()
        self.rank = self.rank()

    def isStraight(self):
        straight = True
        cards = [*self.cards]
        card = cards[0]
        for next in cards[1:]:
            if next != card - 1:
                straight = False
            card = next
        return straight

    def rank(self):
        counts = self.cards.values()
        if 4 in counts:
            return 8
        elif 3 in counts and 2 in counts:
            return 7
        elif 3 in counts:
            return 4
        elif 2 in Counter(counts).values():
            return 3
        elif 2 in counts:
            return 2
        elif self.straight & self.suited:
            return 9
        elif self.suited:
            return 6
        elif self.straight:
            return 5
        else:
            return 1

    def compareEqualRank(self, hand2):
        sorted1 = sorted(self.cards.items(), key=lambda x: x[1], reverse=True)
        sorted2 = sorted(hand2.cards.items(), key=lambda x: x[1], reverse=True)
        for i in range(len(sorted1)):
            if sorted1[i] != sorted2[i]:
                return sorted1[i] > sorted2[i]
        else:
            return False

    def __gt__(self, hand2):
        if self.rank == hand2.rank:
            return self.compareEqualRank(hand2)
        else:
            return self.rank > hand2.rank


def main(file):
    result = 0
    for line in file:
        hand1 = Hand(line.split()[:5])
        hand2 = Hand(line.split()[5:])
        if hand1 > hand2:
            result += 1
    return result


if __name__ == '__main__':
    with open('../tests/poker.txt') as file:
        print(main(file))
