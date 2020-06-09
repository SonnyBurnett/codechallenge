def find_highest_card(hand):
    return [max([values.index(card[0]) for card in hand if values.index(card[0])]) + 2]


def find_value_occurrences(hand):
    value_list = [values.index(card[0]) for card in hand]
    return [[value+2, value_list.count(value)] for value in set(value_list)]


def find_suite_occurrences(hand):
    suite_list = [suite.index(card[1]) for card in hand]
    return [[suite[color], suite_list.count(color)] for color in set(suite_list)]


def score_straight(hand):
    value_list = [values.index(card[0]) for card in hand]
    return value_list

# def score_flush(hand):
#     return score
#
# def score_fullhouse(hand):
#     return score
#
# def score_four_of_a_kind(hand):
#     return 90
#
# def score_straight_flush(hand):
#     return 90
#
# def score_royal_flush(hand):
#     return 100

suite = ['H', 'D', 'S', 'C']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

hand_player1 = ['2H', '2C', '4S', '4S', '6S']
print(find_suite_occurrences(hand_player1))

# score_flush(hand)
number_of_players = 2
