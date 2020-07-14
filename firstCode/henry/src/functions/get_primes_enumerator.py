primes = [2, 3]


def is_next_prime_given_existing_primes(candidate_prime):
    for prime in primes:
        if candidate_prime % prime == 0:
            return False

    return True


def add_prime():
    candidate_prime = primes[-1] + 1

    while True:
        if is_next_prime_given_existing_primes(candidate_prime):
            primes.append(candidate_prime)
            return

        candidate_prime += 1


def get_primes_enumerator():
    i = 0

    while True:
        if len(primes) <= i:
            add_prime()

        yield primes[i]
        i += 1
