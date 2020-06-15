import unittest
from p54 import Poker, OneRound, PlayerHand


class test_p54(unittest.TestCase):
  def test_OneRound(self):
    _one_round = OneRound('5C QC QH AS TS 4S 6S 4C 5H JS')
    self.assertTrue(_one_round.did_player1_win())

  def test_sum_of_winnings(self):
    _hands = '''5H 5C 6S 7S KD 2C 3S 8S 8D TD
      5D 8C 9S JS AC 2C 5C 7D 8S QH
      2D 9C AS AH AC 3D 6D 7D TD QD
      4D 6S 9H QH QC 3D 6D 7H QD QS
      2H 2D 4C 4D 4S 3C 3D 3S 9S 9D
      2H 2D 4C 4D AH 2C 2S 4H 4S KD
      TH TD 4C 4D 3H TC TS 4H 4S 7D'''
    poker = Poker(poker_hands=_hands)
    self.assertEqual(poker.player1_wins, 4)

  def test_card_value(self):
    _player_hand = PlayerHand('5C QC QH AS TS')
    self.assertEqual(_player_hand._PlayerHand__get_card_value('Q'), 12)
    self.assertEqual(_player_hand._values, [5, 12, 12, 14, 10])
    self.assertEqual(_player_hand._colors, ['C', 'C', 'H', 'S', 'S'])
    self.assertEqual(_player_hand._duplicates, [12])

  def test_card_wrong_value(self):
    # test wrong input
    self.assertRaises(ValueError, PlayerHand, '5C XC QH AS TS')
    self.assertRaises(ValueError, PlayerHand, '5C QC QH AS')
    self.assertRaises(ValueError, PlayerHand, '5CQCQHASTS')

  def test_fail_to_load_file(self):
    file_name = 'not_existing_file.txt'
    self.assertRaises(FileNotFoundError, Poker, file_name)

  def test_euler(self):
    poker = Poker()
    self.assertEqual(poker.euler_solution(), 376)
