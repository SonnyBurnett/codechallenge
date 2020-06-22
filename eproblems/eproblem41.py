from eproblem12 import prime_factors
from itertools import permutations
from functools import reduce
import argparse


def convert(set_in):
    """Converts a set into an integer number from left to right.

    :param set_in: set of integers
    :return: integer representing the set.
    """
    return reduce(lambda tens, ones: tens * 10 + ones, set_in)


def last_prime(list_in):
    """Returns the last prime from the list_in argument.
    This method is rescuing the prime_factors method from eproblem12 :)

    :param list_in: a list of all permutation sets from low to high.
    :return: first prime number from the end of the list or it is 1.
    """
    for i in range(len(list_in) - 1, 0, -1):
        if len(prime_factors(convert(list_in[i]))) == 3:
            return convert(list_in[i])

    return 1


def eproblem41(n_digit):
    """Set the boundary for the current Euler exercise and to kick off the calculation.
    TODO: reuse the problem 1 sum_total to calculate the sums mod % 3 for the suited permutations (way over the top :) )

    :param n_digit: number of digits of the length of the number and highest digit value.
    :return: the highest prime of n-digits containing numbers below or equal to n.
    """
    a_list = [(1,)]
    if n_digit >= 4:
        a_list += list(permutations(range(1, 5), 4))
    if n_digit >= 5:
        a_list += list(permutations(range(1, 6), 5))
    if n_digit >= 7:
        a_list += list(permutations(range(1, 8), 7))
    if n_digit > 9:
        return "Not implemented above n-digit 9!"

    return last_prime(a_list)


def main():
    """"Main is the interactive method start of the second project Euler problem,
        reasoning is documented in the '../notebooks/Project Euler Problem 41.ipynb' notebook.
        This method is anti pattern, but used for the interactive guided demonstration of the Notebooks.

    """
    n_digit: int = int(input("Search for pandigital below n_digit digits: "))
    print("Largest n-digit pandigital prime is: ", eproblem41(n_digit))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_digit", "-n", help="Search for pandigital below n_digit digits")
    args = parser.parse_args()

    if not isinstance(args.n_digit, type(None)):
        eproblem41(args.n_digit)
    else:
        main()
