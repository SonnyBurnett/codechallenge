import sympy
import itertools


def make_string_from_digits(n):
    return "".join(map(str, [x for x in range(1, n+1)]))


def make_num_from_list(lst):
    return int("".join(map(str, lst)))


def get_prime_permutations(s):
    return [make_num_from_list(p) for p in itertools.permutations(str(s), len(s)) if sympy.isprime(make_num_from_list(p))]


def get_max_num_from_list(ls):
    m = -1 if len(ls) < 1 else max(ls)
    return m


print(max(get_max_num_from_list([get_prime_permutations(make_string_from_digits(q)) for q in range(2, 10)]) ))
