import math

def num_divisors(triangle):
    divisors = 2
    i = 2

    triangleroot = math.sqrt(triangle)
    while i < triangleroot:
        if (triangle%i) == 0:
            divisors += 2
        i += 1

    if i==triangleroot:
        return divisors+1
    else:
        return divisors
        
triangle_num = 1
total_divisors = 0
n_divisors = 1
found=False

while not found:
    while total_divisors < 500:
        triangle_num += 1
        nplus1_divisors = num_divisors(triangle_num)
        total_divisors = n_divisors*nplus1_divisors
        n_divisors = nplus1_divisors
    check = (triangle_num-1)*triangle_num/2

    if num_divisors(check) > 500:
        found = True
    else:
        total_divisors = 0

print(int(check))
