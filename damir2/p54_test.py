import unittest
import p54

class Test_p54(unittest.TestCase):
  def test_Hand(self):
    _hand = p54.Hand('5C QC QH AS TS 4S 6S 4C 5H JS')
    self.assertTrue(_hand.did_player1_win())

  def test_sum_of_winnings(self):
    