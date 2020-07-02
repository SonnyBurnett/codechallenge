'''
https://projecteuler.net/problem=59

Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to
ASCII, then XOR each byte with a given value, taken from a secret key.
The advantage with the XOR function is that using the same encryption key
on the cipher text, restores the plain text; for example,
65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and
without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified
method is to use a password as a key. If the password is shorter than the
message, which is likely, the key is repeated cyclically throughout the
message. The balance for this method is using a sufficiently long password
key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower
case characters. Using p059_cipher.txt
(right click and 'Save Link/Target As...'), a file containing the encrypted
ASCII codes, and the knowledge that the plain text must contain common
English words, decrypt the message and find the sum of the ASCII values
in the original text.
'''
import os
import string
import re
from itertools import cycle, product


class CipherDecoder():
  def __init__(self,
               minimum_match_percentage: int = 95,
               minimum_words_to_find: int = 5,
               minimum_length_word: int = 3,
               minimum_confidence_factor: int = 65,
               complex_dictionary=True):
    if not isinstance(minimum_match_percentage, int) \
       or not isinstance(minimum_words_to_find, int) \
       or not isinstance(minimum_length_word, int) \
       or not isinstance(minimum_confidence_factor, int):
      raise TypeError('Minimum values expected as positive integeters.')
    if minimum_match_percentage < 50 or minimum_match_percentage > 100:
      ValueError('minimum_match_percentage expected in range from 50 till 100.')
    if minimum_words_to_find < 1:
      ValueError('minimum_words_to_find expected to be positive integer.')
    if minimum_length_word < 1:
      ValueError('minimum_length_words expected to be positive integer.')
    if minimum_confidence_factor < 30 or minimum_confidence_factor > 100:
      ValueError('minimum_confidence_factor expected in range from 30 till 100.')

    self.__location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    self.__cipher = ''
    self.__english_dictionary = self.__load_file('p059_words_alpha.txt') if complex_dictionary else self.__load_file('p059_words_3000_most_common.txt')
    self.__password_letters = string.ascii_lowercase
    self.__minimum_match_percentage = minimum_match_percentage / 100
    self.__minimum_words_to_find = minimum_words_to_find
    self.__minimum_length_word = minimum_length_word
    self.__minimum_confidence_factor = minimum_confidence_factor / 100

  def __load_file(self, filename: str) -> str:
    if not isinstance(filename, str):
      raise TypeError('Expected filename as a string.')
    if not os.path.exists(os.path.join(self.__location, filename)):
      raise FileNotFoundError("File specified does not exists.")

    content = ''
    with open(os.path.join(self.__location, filename)) as file:
      content = file.read()

    return content

  def decode_file_message(self, filename: str) -> int:
    data = self.__load_file(filename)
    return self.decode_data(data)

  def decode_data(self, data: str):
    if not isinstance(data, str):
      raise TypeError('Expecting a non-empty string.')
    if len(data) == 0:
      raise TypeError('Expecting a non-empty string.')

    for key in product([c for c in self.__password_letters], repeat=3):
      decoded_data = ''.join(chr(int(x) ^ ord(y)) for (x, y) in zip(data.split(','), cycle(key)))
      all_words = list(re.findall(r'\b(\w{' + str(self.__minimum_length_word) + r',})\b', decoded_data))
      potential_words = list(re.findall(r'(?:(?=^)|(?<=[,.\s]))([a-zA-Z]{' + str(self.__minimum_length_word) + r',})(?=\b)', decoded_data))

      if len(potential_words) >= self.__minimum_words_to_find and \
         len(potential_words) / len(all_words) >= self.__minimum_confidence_factor:
        matched_words = [all_words[x].lower() in self.__english_dictionary for x in range(len(all_words))]
        sum_of_matched_english_words = sum([1 for x in matched_words if x is True])

        if sum_of_matched_english_words / len(all_words) > self.__minimum_match_percentage:
          return decoded_data

    return ''

  @staticmethod
  def sum_ascii_codes(data: str):
    if not isinstance(data, str):
      raise TypeError('Expecting a non-empty string.')

    if len(data) == 0:
      return None

    return sum([ord(x) for x in data])

  def euler_solution(self):
    return CipherDecoder.sum_ascii_codes(self.decode_file_message('p059_cipher.txt'))


def main():
  '''
  main function
  '''
  _cipher = CipherDecoder()
  print('Solution for the Euler 059 problem:')
  # prints: 129448
  print(_cipher.euler_solution())


if __name__ == "__main__":
  main()
