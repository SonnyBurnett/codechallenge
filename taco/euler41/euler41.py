import sympy
from itertools import permutations


def make_string_from_digits(n):
    return "".join(map(str, [x for x in range(1, n+1)]))


def get_max_prime_from_permutations(n):
    return max([int(x) if sympy.isprime(int(x)) else -1 for x in list(map("".join, permutations(n)))])


def main():
    print(max([get_max_prime_from_permutations(make_string_from_digits(q)) for q in range(2, 10)]))


if __name__ == '__main__':
    main()

