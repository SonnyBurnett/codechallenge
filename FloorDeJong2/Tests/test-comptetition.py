import unittest
from unittest import mock

from PokerGame.competition import PokerCompetition
import PokerGame.player
from PokerGame.player import Player
import PokerGame.pokerhand as ph


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

    @mock.patch("PokerGame.pokerhand.PokerHand.get_highest_card")
    def test_determineWinnerViaHighestCard(self, mock_hand_highest_card):
        mock_hand_highest_card.side_effect = [11, 13, 9, 8, 8, 6, 3, 6, 2, 5]
        winner = self.poker_competition.determine_winner_via_highest_card(self.player_one, self.player_two, 1)
        self.assertEqual(winner, self.player_two)

        mock_hand_highest_card.side_effect = [11, 11, 9, 8, 8, 6, 3, 6, 2, 5]
        winner = self.poker_competition.determine_winner_via_highest_card(self.player_one, self.player_two, 1)
        self.assertEqual(winner, self.player_one)

        mock_hand_highest_card.side_effect = [11, 11, 9, 9, 6, 6, 3, 3, 2, 5]
        winner = self.poker_competition.determine_winner_via_highest_card(self.player_one, self.player_two, 1)
        self.assertEqual(winner, self.player_two)

        mock_hand_highest_card.side_effect = [11, 11, 9, 9, 6, 6, 3, 3, 2, 5]
        with self.assertRaises(SystemExit) as se:
            self.poker_competition.determine_winner_via_highest_card(self.player_one, self.player_two, 6)

        self.assertEqual(se.exception.args[0], "Tied - Both have all the same values in cards")

    @mock.patch("PokerGame.pokerhand.PokerHand.get_hand_value")
    def test_determineWinnerViaCardValue(self, mock_get_hand_value):
        mock_get_hand_value.side_effect = [[7], [12]]
        winner = self.poker_competition.determine_winner_via_card_value(self.player_one, self.player_two, 0)
        print(winner.get_name())
        self.assertEqual(winner, self.player_two)

        mock_get_hand_value.side_effect = [[7, 9], [12, 6]]
        winner = self.poker_competition.determine_winner_via_card_value(self.player_one, self.player_two, 0)
        self.assertEqual(winner, self.player_two)

        mock_get_hand_value.side_effect = [[7, 6], [7, 2], [7, 6], [7, 2]]
        winner = self.poker_competition.determine_winner_via_card_value(self.player_one, self.player_two, 0)
        self.assertEqual(winner, self.player_one)

    @mock.patch("PokerGame.competition.determine_winner_via_highest_card")
    @mock.patch("PokerGame.competition.determine_winner_via_card_value")
    def test_determineWinnerSameHand(self, mock_highest_card, mock_card_value):
        mock_highest_card.return_value = self.player_one
        mock_card_value.return_value = self.player_one

        self.assertEqual(self.poker_competition.determine_winner_same_hand(self.player_one, self.player_two, 1), self.player_one)


