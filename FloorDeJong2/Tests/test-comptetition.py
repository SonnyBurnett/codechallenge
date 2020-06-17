import unittest
from PokerGame.competition import PokerCompetition
from PokerGame.player import Player


class TestCompetition(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.poker_competition = PokerCompetition("Poker League")


    def test_addPlayer(self):
        player_one = Player("Floor")
        self.poker_competition.add_player(player_one)
        print(self.poker_competition.return_player_list())

