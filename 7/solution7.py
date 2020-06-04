def is_prime(i):
    return len([x for x in range(2,round(i/2)+1) if i % x == 0 and i != x]) == 0


x = 1
number_of_primes = 0
while number_of_primes != 10001:
    x += 1
    if is_prime(x):
        number_of_primes += 1
print(x)

# print([x for x in range(1,20) if is_prime(x)])
