import unittest
from unittest import mock

from Game.PokerGame.competition import PokerCompetition
from Game.PokerGame.player import Player
import Game.PokerGame.pokerhand


class TestCompetition(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.poker_competition = PokerCompetition("Poker League")
        cls.player_one = Player("Floor")
        cls.player_two = Player("Freek")

    # @mock.patch("PokerGame.player.Player")
    # def test_addPlayer2(self, mock_player):
    #     player_one = PokerGame.player.Player()
    #     player_two = PokerGame.player.Player()
    #     self.poker_competition.add_player(player_one)
    #     self.poker_competition.add_player(player_two)
    #
    #     self.assertEqual(self.poker_competition.return_player_list()[0], player_one)
    #     self.assertEqual(self.poker_competition.return_player_list()[0], player_two)

    def test_addPlayer(self):
        self.poker_competition.add_player(self.player_one)
        self.poker_competition.add_player(self.player_two)

        self.assertEqual(self.poker_competition.return_player_list()[0], self.player_one)
        self.assertEqual(self.poker_competition.return_player_list()[1], self.player_two)

    def test_dealCards(self):
        cards = ["8D", "JD", "TD", "9D", "7D", "4D", "JD", "2D", "7D", "KD"]
        self.poker_competition.deal_cards(cards)

        player_list = self.poker_competition.return_player_list()
        self.assertEqual(player_list[0].get_poker_hand().get_cards(), ["8D", "JD", "TD", "9D", "7D"])
        self.assertEqual(player_list[1].get_poker_hand().get_cards(), ["4D", "JD", "2D", "7D", "KD"])

    def test_detemineWinner_straightFlush_highCard(self):
        cards = ["8D", "JD", "TD", "9D", "7D", "4D", "JD", "2D", "7D", "KD"]
        self.poker_competition.deal_cards(cards)
        self.poker_competition.determine_winner()

        player_list = self.poker_competition.return_player_list()
        self.assertEqual(player_list[0].get_wins(), 1)
        self.assertEqual(player_list[1].get_wins(), 0)

        cards = ["8D", "JD", "TD", "9D", "7D", "AD", "JD", "TD", "QD", "KD"]
        self.poker_competition.deal_cards(cards)
        self.poker_competition.determine_winner()

        self.assertEqual(player_list[0].get_wins(), 1)
        self.assertEqual(player_list[1].get_wins(), 1)



    # @mock.patch("import Game.PokerGame.pokerhand.PokerHand.__gt__()")
    # def test_determineWinner(self, mock_hand_larger_then):
    #     mock_hand_larger_then.side_effect = [True, False]
    #
    #     self.poker_competition.determine_winner()
    #     self.assertEqual(self.player_one.get_wins(), 1)
        # self.assertEqual(self.player_two.get_wins(), 0)


