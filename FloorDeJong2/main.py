from Competition import Poker_Competition
from player import Player

player_one = Player("Floor")


def find_winner(cards):
    cards = cards.split()
    player_one_cards = cards[0:5]
    player_two = cards[5:11]
    # print(player_one)
    # print(player_two)

    player_one.set_hand(player_one_cards)
    print("Hand is", player_one.get_hand())

    # player_one.add_win()
    # print(player_one.get_wins())

    # print(player_one.get_highest_card())

    poker_competion = Poker_Competition()
    poker_competion.add_player(player_one)

    winner = 1
    return winner

input_1 = "2S 3S 4S 5S AS 8S 2C 3S 8D HD"
find_winner(input_1)
