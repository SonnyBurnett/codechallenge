from functions import get_primes_enumerator as functions


def find_prime_factors(value):
    result = {}
    remainder = value
    while remainder > 1:
        primes = functions.get_primes_enumerator()
        for candidatePrime in primes:
            if remainder % candidatePrime == 0:
                if candidatePrime in result:
                    result[candidatePrime] += 1
                else:
                    result[candidatePrime] = 1

                remainder /= candidatePrime
                break
    return result