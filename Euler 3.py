""""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.
5x7x13x29=13195
What is the largest prime factor of the number 600851475143 ?
"""

#Calculate largest prime factor

def create_list_prime_till_number(n):
    #Set variable of the function
    a = 2
    b = 0
    list = []
    #Loop till n
    while a < n:
        b = n / a
        # Is it a prime number
        if (b).is_integer():
            list.append(a)
            #print(list)
            sum = 1
            # Multiply prime factors = n
            for x in list:
                sum = x * sum
                #print(sum)
                if sum == n:
                    return x,list,n
        a = a + 1

#Calls the prime calculator function and prints the returned value

x,list,n = create_list_prime_till_number(600851475143)
print("Largest prime factor from " + str(n) + " is " + str(x) + " from prime factors " + str(list))

