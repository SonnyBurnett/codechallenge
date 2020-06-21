import sys
from collections import Counter


def replace_letter_cards(card):
    if card == "T":
        return 10
    elif card == "J":
        return 11
    elif card == "Q":
        return 12
    elif card == "K":
        return 13
    elif card == "A":
        return 14
    elif card in ["{:1d}".format(x) for x in range(1, 10)]:
        return int(card)
    else:
        sys.exit("Card %s does not exists" % card)


def is_flush(cards):
    suit = cards[0][1]
    for card in cards:
        if card[1] != suit:
            return False
    return True


def is_straight(cards_list):
    if Counter(cards_list.values())[1] == 5:
        return sorted(cards_list.keys()) == list(range(min(cards_list.keys()), max(cards_list.keys()) + 1))
    else:
        return False

class PokerHand:
    def __init__(self, cards):
        self.__cards = cards
        self.__card_values = Counter(sorted([replace_letter_cards(card[0]) for card in self.__cards], reverse=True))
        self.__hand = self.determine_hand()


    def get_hand(self):
        return self.__hand

    def get_card_values(self):
        return self.__card_values

    def get_cards(self):
        return self.__cards

    def determine_hand(self):
        if is_flush(self.__cards):
            if is_straight(self.__card_values):
                if 14 in self.__card_values:
                    return 10
                else:
                    return 9
            else:
                return 6

        if 4 in self.__card_values.values():
            return 8
        elif all(x in self.__card_values.values() for x in [3, 2]):
            return 7
        elif is_straight(self.__card_values):
            return 5
        elif 3 in self.__card_values.values():
            return 4
        elif Counter(self.__card_values.values())[2] == 2:
            return 3
        elif 2 in self.__card_values.values():
            return 2
        else:
            return 1

    def __gt__(self, other):
        if self.__hand == other.get_hand():
            for i in range(len(self.__card_values)):
                if self.__card_values.most_common()[i][0] > other.get_card_values().most_common()[i][0]:
                    return True
                elif self.__card_values.most_common()[i][0] < other.get_card_values().most_common()[i][0]:
                    return False

            sys.exit("The values of cards where same")

        else:
            return self.__hand > other.get_hand()