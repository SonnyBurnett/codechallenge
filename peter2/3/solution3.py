def isprime(i):
    if len([x for x in range(2,i) if i % (x) == 0 and i != x]) == 0:
        return True
    else:
        return False
# Only check for odd numbers if prime
primelist = [i for i in range(1,40000, 2) if isprime(i)]
print(max([z for z in primelist if 600851475143 % z == 0]))
