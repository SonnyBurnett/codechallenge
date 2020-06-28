import sys
import unittest

sys.path.append('../')

from classes.GameRunner import GameRunner


class TestGameRunner(unittest.TestCase):
    def test_run_on_example(self):
        game_runner = GameRunner('../test_hii.txt')

        game_result = game_runner.run()

        self.assertEqual(2, game_result.win_count[1])
        self.assertEqual(3, game_result.win_count[0])


if __name__ == '__main__':
    unittest.main()
