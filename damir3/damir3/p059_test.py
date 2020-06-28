import unittest
from itertools import cycle
from .p059 import Cipher


class Test_p059(unittest.TestCase):
  def test_euler(self):
    _cipher = Cipher()
    temp = _cipher.decode_file_message('p059_cipher.txt')
    self.assertEqual(temp, 129448)

  def test_simple_1(self):
    _cipher = Cipher(minimum_words_to_find=2)
    key = 'dam'
    data = 'Hello world is going strong!'
    encoded = ','.join(str(ord(x) ^ ord(y)) for (x, y) in zip(data, cycle(key)))
    output = _cipher.decode_data(encoded)
    self.assertEqual(output, data)

  def test_simple_2(self):
    _cipher = Cipher(minimum_words_to_find=1, minimum_match_percentage=50)
    key = 'bob'
    data = 'Hello world!'
    encoded = ','.join(str(ord(x) ^ ord(y)) for (x, y) in zip(data, cycle(key)))
    output = _cipher.decode_data(encoded)
    self.assertNotEqual(output, data)
