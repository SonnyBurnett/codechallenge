import math


def prime_factors(number):
    """Compute a list of the prime factors of a given number.
    Method assumes that number is larger or equal to 0.

    :param number: this is the number that will be factorised into prime factors.
    :return: list of prime factors.
    """
    original = number
    prime_list = [1]

    while number % 2 == 0:
        prime_list.append(2)
        number = number * 0.5

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            prime_list.append(int(i))
            number = number / i

    if number > 2:
        prime_list.append(int(number))

    # Ensure that for 0 and 1 there is no duplicate
    if original != 1:
        prime_list.append(int(original))

    return prime_list


def tot_dividers(list_div):
    """Calculate the total number of dividers based on a prime factor powers dictionary.

    :param list_div: A prime factor dictionary.
    :return: Number of total dividers.
    """
    list_helper = []
    result = 1

    for key in list_div:
        list_helper.append(list_div[key])

    for x in range(1, len(list_helper) - 1):
        result = result * (list_helper[x] + 1)

    return result


def dict_prime_factors(prime_list):
    """Generate a dictionary of the a prime factor list.
    
    :param prime_list: A prime factor list possibly containing same prime factors.
    :return: The dictionary for the count of the prime factors

            (equivalent to the power of the prime factor).
    """
    return {index: prime_list.count(index) for index in prime_list}


def main():
    """"Main method of the twelfth project Euler problem,
        reason1ing is documented in the '../notebooks/Project Euler Problem 12.ipynb' notebook.

    """
    target: int = int(input("Calculate below: "))
    max_dividers: int = int(input("Minimal number of dividers: "))

    max_factor = 0

    for i in range(1, target):
        i = int(i * (i + 1) * 0.5)  # Trick to speed up to the next Triangle number
        factors = prime_factors(i)
        powers = dict_prime_factors(factors)
        dividers = tot_dividers(powers)

        if max_factor < dividers:
            print("Triangle: ", i, " ", end='')
            print("Factors: ", factors, " ", end='')
            print("Powers: ", powers, " ", end='')
            print("Dividers: ", str(dividers))
            max_factor = dividers

        if max_factor > max_dividers:
            break


if __name__ == "__main__":
    main()
