import unittest
from itertools import cycle
from .p059 import CipherDecoder


class Test_p059(unittest.TestCase):
  def test_euler(self):
    _cipher = CipherDecoder()
    temp = _cipher.euler_solution()
    self.assertEqual(temp, 129448)

  def test_euler_with_simple_dictionary_no_match(self):
    _cipher = CipherDecoder(complex_dictionary=False)
    temp = _cipher.euler_solution()
    self.assertNotEqual(temp, 129448)

  def test_euler_with_simple_dictionary_working(self):
    _cipher = CipherDecoder(complex_dictionary=False, minimum_match_percentage=69)
    temp = _cipher.euler_solution()
    self.assertEqual(temp, 129448)

  def test_simple(self):
    _cipher = CipherDecoder(minimum_words_to_find=2)
    key = 'dam'
    data = 'Hello world is going strong!'
    encoded_data = ','.join(str(ord(x) ^ ord(y)) for (x, y) in zip(data, cycle(key)))
    output = _cipher.decode_data(encoded_data)
    self.assertEqual(output, data)

  def test_too_simple_no_match(self):
    _cipher = CipherDecoder(minimum_words_to_find=1, minimum_match_percentage=50)
    key = 'bob'
    data = 'Hello world!'
    encoded_data = ','.join(str(ord(x) ^ ord(y)) for (x, y) in zip(data, cycle(key)))
    output = _cipher.decode_data(encoded_data)
    self.assertNotEqual(output, data)
