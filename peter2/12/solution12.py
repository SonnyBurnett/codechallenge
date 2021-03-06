def create_triangle_number_list(max_triangle_number):
    triangle_number_list = [1]
    for addition in range(2, max_triangle_number):
        triangle_number_list.append(triangle_number_list[len(triangle_number_list) - 1] + addition)
    return triangle_number_list


def number_of_divisors(number):
    # Only iterate till the square-root and multiple number of elements by 2
    # since a*b = b*a, added plus 1 for the small numbers
    return 2 * len([divisor for divisor in range(1, round(number**0.5)+1) if number % divisor == 0])


def print_and_stop_after_first_divisor_limit_found(number, divisor_limit):
    # Determine number of divisors
    no_divisors = number_of_divisors(number)
    if no_divisors > divisor_limit:
        print(number, no_divisors)
        exit(0)


# Iterate over the list of created Triangle numbers. for each Triangle number call the function to print
# the number of Divisors, given the limit.
[print_and_stop_after_first_divisor_limit_found(triangle_nr, 500) for triangle_nr in
 create_triangle_number_list(1000000)]
