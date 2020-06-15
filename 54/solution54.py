def find_highest_card(hand):
    return [max([values.index(card[0]) for card in hand if values.index(card[0])]) + 2]


def find_value_occurrences(hand):
    value_list = [values.index(card[0]) for card in hand]
    return [[value + 2, value_list.count(value)] for value in set(value_list)]


def find_suite_occurrences(hand):
    suite_list = [suite.index(card[1]) for card in hand]
    return [[suite[color], suite_list.count(color)] for color in set(suite_list)]


def is_all_consecutive(hand):
    value_occurences_list = find_value_occurrences(hand)
    if len(value_occurences_list) < 5:
        return False
    else:
        value_list = [element[0] for element in value_occurences_list]
        diff_list = [abs(j-i) for i,j in zip(value_list, value_list[1:])]
        return diff_list == [1,1,1,1]
    return False


def is_all_same_suite(hand):
    return len(find_suite_occurrences(hand)) == 1


def is_straight(hand):
    return len(find_value_occurrences(hand)) == 5


def is_flush(hand):
    return is_all_same_suite(hand)


def is_four_of_a_kind(hand):
    return False


def is_four_of_a_kind(hand):
    return False


def is_straight_flush(hand):
    return is_all_consecutive(hand) and is_all_same_suite() and find_highest_card(hand) < 14


def is_royal_flush(hand):
    return is_all_consecutive(hand) and is_all_same_suite() and find_highest_card(hand) == 14


def is_full_house(hand):
    pass


def is_three_of_a_kind(hand):
    pass


def is_two_pairs(hand):
    pass


def is_one_pair(hand):
    pass


def calculate_hand_score(hand):
    score = 0
    if is_royal_flush(hand):
        print("Royal Flush {}".format(hand))
        return 200
    elif is_straight_flush(hand):
        print("Straight Flush {}".format(hand))
        return 150
    elif is_four_of_a_kind(hand):
        print("Four of a kind {}".format(hand))
        return 100
    elif is_full_house(hand):
        print("Full house {}".format(hand))
        return 90
    elif is_flush(hand):
        print("Flush {}".format(hand))
        return 80
    elif is_straight(hand):
        print("Straight {}".format(hand))
        return 70
    elif is_three_of_a_kind(hand):
        print("Three of a kind {}".format(hand))
        return 60
    elif is_two_pairs(hand):
        print("Two pairs {}".format(hand))
        return 50
    elif is_one_pair(hand):
        print("One pair {}".format(hand))
        return 50
    else:
        return find_highest_card(hand)
    return score


def determine_winner(game):
    winning_hand = 1
    first_hand = game[0:14].split(" ")
    second_hand = game[15:29].split(" ")
    calculate_hand_score(first_hand)
    calculate_hand_score(second_hand)
    return winning_hand


suite = ['H', 'D', 'S', 'C']
values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

input_file = open("poker.txt", "r")
[determine_winner(game) for game in input_file]
