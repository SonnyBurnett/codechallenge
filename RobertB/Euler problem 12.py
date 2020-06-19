import math

def num_divisors(number):
    """
    This function determines how many divisors a number has
    """
    divisors = 2
    i = 2

    number_root = math.sqrt(number)
    while i < number_root: #we don't need to go past the square root. 
        if (number%i) == 0:
            divisors += 2   # For every divisor, there is a counterpart above the square root
        i += 1

    if i==number_root:
        return divisors+1  # correct for the situation when the input is a perfect square. There is no counterpart in this situation 
    else:
        return divisors
        
triangle_num = 1
total_divisors = 0
n_divisors = 1
found=False

# triangle numbers can be written as n*(n+1)/2.
# N and N+1 do not share any divisors. This means that D(n*(n+1)) = D(n)*D(n+1)
# The factor 2 can spoil things though, so we need to check for that.
# For the next triangle number, D(n+1) can be reused as D(n)

while not found:
    while total_divisors < 500:  #if D(n*(n-1)) is not larger than 500, we do not have to check any further. Proceed to next triangle number
        triangle_num += 1
        nplus1_divisors = num_divisors(triangle_num)
        total_divisors = n_divisors*nplus1_divisors
        n_divisors = nplus1_divisors       #  reuse D(n+1) as D(n) to increase computation speed

    check = (triangle_num-1)*triangle_num/2   # we have found a candidate, check this number fully
    if num_divisors(check) > 500:
        found = True          # we are done, this is the result.
    else:
        total_divisors = 0    # proceed with next triangle number

print(int(check))  # produce a nice readable output
