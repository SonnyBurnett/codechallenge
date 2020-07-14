''' Score: 6.5
    Run  0.5 Not the fastest solution... but still works
    NamesOK 1.    Really clear names...
    Linted 1
    Libraries list / 1  For loop nice. Would like to see a list comprehension / filter but this was ok
    SingleResponsibility/2   Really nice. Once of the best decompositions
    Deepsource/1
    Testing 0/3
Bonus 1 point: really clear, really nice layout: seriously well done
  
  
Score 5/10
  
'''

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
