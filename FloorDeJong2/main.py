from Competition import Poker_Competition
from player import Player
from pokerhand import PokerHand

floor = Player("Floor")
freek = Player("Freek")

poker_competition = Poker_Competition()
poker_competition.add_player(floor)
poker_competition.add_player(freek)

filename = "poker.txt"
try:
    file = open(filename, "rt")
except Exception:
    import sys
    sys.exit("Opening %s failed" % filename)

counter = 0
for line in file:

    print(line.split())
    poker_competition.deal_cards(line.split())
    print("Hand is", floor.get_poker_hand().get_hand(), ", value = ", floor.get_poker_hand().get_hand_value())
    print("Hand is", freek.get_poker_hand().get_hand(), ", value = ", freek.get_poker_hand().get_hand_value())

    winner = poker_competition.determine_winner()
    print("%s : %s" %(floor.get_name(), floor.get_wins()))
    print("%s : %s" %(freek.get_name(), freek.get_wins()))

    counter += 1

print(counter)
print("wins %s: %s" % (floor.get_name(), floor.get_wins()))
print("wins %s: %s" % (freek.get_name(), freek.get_wins()))
