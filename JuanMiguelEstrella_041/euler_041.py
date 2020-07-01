from functools import reduce


def get_factors(n):

    if n == 0:
        return 0

    ## this is the "mid point" factor of a number. if n = 25, the midpoint is 5 (1,5,5,25). stop there.
    midpoint = int(n**0.5)

    ## loops through 1 to midpoint, if n % factor == 0 then it means it is a divisor
    ## we get that and also the n//factor
    list_of_factors = ([factor, n//factor] for factor in range(1, midpoint+1) if n % factor == 0)

    ## we combine all list_of_factors
    total_factors = reduce((lambda a, b: a+b), list_of_factors)

    return total_factors


def is_prime(n):
    if n == 1:
        return False

    factors = get_factors(n)
    if len(factors) > 2:
        return False
    else:
        return True

def is_digits_unique(n):
    found_flag = [False, False, False, False, False, False, False, False, False, False]
    for c in str(n):
        if found_flag[int(c)]:
            return False
        else:
            found_flag[int(c)] = True

    return True


## we can already reduce our iteration by knowing that 987654321 and 87654321 are divisible by 3 therefore not primes
for x in reversed(range(2, 7654322)):
    if '0' in str(x) or '8' in str(x) or '9' in str(x):
        continue
    if not is_digits_unique(x):
        continue
    if is_prime(x):
        print(x)
        break
