'''
https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all
starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''


class Collatz():
  '''
  Class for Collatz sequence
  '''

  def __init__(self):
    self.__collatz_dict = {}

  def __calculate_Collatz_seq_length(self, n: int) -> int:
    if n == 1:
      return 1
    if n in self.__collatz_dict:
      return self.__collatz_dict[n]
    if (n % 2) == 0:
      self.__collatz_dict[n] = 1 + self.__calculate_Collatz_seq_length(int(n / 2))
    else:
      self.__collatz_dict[n] = 2 + self.__calculate_Collatz_seq_length(int((3 * n + 1) / 2))

    return self.__collatz_dict[n]

  def get_starting_num_with_longest_Collatz(self, max_starting_number: int = 100) -> int:
    if not isinstance(max_starting_number, int):
      raise TypeError('Expected positve integer vaule')
    if max_starting_number < 1:
      raise ValueError('Expected positve integer vaule')
    for x in range(int(max_starting_number / 2), max_starting_number):
      self.__calculate_Collatz_seq_length(x)
    return max(self.__collatz_dict, key=self.__collatz_dict.get)


def main():
  '''
  main function
  '''
  print('Solution for the Euler 014 problem:')
  _collatz = Collatz()
  x = _collatz.get_starting_num_with_longest_Collatz(max_starting_number=1000000)
  print('Longest chain is for a number: {}'.format(x))


if __name__ == "__main__":
  main()
