from Game.PokerGame.competition import PokerCompetition
from Game.PokerGame.player import Player

floor = Player("Floor")
freek = Player("Freek")

poker_competition = PokerCompetition("Poker League")
poker_competition.add_player(floor)
poker_competition.add_player(freek)

filename = "../resources/poker.txt"
try:
    file = open(filename, "rt")
except Exception:
    import sys
    sys.exit("Opening %s failed" % filename)

for line in file:
    poker_competition.deal_cards(line.split())
    poker_competition.determine_winner()

print("wins %s: %s" % (floor.get_name(), floor.get_wins()))
print("wins %s: %s" % (freek.get_name(), freek.get_wins()))
