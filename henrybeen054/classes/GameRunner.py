import collections
from classes.Game import Game


class GameResult:
    def __init__(self, win_count):
        self.win_count = win_count


class GameRunner:
    def __init__(self, file_name):
        self.file_name = file_name

    def run(self):
        input_file = open('euler054.txt', 'r')
        lines = input_file.readlines()

        games = map(Game, lines)

        winners = map(lambda g: g.get_winning_player_id(), games)
        win_count = collections.Counter(winners)

        return GameResult(win_count)

