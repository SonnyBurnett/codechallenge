import sys
import time

sys.path.append('../')
from functions import find_prime_factors as functions


def main():
    target = 600851475143

    dict_of_prime_factor_to_count = functions.find_prime_factors(target)
    max_prime_factor = max(dict_of_prime_factor_to_count.keys())

    print(f'Maximum prime factor = {max_prime_factor}')

if __name__ == '__main__':
    main()