''' The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ? '''

def buildprimeslist(endrange, primesList):
    primes = primesList
    for n in range(2,endrange):
        #print("Test this number" + str(n))
        if n not in primes:
            #print("Not in primeslist")
            #Try figuring out if it is a prime number
            #1. Divide it by itself, if it is divisible without a remainder then go to 2
            #2. Divide it by other prime numbers, if it is divisible by any prime number then it is not a prime number
            # if it is was not possible to divide it  by any of prime numbers then it is a prime number.
            if n % n == 0:
                #print("Divisible by itself: " + str(n))
                for p in primes:
                #if a number has no remainder from a prime
                    pr = True  
                    if pr:    
                        if n % p == 0:
                            #print(str(n) + " - not a prime, divisible by: " + str(p))
                            pr = False
                            break
                        #else:
                            #print("Not divisible by a prime. " + str(p))

                if pr is True:
                    #print("Add {prime} to primes".format(prime = n))
                    primes.append(n)
            #else:
                #print("Not devisible by itself " + str(n))

    return(primes)


def primeFactor(num,plist):
    outn = 0
    for n in plist:
        if num != n:
            if num % n == 0:
                print(f'{num} is devisable by {n} prime factor')
                num /= n
                outn = n
                break
        else:
            outn = n
            break
                
    if num - outn != 0: 
        primeFactor(num,plist)
    else: 
        print(f'Highest prime factor is {num}')

num = 600851475143
plist = buildprimeslist(10000,[2])

primeFactor(num,plist)