# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
#  For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?


from itertools import permutations

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def fast_prime_verification(test_number):
    if test_number % 2 != 0:
        if (test_number+1) % 6 == 0 or (test_number-1) % 6 == 0:
            if is_prime(test_number):
                return True
    return False

if __name__ == "__main__":
    test_number=123456789
    test_number_length=len(str(test_number))
    prime=False
    while True:
        # get permutations of input number.
        test_number_list = permutations(str(test_number)[:test_number_length])
        # reverse list
        test_number_list = list(test_number_list)[::-1]
        for number in test_number_list:
            # test number list is now a list of tuples (see itertools.permutations)
            number=int(''.join(number))
            if fast_prime_verification(number):
                prime = number
                break
        test_number_length -= 1
        if prime:
            print(prime)
            break        
    pass