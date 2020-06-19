def find_highest_card(hand):
    return max([values.index(card[0]) for card in hand]) + 2


def find_value_occurrences(hand):
    value_list = [values.index(card[0]) for card in hand]
    return [[value + 2, value_list.count(value)] for value in set(value_list)]


def find_suite_occurrences(hand):
    suite_list = [suite.index(card[1]) for card in hand]
    return [[suite[color], suite_list.count(color)] for color in set(suite_list)]


def is_all_consecutive(hand):
    value_occurrences_list = find_value_occurrences(hand)
    if len(value_occurrences_list) < 5:
        return False
    else:
        value_list = [element[0] for element in value_occurrences_list]
        diff_list = [abs(j - i) for i, j in zip(value_list, value_list[1:])]
        return diff_list == [1, 1, 1, 1]
    return False


def is_all_same_suite(hand):
    return len(find_suite_occurrences(hand)) == 1


def is_straight(hand):
    return is_all_consecutive(hand)


def is_flush(hand):
    return is_all_same_suite(hand)


def is_four_of_a_kind(hand):
    return [element[1] for element in find_value_occurrences(hand)].count(4) == 1


def is_straight_flush(hand):
    return is_all_consecutive(hand) and is_all_same_suite(hand) and find_highest_card(hand) < 14


def is_royal_flush(hand):
    return is_all_consecutive(hand) and is_all_same_suite(hand) and find_highest_card(hand) == 14


def is_full_house(hand):
    return is_three_of_a_kind(hand) and is_one_pair(hand)


def is_three_of_a_kind(hand):
    return 3 in [element[1] for element in find_value_occurrences(hand)]


def is_two_pairs(hand):
    return [element[1] for element in find_value_occurrences(hand)].count(2) == 2


def is_one_pair(hand):
    return [element[1] for element in find_value_occurrences(hand)].count(2) == 1


def calculate_hand_score(hand):
    score = 0
    if is_royal_flush(hand):
        return 200
    elif is_straight_flush(hand):
        return 180 + find_highest_card(hand)
    elif is_four_of_a_kind(hand):
        return 160 + max([element[0] for element in find_value_occurrences(hand) if element[1] == 4])
    elif is_full_house(hand):
        return 120 + max([element[0] for element in find_value_occurrences(hand) if element[1] == 3])
    elif is_flush(hand):
        return 100 + find_highest_card(hand)
    elif is_straight(hand):
        return 80 + find_highest_card(hand)
    elif is_three_of_a_kind(hand):
        return 60 + max([element[0] for element in find_value_occurrences(hand) if element[1] == 3])
    elif is_two_pairs(hand):
        return 40 + max([element[0] for element in find_value_occurrences(hand) if element[1] == 2])
    elif is_one_pair(hand):
        return 20 + (max(element[0] for element in find_value_occurrences(hand) if element[1] == 2))
    else:
        return find_highest_card(hand)
    return score


def determine_winner(game):
    first_hand = game[0:14].split(" ")
    second_hand = game[15:29].split(" ")
    if calculate_hand_score(first_hand) > calculate_hand_score(second_hand):
        return 1
    else:
        return 2


suite = ['H', 'D', 'S', 'C']
values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
input_file = open("poker.txt", "r")

game_winner_list = [determine_winner(game) for game in input_file]
print("Player One won: {} ganes".format(game_winner_list.count(1)))
print("Player Two won: {} ganes".format(game_winner_list.count(2)))