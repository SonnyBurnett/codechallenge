from PokerGame.pokerhand import PokerHand


class Player:
    def __init__(self, name):
        self.__nr_wins = 0
        self.__nr_losts = 0
        self.__poker_hand = None
        self.__name = name

    def get_name(self):
        return self.__name

    def set_hand(self, cards):
        self.__poker_hand = PokerHand(cards)

    def get_poker_hand(self):
        return self.__poker_hand

    def get_wins(self):
        return self.__nr_wins

    def add_win(self):
        self.__nr_wins += 1

    def get_lost(self):
        return self.__nr_losts

    def add_losts(self):
        self.__nr_losts += 1
