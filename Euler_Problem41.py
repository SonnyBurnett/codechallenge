import itertools
import math

def test_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

prime_list = []
for i in range(2,10):
    list1 = [item for item in itertools.permutations(range(1,i+1), i)]
    list2 = list(itertools.chain(*list1))
    number = ''.join(map(str,list2))


    for y in range(0,(len(number) - (i-1)),i):
        prime = int(number[y:y+i])
        if test_prime(prime) == True:
            prime_list.append(prime)

print("Largest n-digit pandigital prime is " + str(max(prime_list)))

if 2143 in prime_list:
    print ("Test is success!")
else:
    print("Test failed!")
