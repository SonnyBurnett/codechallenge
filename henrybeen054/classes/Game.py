import collections
from classes.Card import Card

SCORE_SHIFTERS = (
    pow(16, 5),
    pow(16, 4),
    pow(16, 3),
    pow(16, 2),
    pow(16, 1),
    1)


class Hand:
    def __init__(self, player_id, hand_descriptor):
        self.player_id = player_id

        self.cards = list(map(Card, hand_descriptor))
        self.sorted_card_values = sorted([c.value for c in self.cards], reverse=True)

    def __is_straight(self):
        for i in range(len(self.sorted_card_values) - 1):
            if self.sorted_card_values[i] != self.sorted_card_values[i + 1] + 1 :
                return False

        return True

    def __is_flush(self):
        return all(c.suit == self.cards[0].suit for c in self.cards)

    def __get_hand_type_score(self):
        if self.__is_flush() and self.__is_straight:
            return 16

        if self.__is_flush():
            return 12

        if self.__is_straight:
            return 11

        values_counter = sorted(collections.Counter(self.sorted_card_values).values(), reverse=True)
        return values_counter[0] + 8 + values_counter[1]

    def get_score(self):
        individual_scores = [self.__get_hand_type_score()] + self.sorted_card_values
        weighted_scores = [a * b for a, b in zip(SCORE_SHIFTERS, individual_scores)]
        return sum(weighted_scores)