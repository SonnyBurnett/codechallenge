import unittest
from .p015 import Grid


class Test_p015(unittest.TestCase):
  def test_cases(self):
    grid = Grid()
    self.assertEqual(grid.calculate_grid_routes(3, 3), 20)
    self.assertEqual(grid.calculate_grid_routes(2, 2), 6)
    self.assertEqual(grid.calculate_grid_routes(1, 1), 2)

  def test_euler(self):
    grid = Grid()
    self.assertEqual(grid.euler_solution(), 137846528820)

  def test_exceptions(self):
    grid = Grid()
    self.assertRaises(TypeError, grid.calculate_grid_routes, '2', 2)
    self.assertRaises(ValueError, grid.calculate_grid_routes, -1, 2)
    self.assertRaises(ValueError, grid.calculate_grid_routes, 4, 0)
    self.assertRaises(TypeError, grid.calculate_grid_routes, '0', '2')
    self.assertRaises(ValueError, grid.calculate_grid_routes, -1, 2)
