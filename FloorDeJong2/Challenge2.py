from collections import defaultdict


def reverse_string_in_list(str_list):
    return [x[::-1] for x in str_list]


def get_keys_by_value(list, number):
    return [int(key) for (key, value) in list.items() if value == number]


def replace_letter_cards(card):
    if card == "J":
        return 11
    elif card == "Q":
        return 12
    elif card == "K":
        return 13
    elif card == "A":
        return 14
    else:
        return int(card)


def check_consecutive(max_key_list):
    return False


def determine_hand(player_hand):
    print(player_hand)

    player_hand_reversed = reverse_string_in_list(player_hand)
    cards_per_suits = defaultdict(list)
    for card in player_hand_reversed:
        cards_per_suits[card[0]].append(replace_letter_cards(card[1]))
    # print(cards_per_suits)

    max_suit = max(cards_per_suits, key=lambda x: len(set(cards_per_suits[x])))
    max_suit_values = cards_per_suits[max_suit]
    # print(max_suit_values)

    if len(max_suit_values) == 5:
        if check_consecutive(max_suit_values):
            if "A" in max_suit_values:
                return 10
            else:
                return 9
        else:
            return 6

    # value2 = {}
    # value2 = {card[0]: (value2.get(card[0], 0) + 1) for card in player_hand}
    # print("comprehension", value2)

    cards_per_value = {}
    for card in player_hand:
        cards_per_value[replace_letter_cards(card[0])] = cards_per_value.get(replace_letter_cards(card[0]), 0) + 1
    print(cards_per_value)

    if 4 in cards_per_value.values():
        value = get_keys_by_value(cards_per_value, 4)[0]
        return 8, value

    elif 3 in cards_per_value.values():
        value_3 = get_keys_by_value(cards_per_value, 3)[0]
        if 2 in cards_per_value.values():
            value_2 = get_keys_by_value(cards_per_value, 2)[0]
            return 7, value_3, value_2
        else:
            return 4, value_3

    elif check_consecutive(list(cards_per_value)):
        return 5

    elif 2 in cards_per_value.values():
        value = get_keys_by_value(cards_per_value, 2)
        if len(value) == 2:
            return 3, max(value), min(value)
        else:
            return 2, value[0]

    else:
        return 1, max(cards_per_value.keys())


def find_winner(hands):
    hands = hands.split()
    player_one = hands[0:5]
    player_two = hands[5:11]
    # print(player_one)
    # print(player_two)

    print(determine_hand(player_one))

    winner = 1
    return winner


input_1 = "2S 3C 6H 4S AD 8S 2C 3S 8D HD"
find_winner(input_1)

# input_2 = input_1.split()
# print(input_2)
# for i, card in enumerate(input_2):
#     # print(i, card, card[0])
#     if card[0] in ["J", "Q", "H", "A"]:
#         input_2[i] = card.replace("A", "14")
#         print(i, card)


# new_list = []
# for i in range(10):
#     if i <= 5:
#         new_list.append(i*2)
# print(new_list)
#
# new_list = [i*2 for i in range(10) if i <= 5]
# print(new_list)
