def is_prime(number):
    if number < 2:
        prime = False
    elif number == 2:
        prime = True
    else:
        for i in range(2, number):
            if number % i == 0:
                prime = False
                break
            else:
                prime = True
    return prime


def calculate_pandigital_prime(pandigital_n_limit=9):
    from itertools import permutations
    largest_pandigital_prime = None
    possible_keys = generate_possible_permutation_keys(pandigital_n_limit)
    for key in possible_keys:
        if largest_pandigital_prime:
            break
        pandigital_numbers = permutations(key)
        for number in pandigital_numbers:
            number_as_integer = int("".join(number))
            if is_prime(number_as_integer):
                largest_pandigital_prime = number_as_integer
                break
    return largest_pandigital_prime


def generate_possible_permutation_keys(limit):
    longest_key = "".join([str(limit-i) for i in range(limit)])
    possible_keys = [longest_key[i:] for i in range(limit)]
    return possible_keys

