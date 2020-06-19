from Game.PokerGame.competition import PokerCompetition
from Game.PokerGame.player import Player

floor = Player("Floor")
freek = Player("Freek")

poker_competition = PokerCompetition()
poker_competition.add_player(floor)
poker_competition.add_player(freek)

cards_royal_flush = "AD JD 10D QD KD "
cards_straight_flush = "4D 8D 5D 7D 6D "
cards_four_of_a_kind = "4D 4S 4C QD 4H "
cards_full_house = "4D JD 4S 4C JH "
cards_full_house2 = "4D 8D 4S 4C 8H "
cards_flush = "2D JD 4D 10D AD "
cards_straight = "2D 6S 4D 5H 3C "
cards_three_of_a_kind = "2D 6S 4D 6H 6C "
cards_two_pairs = "2D 6S 4D 2H 6C "
cards_pair = "2D 6S 5D QH 6C "
cards_pair2 = "3D 6S 5D QH 6C "
cards_high_card = "2D QS 4D 9H 6C "

# # 2 Royal flush
# cards = (cards_royal_flush + cards_royal_flush).split()
# poker_competition.deal_cards(cards)
# winner = poker_competition.determine_winner()
# print(winner.get_name())
# print(floor.get_name(), ":", floor.get_wins())
# print(freek.get_name(), ":", freek.get_wins())

# # Royal flush, Four of a kind
# cards = (cards_royal_flush + cards_four_of_a_kind).split()
# poker_competition.deal_cards(cards)
# winner = poker_competition.determine_winner()
# print(winner.get_name())
# print(floor.get_name(), ":", floor.get_wins())
# print(freek.get_name(), ":", freek.get_wins())

# # Royal flush, Four of a kind
# cards = (cards_four_of_a_kind + cards_royal_flush).split()
# poker_competition.deal_cards(cards)
# winner = poker_competition.determine_winner()
# print(winner.get_name())
# print(floor.get_name(), ":", floor.get_wins())
# print(freek.get_name(), ":", freek.get_wins())

# # three of a kind, full house
# cards = (cards_three_of_a_kind + cards_full_house).split()
# poker_competition.deal_cards(cards)
# winner = poker_competition.determine_winner()
# print(winner.get_name())
# print(floor.get_name(), ":", floor.get_wins())
# print(freek.get_name(), ":", freek.get_wins())

# # 2 full house
# cards = (cards_full_house + cards_full_house2).split()
# poker_competition.deal_cards(cards)
# winner = poker_competition.determine_winner()
# print(winner.get_name())
# print(floor.get_name(), ":", floor.get_wins())
# print(freek.get_name(), ":", freek.get_wins())

# # same pair
# cards = (cards_pair + cards_pair2).split()
# poker_competition.deal_cards(cards)
# winner = poker_competition.determine_winner()
# print(winner.get_name())
# print(floor.get_name(), ":", floor.get_wins())
# print(freek.get_name(), ":", freek.get_wins())

# Test examples of euler
cards = ["5H 5C 6S 7S KD 2C 3S 8S 8D TD",
         "5D 8C 9S JS AC 2C 5C 7D 8S QH",
         "2D 9C AS AH AC 3D 6D 7D TD QD",
         "4D 6S 9D QH QC 3D 6D 7H QD QS",
         "2H 2D 4C 4D 4S 3C 3D 3S 9S 9D"]

for player_cards in cards:
    poker_competition.deal_cards(player_cards.split())
    winner = poker_competition.determine_winner()
    print("%s hand: %s with %s" %(floor.get_name(), floor.get_poker_hand().get_hand(), floor.get_poker_hand().get_hand_value()))
    print("%s hand: %s with %s" %(freek.get_name(), freek.get_poker_hand().get_hand(), freek.get_poker_hand().get_hand_value()))
    print(winner.get_name())

print(floor.get_name(), ":", floor.get_wins())
print(freek.get_name(), ":", freek.get_wins())
