'''
https://projecteuler.net/problem=17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''


class Number():
  def __init__(self):
    self.single_digits = 'zero one two three four five six seven eight nine'.split()
    self.up_to_twenties = 'ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty'.split()
    self.doubles = 'doublezero ten twenty thirty forty fifty sixty seventy eighty ninety'.split()

  def __translate_singles_to_word(self, number: int) -> str:
    return self.single_digits[number]

  def __translate_doubles_to_word(self, number: int) -> str:
    if number > 20:
      if number % 10 == 0:
        return self.doubles[int(number / 10)]
      else:
        return self.doubles[int(number / 10)] + '-' + self.single_digits[number % 10]
    elif number >= 10:
      return (self.single_digits + self.up_to_twenties)[number]
    return self.__translate_singles_to_word(number % 10)

  def __translate_hundreds_to_word(self, number: int) -> str:
    if number >= 100:
      hundred = self.single_digits[int(number / 100)] + ' hundred'
      if number % 100 == 0:
        return hundred
      else:
        return hundred + ' and ' + self.__translate_doubles_to_word(number % 100)
    else:
      return self.__translate_doubles_to_word(number)
    return ''

  def translate_number_to_word(self, number: int) -> str:
    if not isinstance(number, int):
      raise TypeError('Positive integer expected larger than zero and smaller or equal 1000')
    if number < 1 or number > 1000:
      raise ValueError('Positive integer expected larger than zero and smaller or equal 1000')

    if number == 1000:
      return 'one thousand'

    words = self.__translate_hundreds_to_word(number)

    return words

  def euler(self):
    word_count = sum([len(self.translate_number_to_word(x).replace('-', '').replace(' ', '')) for x in range(1, 1001)])
    return word_count


def main():
  _num = Number()
  print('Solution for the Euler 017 problem:')
  print(_num.euler())


if __name__ == "__main__":
  main()
