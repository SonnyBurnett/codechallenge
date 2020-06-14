from collections import defaultdict

from pokerhand import PokerHand


class Player:
    def __init__(self, name):
        self.nr_wins = 0
        self.nr_losts = 0
        self.poker_hand = None
        self.name = name

    def get_name(self):
        return self.name

    def set_hand(self, cards):
        self.poker_hand = PokerHand(cards)

    def get_poker_hand(self):
        return self.poker_hand

    def get_wins(self):
        return self.nr_wins

    def add_win(self):
        self.nr_wins += 1

    def get_lost(self):
        return self.nr_losts

    def add_losts(self):
        self.nr_losts += 1
