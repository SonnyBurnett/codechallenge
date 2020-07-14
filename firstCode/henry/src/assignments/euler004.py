import sys
import time

sys.path.append('../')
from functions import find_prime_factors as functions

def ceiling_division(dividend, divisior):
    return -(-dividend // divisior)

def is_palindrome(value):
    text = str(value)
    length = len(text)

    for index in range(0, ceiling_division(length, 2)):
        if text[index] != text[length - 1 - index]:
            return False

    return True


def main():
    start = time.time()

    largest_palindrome = 0

    for left in range(999, 1, -1):
        for right in range(left, 1, -1):
            value = left * right

            if value < largest_palindrome:
                break;

            if is_palindrome(value):
                largest_palindrome = value

    end = time.time()
    print(f'Largest palindrome = {largest_palindrome}')
    print(f'Duration: {end - start} seconds')


if __name__ == '__main__':
    main()