import sys
import unittest

sys.path.append('../')

from classes.Game import Game


class TestPreprovidedTestCases(unittest.TestCase):
    def example1(self):
        game = Game("5H 5C 6S 7S KD 2C 3S 8S 8D TD")

        actual_winner = game.get_winning_player_id()

        self.assertEqual(1, actual_winner)

    def example2(self):
        game = Game("5D 8C 9S JS AC 2C 5C 7D 8S QH")

        actual_winner = game.get_winning_player_id()

        self.assertEqual(0, actual_winner)

    def example3(self):
        game = Game("2D 9C AS AH AC 3D 6D 7D TD QD")

        actual_winner = game.get_winning_player_id()

        self.assertEqual(1, actual_winner)

    def example4(self):
        game = Game("4D 6S 9H QH QC 3D 6D 7H QD QS")

        actual_winner = game.get_winning_player_id()

        self.assertEqual(0, actual_winner)

    def example5(self):
        game = Game("2H 2D 4C 4D 4S 3C 3D 3S 9S 9D")

        actual_winner = game.get_winning_player_id()

        self.assertEqual(0, actual_winner)


class TestGameWithTwoPlayers(unittest.TestCase):
    def test_pair_wins_over_high_card(self):
        game = Game("3H 3C 4H 6H 5H 3D 7D 4D 6C TD")

        actual_winner = game.get_winning_player_id()

        self.assertEqual(0, actual_winner)

    def test_two_pair_wins_over_pair(self):
        game = Game("3H 3C 4H 6H 5H TD 7D 7D 6C TD")

        actual_winner = game.get_winning_player_id()

        self.assertEqual(1, actual_winner)

    def test_three_of_a_kind_wins_over_pair(self):
        game = Game("3H 3C 4H 6H 5H 7D 7D 7D 6C TD")

        actual_winner = game.get_winning_player_id()

        self.assertEqual(1, actual_winner)

    def test_straight_wins_over_three_of_a_kind(self):
        game = Game("3H 7C 4H 6H 5H 7D 7D 7D 6C TD")

        actual_winner = game.get_winning_player_id()

        self.assertEqual(0, actual_winner)

    def test_flush_wins_over_straight(self):
        game = Game("3H 7C 4H 6H 5H 7S 7S 7S 6S TS")

        actual_winner = game.get_winning_player_id()

        self.assertEqual(1, actual_winner)

    def test_full_house_wins_over_flush(self):
        game = Game("3H 3C 3H 6H 6H 7S 7S 7S 6S TS")

        actual_winner = game.get_winning_player_id()

        self.assertEqual(0, actual_winner)

    def test_four_of_a_kind_wins_over_full_house(self):
        game = Game("3H 3C 3H 3H 6H 7S 7S 7S 6S 6S")

        actual_winner = game.get_winning_player_id()

        self.assertEqual(0, actual_winner)

    def test_straight_flush_wins_over_four_of_a_kind(self):
        game = Game("3H 3C 3H 3H 6H 7S 8S 9S TS JS")

        actual_winner = game.get_winning_player_id()

        self.assertEqual(1, actual_winner)

    def test_high_pair_wins(self):
        game = Game("5H 5C 6H 8H TH 4S 4S 6C TS JS")

        actual_winner = game.get_winning_player_id()

        self.assertEqual(0, actual_winner)

    def test_high_card_wins_equal_pairs(self):
        game = Game("5H 5C 6H 8H TH 5S 5S 6C TS JS")

        actual_winner = game.get_winning_player_id()

        self.assertEqual(1, actual_winner)


class TestGameWithThreePlayers(unittest.TestCase):
    def test_pair_wins(self):
        game = Game("3H 3C 4H 6H 5H 3D 7D 4D 6C TD 5S 8S TS AS 2C")

        actual_winner = game.get_winning_player_id()

        self.assertEqual(0, actual_winner)


class TestGameWithTenPlayers(unittest.TestCase):
    def test_pair_wins(self):
        game = Game("3H 3C 4H 6H 5H 3D 7D 4D 6C TD 5S 8S TS AS 2C 5S 8S TS AS 2C 5S 8S TS AS 2C 5S 8S TS AS 2C 5S 8S "
                    "TS AS 2C 5S 8S TS AS 2C 5S 8S TS AS 2C 5S 8S TS AS 2C")

        actual_winner = game.get_winning_player_id()

        self.assertEqual(0, actual_winner)


if __name__ == '__main__':
    unittest.main()
