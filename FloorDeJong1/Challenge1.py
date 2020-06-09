import math


def find_nr_of_factors(number):
    sqrt = math.sqrt(number)
    nr_divisors = 0
    for i in range(1, int(sqrt)):
        if number % i == 0:
            if i == sqrt:
                nr_divisors += 1  # 1 factor if sqrt
            else:
                nr_divisors += 2  # 2 factors if you find 1 (2*4 = 8 so both 2 and 4 are divisors of 8)

    return nr_divisors


def find_triangle_with_nr_factors(max_factors):
    triangle_number = 0
    found_nr = False
    i = 1
    while not found_nr:
        triangle_number += i
        i += 1

        if find_nr_of_factors(triangle_number) >= max_factors:
            return triangle_number


print(find_triangle_with_nr_factors(500))
