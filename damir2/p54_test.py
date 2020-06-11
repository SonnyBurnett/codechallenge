import unittest
import p54

class Test_p54(unittest.TestCase):
  def test_Hand(self):
    _hand = p54.Hand('5C QC QH AS TS 4S 6S 4C 5H JS')
    self.assertTrue(_hand.did_player1_win())

  def test_sum_of_winnings(self):
    _hands = '''5H 5C 6S 7S KD 2C 3S 8S 8D TD
      5D 8C 9S JS AC 2C 5C 7D 8S QH
      2D 9C AS AH AC 3D 6D 7D TD QD
      4D 6S 9H QH QC 3D 6D 7H QD QS
      2H 2D 4C 4D 4S 3C 3D 3S 9S 9D'''
    poker = p54.Poker(poker_hands = _hands)
    self.assertEqual(poker.player1_wins, 3)

  def test_card_value(self):
    _player_hand = p54.PlayerHand('5C QC QH AS TS')
    self.assertEqual(_player_hand._PlayerHand__get_card_value('Q'), 12)
    self.assertEqual(_player_hand._values, [5, 12, 12, 14, 10])
    self.assertEqual(_player_hand._colors, ['C', 'C', 'H', 'S', 'S'])
    self.assertEqual(_player_hand._duplicates, [12])

  def test_load_file(self):
    file_name = 'not_existing_file.txt'
    self.assertRaises(FileNotFoundError, p54.Poker(file_name))
    file_name = 'p54-poker.txt'

  def test_euler(self):
    poker = p54.Poker()
    self.assertEqual(poker.euler_solution(), 376)