def fetch_number_of_divisors(x):
    return len([i for i in range(1,21) if x % i == 0])

for x in range(0, 10000000000, 20):
    divisors = fetch_number_of_divisors(x)
    if divisors == 20:
        print("We found {}".format(x))