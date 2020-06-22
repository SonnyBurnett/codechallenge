import math
import time


def determine_factors(number):
    factors = []
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            factors.append(i)
    return factors


def is_prime(number):
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            return False

    return True


def determine_max_prime_factor(number):
    factors = determine_factors(number)

    primes = []
    for factor in factors:
        if is_prime(factor):
            primes.append(factor)

    return max(primes)


if __name__ == "__main__":
    start_time = time.time()

    prime_factors = determine_max_prime_factor(600851475143)
    print(prime_factors)

    print("time", time.time() - start_time)
