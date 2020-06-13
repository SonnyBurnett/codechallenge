from collections import defaultdict

from hand import Hand


class Player:
    def __init__(self, name):
        self.nr_wins = 0
        self.nr_losts = 0
        self.hand = None
        self.name = name

    def get_name(self):
        return self.name

    def set_hand(self, cards):
        self.hand = Hand(cards)

    def get_hand(self):
        return self.hand

    def get_wins(self):
        return self.nr_wins

    def add_win(self):
        self.nr_wins += 1

    def get_lost(self):
        return self.nr_losts

    def add_losts(self):
        self.nr_losts += 1
