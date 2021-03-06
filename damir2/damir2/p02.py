'''
https://projecteuler.net/problem=2

Each new term in the Fibonacci sequence is generated by adding
the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values
do not exceed four million, find the sum of the even-valued terms.
'''


def __fibonacci_generator_up_to_a_limit(limit):
  if type(limit) != int:
    raise TypeError("Only integer numbers allowed.")
  if limit < 1:
    raise ValueError("Only positive integer numbers allowed.")

  a, b = 0, 1
  while True:
    if a > limit:
      break
    yield a
    a, b = b, a + b


def sum_fibonacci_with_limit_and_mod_number(limit=4000000, mod=1):
  if type(mod) != int:
    raise TypeError("mod should be a positive integer.")
  if mod < 1:
    raise ValueError("mod should be positive integer greater than zero.")

  return sum([x for x in __fibonacci_generator_up_to_a_limit(limit) if x % mod == 0])


def main():
  limit = 4000000
  mod = 2
  print('Solution for the Euler 002 problem:')
  # prints: 4613732
  print(sum_fibonacci_with_limit_and_mod_number(limit, mod))


if __name__ == "__main__":
    main()
