from Competition import Poker_Competition
from player import Player
from pokerhand import PokerHand

floor = Player("Floor")
freek = Player("Freek")

cards_random = "5H 5C 6S 7S KD 2C 3S 8S 8D 4D"
cards_two_royal_flush = "JD 10D QD KD AD 2C 5C 7D 8S QH"
cards_same_values = "5H 5C 6S 7S KD 5H 5C 8S 7S KD"

cards = cards_same_values
cards = cards.split()

poker_competition = Poker_Competition()
poker_competition.add_player(floor)
poker_competition.add_player(freek)

poker_competition.deal_cards(cards)
print("Hand is", floor.get_poker_hand().get_hand(), ", value = ", floor.get_poker_hand().get_hand_value())
print("Hand is", freek.get_poker_hand().get_hand(), ", value = ", freek.get_poker_hand().get_hand_value())

print(floor.get_poker_hand().get_highest_card(1))
print(freek.get_poker_hand().get_highest_card(1))

winner = poker_competition.determine_winner()
print("Winner is", winner.get_name(), ", total wins = ", winner.get_wins())

