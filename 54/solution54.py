def highest_score(hand):
    highest = 2
    for card in hand:
        if values.index(card[0]) > highest:
            highest = values.index(card[0])
    return highest+2

# def highest_card(hand):
#     return score
#
# def score_one_pair(hand):
#     return score
#
# def score_two_pairs(hand):
#     return score
#
# def score_three_of_a_kind(hand):
#     return score
#
# def score_straight(hand):
#     return score
#
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

colors = ['H', 'D', 'S', 'C']
values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

hand_player1 = ['5H','5C','6S','7S','KD']
print(highest_score(hand))

# score_flush(hand)
number_of_players = 2
