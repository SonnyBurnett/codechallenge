'''
https://projecteuler.net/problem=15

Starting in the top left corner of a 2×2 grid, and only being able to
move to the right and down, there are exactly 6 routes to the bottom
right corner.

How many such routes are there through a 20×20 grid?
'''
from typing import Any, Dict


class Grid():
  def __init__(self):
    self.__matrix: Dict[Any, int] = {(0, 0): 1}

  def __is_coordinate_in_range(self, x, y, max_x, max_y):
    if x < 0 or x > max_x:
      return False
    if y < 0 or y > max_y:
      return False
    return True

  def calculate_grid_routes(self, max_x: int, max_y: int) -> int:
    if not isinstance(max_x, int) or not isinstance(max_y, int):
      raise TypeError('Grid size is in postive integers larger than 1.')
    if max_x < 1 or max_y < 1:
      raise ValueError('Grid size is in postive integers larger than 1.')
    for x in range(max_x + 1):
      for y in range(max_y + 1):
        if x == 0 and y == 0:
          continue
        combinations_left = 0
        combinations_top = 0
        if self.__is_coordinate_in_range(x - 1, y, max_x, max_y):
          combinations_left = self.__matrix[(x - 1, y)]
        if self.__is_coordinate_in_range(x, y - 1, max_x, max_y):
          combinations_top = self.__matrix[(x, y - 1)]
        self.__matrix[(x, y)] = combinations_left + combinations_top
    return self.__matrix[(x, y)]

  def euler_solution(self) -> int:
    return self.calculate_grid_routes(20, 20)


def main():
  '''
  main function
  '''
  _grid = Grid()
  print('Solution for the Euler 015 problem:')
  # prints: 137846528820
  print(_grid.euler_solution())


if __name__ == "__main__":
  main()
