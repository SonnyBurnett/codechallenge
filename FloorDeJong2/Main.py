from player import Player

player_one = Player("Floor")


def find_winner(hands):
    hands = hands.split()
    player_one_hand = hands[0:5]
    player_two = hands[5:11]
    # print(player_one)
    # print(player_two)

    print(player_one.determine_hand(player_one_hand))
    print(player_one.get_hand(player_one_hand))

    winner = 1
    return winner

input_1 = "2S 3C 4H 4S AD 8S 2C 3S 8D HD"
find_winner(input_1)
