import math


def determine_factors(number):
    factors = []
    for i in range(2, int(number/2)+1):
        if number % i == 0:
            factors.append(i)
    return factors


def find_smallest_number_divisible_by_range(max_dividor):
    divisible_by_range = False

    number = max_dividor
    while not divisible_by_range:
        factors = determine_factors(number)
        # print(number, factors)
        if all(elem in factors for elem in range(1, max_dividor + 1)):
            return number

        number += 1

        # if number == 12:
        #     break



if __name__ == "__main__":
    print(determine_factors(10))
    find_smallest_number_divisible_by_range(10)
    # list1 = ['Hi',  'hello', 'at', 'this', 'there', 'from']
    # list2 = ['there', 'hello', 'Hi', 'Floor']
    # result = all(elem in list1 for elem in list2)
    # print(result)
