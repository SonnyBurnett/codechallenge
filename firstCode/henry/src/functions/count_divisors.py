from functions import find_prime_factors as functions


def count_divisors_naive(value):
    divisors_count = 0

    for divisor in range(1, value+1):
        if value % divisor == 0:
            divisors_count += 1

    return divisors_count


def count_divisors_reduced_by_pairs(value):
    result = 0
    lower_search_bound = 1
    upper_search_bound = value // 2

    while lower_search_bound < upper_search_bound:
        if value % lower_search_bound == 0:
            upper_search_bound = value / lower_search_bound

            if lower_search_bound * lower_search_bound == value:
                result += 1
            else:
                result += 2

        lower_search_bound += 1

    return result


def count_divisors_reduced_by_primes(value):
    dict_prime_to_count = functions.find_prime_factors(value)

    number_of_prime_combinations = 1
    for prime in dict_prime_to_count:
        number_of_prime_combinations *= (1 + dict_prime_to_count[prime])

    return number_of_prime_combinations
