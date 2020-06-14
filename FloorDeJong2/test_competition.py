from Competition import Poker_Competition
from player import Player

floor = Player("Floor")
freek = Player("Freek")

poker_competition = Poker_Competition()
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
cards_pair = "2D 6S 4D AH 6C "
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

# 2 full house --> wrong
cards = (cards_full_house + cards_full_house2).split()
poker_competition.deal_cards(cards)
winner = poker_competition.determine_winner()
print(winner.get_name())
print(floor.get_name(), ":", floor.get_wins())
print(freek.get_name(), ":", freek.get_wins())
