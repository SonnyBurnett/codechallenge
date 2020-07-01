# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

def get_prim_division(i):
    return_list = []
    for x in range(1,i):
        for y in range(2,x):
            if (x%y) == 0:
                break
        else:
           return_list.append(x)
    return return_list 

def get_prim_sieve_of_eratosthenes(i):
    return_list = []
    sieve = [True] * i
    for n in range(2,i):
        if sieve[n]:
            return_list.append(n)
            for x in range(n*n, i, n):
                sieve[x] = False
    return return_list


if __name__ == "__main__":
    my_list = get_prim_sieve_of_eratosthenes(2000000)
    print(sum(my_list))