import time
from classes.GameRunner import GameRunner


def main():
    start = time.time()

    game_runner = GameRunner('euler054.txt')
    game_result = game_runner.run()

    end = time.time()

    print(f'Player one win count: {game_result.win_count[0]}')
    print(f'Duration: {end - start}')


if __name__ == '__main__':
    main()
