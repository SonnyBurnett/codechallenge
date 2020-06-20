import time
from classes.Game import Game


def count_first_wins(player_id, lines):
    games = map(Game, lines)
    player_one_wins_count = sum(1 for g in games if g.get_winning_player_id() == player_id)
    return player_one_wins_count


def main():
    start = time.time()

    input_file = open('euler054.txt', 'r')

    lines = input_file.readlines()
    result = count_first_wins(0, lines)

    end = time.time()
    print(f'Result: {result}')
    print(f'Duration: {end - start}')


if __name__ == '__main__':
    main()
