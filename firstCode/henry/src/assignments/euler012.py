import sys
import time

sys.path.append('../')
from functions import count_divisors as functions

def main():
    target = 500
    index = 1
    value = 1
    divisors = 0

    start = time.time()

    while divisors < target:
        index += 1
        value += index
        divisors = functions.count_divisors_reduced_by_primes(value)

    end = time.time()

    print(f'Triangle index: {index}')
    print(f'Triangle number: {value}')
    print(f'Duration: {end - start} seconds')

if __name__ == '__main__':
    main()