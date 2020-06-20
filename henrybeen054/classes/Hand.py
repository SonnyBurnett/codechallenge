import collections

CARD_VALUES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

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

        self.__get_suits_from_hand_descriptor(hand_descriptor)
        self.__get_values_from_hand_descriptor(hand_descriptor)

    def __get_suits_from_hand_descriptor(self, hand_descriptor):
        self.card_suits = list(map(lambda x: x[1], hand_descriptor))

    def __get_values_from_hand_descriptor(self, hand_descriptor):
        card_value_descriptors = map(lambda x: x[0], hand_descriptor)
        card_values = map(lambda x: CARD_VALUES[x], card_value_descriptors)

        card_values_occurrences = collections.Counter(card_values)
        self.card_values_to_count = collections.OrderedDict(
            sorted(card_values_occurrences.items(), reverse=True, key=lambda i: (i[1], i[0])))

    def __is_straight(self):
        if len(self.card_values_to_count) != 5:
            return False

        values = list(self.card_values_to_count.keys())

        for i in range(1, len(values)):
            if values[i] != values[i - 1] - 1:
                return False

        return True

    def __is_flush(self):
        return all(x == self.card_suits[0] for x in self.card_suits)

    def __get_hand_type_score(self):
        is_flush = self.__is_flush()
        is_straight = self.__is_straight()

        if is_flush and is_straight:
            scores = [4, 2]
        elif self.__is_flush():
            scores = [3, 1, 4]
        elif is_straight:
            scores = [3, 1, 3]
        else:
            scores = sorted(collections.Counter(self.card_values_to_count).values(), reverse=True)

        weighted_scores = [a * b for a, b in zip([64, 8, 1], scores)]
        score = sum(weighted_scores)
        return score

    def get_score(self):
        scores = [self.__get_hand_type_score()] + list(self.card_values_to_count.keys())
        weighted_scores = [a * b for a, b in zip(SCORE_SHIFTERS, scores)]
        score = sum(weighted_scores)
        return score
