'''
https://projecteuler.net/problem=15

Starting in the top left corner of a 2×2 grid, and only being able to
move to the right and down, there are exactly 6 routes to the bottom
right corner.

How many such routes are there through a 20×20 grid?
'''
from typing import Any, List


class Grid():
  def __init__(self):
    self.__matrix: List[Any] = []

  def calculate_grid_routes(self, grid_x: int, grid_y: int) -> None:
    for x in range(grid_x):
      for y in range(grid_y):
        self.__matrix.append((x, y))
