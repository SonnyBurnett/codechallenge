import unittest
from .p017 import Number


class Test_p017(unittest.TestCase):
  def test(self):
    _num = Number()
    _word = _num.translate_number_to_word(769)
    self.assertEqual(_word, 'seven hundred and sixty-nine')
    _word = _num.translate_number_to_word(16)
    self.assertEqual(_word, 'sixteen')
    _word = _num.translate_number_to_word(3)
    self.assertEqual(_word, 'three')
    _word = _num.translate_number_to_word(24)
    self.assertEqual(_word, 'twenty-four')
    _word = _num.translate_number_to_word(101)
    self.assertEqual(_word, 'one hundred and one')
    _word = _num.translate_number_to_word(900)
    self.assertEqual(_word, 'nine hundred')
    _word = _num.translate_number_to_word(1000)
    self.assertEqual(_word, 'one thousand')

  def test_euler(self):
    _num = Number()
    _word_count = _num.euler()
    self.assertEqual(_word_count, 21124)
