def isprime(i):
    if len([x for x in range(2,i) if i % (x) == 0 and i != x]) == 0:
        return True
    else:
        return False

def create_triangle_number_list(max_triangle_number):
    triangle_number_list = [1]
    for addition in range(2, max_triangle_number):
        triangle_number_list.append(triangle_number_list[len(triangle_number_list)-1]+addition)
    return triangle_number_list

def number_of_divisors(triangle_number):
    return len([divisor for divisor in range(1,round(triangle_number/2)+1) if triangle_number % divisor == 0])

for triangle_nr in create_triangle_number_list(1000000):
    if not isprime(triangle_nr):
        divisors = number_of_divisors(triangle_nr)
        print("Triangle nr: {}".format(triangle_nr))
        print("Number of divisors: {}".format(divisors))
        if divisors > 200:
            print("\t found at: {}".format(triangle_nr))
            print("\t Number of divisors: {}".format(divisors))