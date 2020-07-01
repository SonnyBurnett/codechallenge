
# Highly divisible triangular number

## Problem approach

1. Factorize into primes
2. Count how many times the primes (not counting 1 to the set of primes) occur, e.g. `28 = 2^2 * 7^1`.
   Now, every divisor is any combination of none to all of those primes. That gives a possible number of combinations
   equal to the product of the times the different primes occur plus 1.
   In the case of `28` (`= 2 * 2 * 7`), this is `(2 + 1) * (1 + 1) = 6`.
   In the case of `21` (`= 3 * 7`): `(1 + 1) * (1 + 1) = 4`.
   In the case of `3` (`= 3`): `(1 + 1) = 2`.

Some things have been done for efficiency:

- Divisors are calculated only for triangle numbers, not all numbers in a more naive loop
- Not all divisors are identified. Instead, it suffices to only determine the amount of divisors
- In the class `FactorCache`, some state is kept to not recalcalate primes of the same number. So, if we already calculated the factors of 28, and later on we need to calculate them for 56, we actually make use of the fact that we know the factors of 28, 14, 7 and 2. This leads to a factor 3 of efficiency only, so for lower numbers, we might as well have left it out.

## Execution result

    The first triangle number with over 500 divisors is 76576500
    python solution.py  1.31s user 0.01s system 99% cpu 1.326 total
