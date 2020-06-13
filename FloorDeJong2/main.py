from Competition import Poker_Competition
from player import Player

floor = Player("Floor")
freek = Player("Freek")
emma = Player("Emma")


cards_random = "5H 5C 6S 7S KD 2C 3S 8S 8D 4D 2C 5C 7D 8S QH"
cards_two_royal_flush = "JD 10D QD KD AD 2C 5C 7D 8S QH JS 10S QS KS AS"
cards_same_values = "5H 5C 6S 7S KD 5H 5C 6S 7S KD 2C 5C 7D 8S QH"

cards = cards_same_values
cards = cards.split()

# player_one.set_hand(player_one_cards)
# player_two.set_hand(player_two_cards)
# print("Hand is", player_one.get_hand())
# print("Hand is", player_two.get_hand())

# player_one.add_win()
# print(player_one.get_wins())

# print(player_one.get_highest_card())

poker_competition = Poker_Competition()
poker_competition.add_player(floor)
poker_competition.add_player(freek)
poker_competition.add_player(emma)

poker_competition.deal_cards(cards)
print("Hand is", floor.get_hand().get_hand(), ", value = ", floor.get_hand().get_hand_value())
print("Hand is", freek.get_hand().get_hand(), ", value = ", freek.get_hand().get_hand_value())
print("Hand is", emma.get_hand().get_hand(), ", value = ", emma.get_hand().get_hand_value())

print(floor.get_hand().get_highest_card(1))
print(freek.get_hand().get_highest_card(1))

highest = poker_competition.determine_winner_via_highest_card(floor, freek, 1)
print(highest.get_name())

# winner = poker_competition.determine_winner()
# print("Winner is", winner.get_name(), ", total wins = ", winner.get_wins())
