'''
https://projecteuler.net/problem=19

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
from datetime import date


class Days():
  def __init__(self):
    self.__first_monday = 0

  @staticmethod
  def get_number_of_days_in_range(day_to_return: int, starting_date: date, ending_date: date) -> int:
    if not isinstance(day_to_return, int):
      raise TypeError('Expected integer between 1 and 7, representing a day in the week')
    if day_to_return < 1 or day_to_return > 8:
      raise ValueError('Expected integer between 1 and 7, representing a day in the week')
    if not isinstance(starting_date, date) or not isinstance(ending_date, date):
      TypeError('Starting and ending date are expected as a date types')
    if starting_date > ending_date:
      ValueError('Starting date must be before the ending date and not before the year 1900.')
    if starting_date.year < 1900 or ending_date.year < 1900:
      ValueError('Starting date must be before the ending date and not before the year 1900.')

    return len([1 for x in range(starting_date.year, ending_date.year + 1) for y in range(1, 13) if date(x, y, 1).isoweekday() == day_to_return])

  @staticmethod
  def euler_solution():
    return Days.get_number_of_days_in_range(7, date(1901, 1, 1), date(2000, 12, 31))


def main():
  '''
  main function
  '''
  print('Solution for the Euler 019 problem:')
  # prints: 171
  print(Days.euler_solution())


if __name__ == "__main__":
  main()
