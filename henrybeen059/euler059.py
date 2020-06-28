import time
from classes.EncryptionBreaker import EncryptionBreaker


def main():
    start = time.time()

    encryption_breaker = EncryptionBreaker('euler059.txt')
    solution = encryption_breaker.run()

    end = time.time()

    print(f'Solution key: {solution.get_key}')
    print(f'Solution text: {solution.get_text()}')
    print(f'Solution asci value: {solution.get_asci_value()}')
    print(f'Duration: {end - start}')


if __name__ == '__main__':
    main()
