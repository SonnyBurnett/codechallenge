# Python3 program to count distinct  
# divisors of a given number n 
  
def SieveOfEratosthenes(n, prime,primesquare, a): 
    # Create a boolean array "prime[0..n]"  
    # and initialize all entries it as  
    # true. A value in prime[i] will finally  
    # be false if i is not a prime, else true. 
    for i in range(2,n+1): 
        prime[i] = True
  
    # Create a boolean array "primesquare[0..n*n+1]" 
    # and initialize all entries it as false.  
    # A value in squareprime[i] will finally be  
    # true if i is square of prime, else false. 
    for i in range((n * n + 1)+1): 
        primesquare[i] = False
  
    # 1 is not a prime number 
    prime[1] = False
  
    p = 2
    while(p * p <= n): 
        # If prime[p] is not changed,  
        # then it is a prime 
        if (prime[p] == True): 
            # Update all multiples of p 
            i = p * 2 
            while(i <= n): 
                prime[i] = False
                i += p 
        p+=1
      
  
    j = 0
    for p in range(2,n+1):  
        if (prime[p]==True):  
            # Storing primes in an array 
            a[j] = p 
  
            # Update value in primesquare[p*p], 
            # if p is prime. 
            primesquare[p * p] = True
            j+=1
  
# Function to count divisors 
def countDivisors(n): 
    # If number is 1, then it will 
    # have only 1 as a factor. So, 
    # total factors will be 1. 
    if (n == 1): 
        return 1
  
    prime = [False]*(n + 2) 
    primesquare = [False]*(n * n + 2) 
      
    # for storing primes upto n 
    a = [0]*n 
  
    # Calling SieveOfEratosthenes to  
    # store prime factors of n and to  
    # store square of prime factors of n 
    SieveOfEratosthenes(n, prime, primesquare, a) 
  
    # ans will contain total 
    # number of distinct divisors 
    ans = 1
  
    # Loop for counting factors of n 
    i=0
    while(1):  
        # a[i] is not less than cube root n 
        if(a[i] * a[i] * a[i] > n): 
            break
  
        # Calculating power of a[i] in n. 
        cnt = 1 # cnt is power of  
                # prime a[i] in n. 
        while (n % a[i] == 0): # if a[i] is a factor of n 
            n = n / a[i] 
            cnt = cnt + 1 # incrementing power 
  
        # Calculating number of divisors 
        # If n = a^p * b^q then total  
        # divisors of n are (p+1)*(q+1) 
        ans = ans * cnt 
        i+=1
  
    # if a[i] is greater than 
    # cube root of n 
      
    n=int(n) 
    # First case 
    if (prime[n]==True): 
        ans = ans * 2
  
    # Second case 
    elif (primesquare[n]==True): 
        ans = ans * 3
  
    # Third casse 
    elif (n != 1): 
        ans = ans * 4
  
    return ans # Total divisors 
  
# Driver Code 
if __name__=='__main__': 
    print("Total distinct divisors of 100 are :",countDivisors(100)) 
  
# This code is contributed 
# by mits 