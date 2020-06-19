import unittest
from unittest import mock

from Game.PokerGame.competition import PokerCompetition
from Game.PokerGame.player import Player


class TestCompetition(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.poker_competition = PokerCompetition("Poker League")
        cls.player_one = Player("Floor")
        cls.player_two = Player("Freek")


    def test_addPlayer(self):
        self.poker_competition.add_player(self.player_one)
        self.poker_competition.add_player(self.player_two)

        self.assertEqual(self.poker_competition.return_player_list()[0], self.player_one)
        self.assertEqual(self.poker_competition.return_player_list()[1], self.player_two)

    def test_dealCards(self):
        cards = ["8D", "JD", "TD", "9D", "7D", "4D", "JD", "2D", "7D", "KD"]
        self.poker_competition.deal_cards(cards)
        self.assertEqual(self.player_one.get_poker_hand().get_cards(), ["8D", "JD", "TD", "9D", "7D"])
        self.assertEqual(self.player_two.get_poker_hand().get_cards(), ["4D", "JD", "2D", "7D", "KD"])

    @mock.patch("PokerGame.player.Player")
    def test_determineWinnerViaHighestCard(self, mock_player):
        mock_get_poker_hand.side_effect = [5, 6]
        result = self.poker_competition.determine_winner_via_highest_card()
        print(result)




