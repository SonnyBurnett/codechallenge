from collections import defaultdict


class PokerHand:

    def __init__(self, cards):
        self.cards = cards
        self.hand_value = []
        self.hand = self.determine_hand(self.cards)

    def get_hand(self):
        return self.hand

    def get_hand_value(self):
        return self.hand_value

    def get_highest_card(self, attempts):
        card_values = sorted([self.replace_letter_cards(self.cards[i][0]) for i in range(len(self.cards))])
        return card_values[- attempts]

    def get_keys_by_value(self, key_dict, number):
        return [int(key) for (key, value) in key_dict.items() if value == number]

    def replace_letter_cards(self, card):
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
        else:
            return int(card)

    def check_consecutive(self, cards_list):
        return sorted(cards_list) == list(range(min(cards_list), max(cards_list) + 1))

    def determine_hand(self, cards):
        # print(cards)

        cards_per_suits = defaultdict(list)
        for card in cards:
            cards_per_suits[card[1]].append(self.replace_letter_cards(card[0]))
        # print(cards_per_suits)

        max_suit = max(cards_per_suits, key=lambda x: len(set(cards_per_suits[x])))
        max_suit_values = cards_per_suits[max_suit]
        # print(max_suit_values)

        if len(max_suit_values) == 5:
            # self.hand_suit = max_suit
            if self.check_consecutive(max_suit_values):
                if 14 in max_suit_values:
                    return 10
                else:
                    return 9
            else:
                return 6

        cards_per_value = {}
        for card in cards:
            cards_per_value[self.replace_letter_cards(card[0])] = cards_per_value.get(
                self.replace_letter_cards(card[0]), 0) + 1
        # print(cards_per_value)

        if 4 in cards_per_value.values():
            self.hand_value.append(self.get_keys_by_value(cards_per_value, 4)[0])
            return 8

        elif 3 in cards_per_value.values():
            self.hand_value.append(self.get_keys_by_value(cards_per_value, 3)[0])
            if 2 in cards_per_value.values():
                # self.hand_value.append(self.get_keys_by_value(cards_per_value, 2)[0])
                return 7
            else:
                return 4

        elif self.check_consecutive(list(cards_per_value)):
            return 5

        elif 2 in cards_per_value.values():
            self.hand_value.extend(sorted(self.get_keys_by_value(cards_per_value, 2), reverse=True))
            if len(self.hand_value) == 2:
                return 3
            else:
                return 2

        else:
            return 1
