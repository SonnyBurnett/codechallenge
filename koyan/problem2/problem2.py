def check_hand_winner(hand_line):
    hand_as_list = hand_line.strip().split()
    if len(hand_as_list) != 10:
        raise ValueError("Input line should contain 10 cards divided by a single space.")
    player1_score = calculate_hand_score(hand_as_list[:5])
    player2_score = calculate_hand_score(hand_as_list[5:])
    player1_wins_hand = player1_score > player2_score
    return player1_wins_hand


def convert_cards_to_numbers(poker_card):
    card_dictionary = {"1D": 1.1, "2D": 2.1, "3D": 3.1, "4D": 4.1, "5D": 5.1, "6D": 6.1, "7D": 7.1, "8D": 8.1,
                       "9D": 9.1, "TD": 10.1, "JD": 11.1, "QD": 12.1, "KD": 13.1, "AD": 14.1, "1H": 1.2, "2H": 2.2,
                       "3H": 3.2, "4H": 4.2, "5H": 5.2, "6H": 6.2, "7H": 7.2, "8H": 8.2, "9H": 9.2, "TH": 10.2,
                       "JH": 11.2, "QH": 12.2, "KH": 13.2, "AH": 14.2, "1C": 1.3, "2C": 2.3, "3C": 3.3, "4C": 4.3,
                       "5C": 5.3, "6C": 6.3, "7C": 7.3, "8C": 8.3, "9C": 9.3, "TC": 10.3, "JC": 11.3, "QC": 12.3,
                       "KC": 13.3, "AC": 14.3, "1S": 1.4, "2S": 2.4, "3S": 3.4, "4S": 4.4, "5S": 5.4, "6S": 6.4,
                       "7S": 7.4, "8S": 8.4, "9S": 9.4, "TS": 10.4, "JS": 11.4, "QS": 12.4, "KS": 13.4, "AS": 14.4}
    try:
        card_as_number = card_dictionary[poker_card]
    except KeyError:
        card_as_number = 0.0
    return card_as_number


def check_for_flush(hand):
    flush = False
    hand_colors = [round(card - int(card), 1) for card in hand]
    if len(set(hand_colors)) == 1:
        flush = True
    return flush


def check_for_straight(hand):
    straight = False
    high_card = hand[0]
    if high_card + high_card - 1 + high_card - 2 + high_card - 3 + high_card - 4 == sum(hand):
        straight = True
    return straight


def check_for_sets(hand):
    hand_pattern = []
    for i in range(4):
        hand_pattern.append(hand[i] == hand[i + 1])
    return hand_pattern


def calculate_hand_score(hand):
    hand_as_numbers = [convert_cards_to_numbers(card) for card in hand]
    if 0.0 in hand_as_numbers:
        hand_score = 0
    else:
        hand_no_colors = [int(card) for card in hand_as_numbers]
        hand_is_flush = check_for_flush(hand_as_numbers)
        hand_sorted = sorted(sorted(hand_no_colors, reverse=True), key=hand_no_colors.count, reverse=True)
        sets_in_hand = check_for_sets(hand_sorted)
        sets_scoring_dictionary = {"[False, False, False, False]": 1, "[True, False, False, False]": 2,
                                   "[True, True, False, False]": 4, "[True, True, True, False]": 8,
                                   "[True, False, True, False]": 3, "[True, True, False, True]": 7}
        hand_score = sets_scoring_dictionary[str(sets_in_hand)]
        if hand_score == 1:
            hand_is_straight = check_for_straight(hand_sorted)
            if hand_is_straight:
                if hand_is_flush:
                    hand_score = 9
                else:
                    hand_score = 5
        if hand_score < 5 and hand_is_flush:
            hand_score = 6
        for i in range(5):
            hand_score += (hand_sorted[i] / (100 ** (i + 1)))
        hand_score = round(hand_score, 10)
    return hand_score


def calculate_number_of_wins(file="p054_poker.txt"):
    save_file = open(file)
    wins = 0
    for line in save_file:
        if check_hand_winner(line):
            wins += 1
    save_file.close()
    return wins
