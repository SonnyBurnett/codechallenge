def is_prime(i):
    return len([x for x in range(2,round(i**0.5)+1) if i % x == 0 and i != x]) == 0

prime_list = [x for x in range(2,2000000) if is_prime(x)]
print("Sum = {}".format(sum(prime_list)))