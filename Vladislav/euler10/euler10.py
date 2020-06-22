
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import time




def buildprimeslist(endrange):
    primesDict = {}
    
    for n in range(2,endrange):
        #print("Test this number" + str(n))
        if n not in primesDict:
            #print("Not in primeslist")
            #Try figuring out if it is a prime number
            #1. Divide it by itself, if it is divisible without a remainder then go to 2
            #2. Divide it by other prime numbers, if it is divisible by any prime number then it is not a prime number
            # if it is was not possible to divide it  by any of prime numbers then it is a prime number.
            if n % n == 0:
                #print("Divisible by itself: " + str(n))
                pr = True  
                for p in primesDict:
                #if a number has no remainder from a prime
                   if pr:    
                        if n % p == 0:
                            #print(str(n) + " - not a prime, divisible by: " + str(p))
                            pr = False
                            break
                        #else:
                            #print("Not divisible by a prime. " + str(p))

                if pr is True:
                    #print("Add {prime} to primes".format(prime = n))
                    primesDict[n] = 1
            #else:
                #print("Not devisible by itself " + str(n))

    return(primesDict)


#print(buildprimeslist(100))

def isPrime(num):
    isPrime = True
    for y in range(2,num):
        if num % y == 0:
            isPrime = False

    return isPrime

def sumPrimes(to):
    total = 0
    for i in range(2, to):
        if isPrime(i):
            #print(f'Number {i} is a prime number')
            total += i
    print(total)

for i in range(1,3):
    start = time.time()
    sumPrimes(10^i)
    end = time.time()
    print(end-start)
