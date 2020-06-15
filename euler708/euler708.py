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


print(buildprimeslist(50,[2]))

