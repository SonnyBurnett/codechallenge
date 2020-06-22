import math
import time


def is_integer_palindrome(number):
    old_number = number
    reverse_number = 0
    digits = len(str(number))
    for i in range(digits):
        dividor = 10**(digits - 1 - i)
        reverse_number += math.floor(old_number / dividor) * (10**(digits-1))/dividor
        old_number = old_number % dividor

    return number == reverse_number


def find_largest_palindrome(max_digit):
    for i in range(10**max_digit, 1, -1):
        for k in range(10**max_digit, 1, -1):
            number = i * k
            if is_integer_palindrome(number):
                return number

    return None


if __name__ == "__main__":
    start_time = time.time()
    print(find_largest_palindrome(3))

    print(time.time() - start_time)
