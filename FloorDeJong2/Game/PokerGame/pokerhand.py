import sys
from collections import defaultdict


def is_flush(cards):
    suit = cards[0][1]
    for card in cards:
        if card[1] != suit:
            return False
    return True


def is_straight(cards_list):
    return sorted(cards_list) == list(range(min(cards_list), max(cards_list) + 1))


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


def get_nr_cards_per_value(cards):
    cards_per_value = {}
    for card in cards:
        cards_per_value[replace_letter_cards(card[0])] = cards_per_value.get(
            replace_letter_cards(card[0]), 0) + 1

    return cards_per_value


def find_key_with_value(some_dict, number):
    return [int(key) for (key, value) in some_dict.items() if value == number]



class PokerHand:

    def __init__(self, cards):
        self.__cards = cards
        self.__hand_value = []
        self.__hand = self.determine_hand()

    def get_hand(self):
        return self.__hand

    def get_hand_value(self):
        return self.__hand_value
    
    def get_cards(self):
        return self.__cards

    def get_highest_card(self, attempt):
        if attempt > 5 or attempt < 1:
            sys.exit("Invalid variable: 1 <= attempts <= 5")

        card_values = sorted([replace_letter_cards(card[0]) for card in self.__cards])
        return card_values[- attempt]

    def determine_hand(self):

        if is_flush(self.__cards):
            card_values = [replace_letter_cards(card[0]) for card in self.__cards]
            if is_straight(card_values):
                if 14 in card_values:
                    return 10
                else:
                    return 9
            else:
                return 6

        nr_cards_per_value = get_nr_cards_per_value(self.__cards)
        if 4 in nr_cards_per_value.values():
            self.__hand_value.append(find_key_with_value(nr_cards_per_value, 4)[0])
            return 8

        elif 3 in nr_cards_per_value.values():
            self.__hand_value.append(find_key_with_value(nr_cards_per_value, 3)[0])
            if 2 in nr_cards_per_value.values():
                return 7
            else:
                return 4

        elif is_straight(list(nr_cards_per_value)):
            return 5

        elif 2 in nr_cards_per_value.values():
            self.__hand_value.extend(sorted(find_key_with_value(nr_cards_per_value, 2), reverse=True))
            if len(self.__hand_value) == 2:
                return 3
            else:
                return 2

        else:
            return 1
