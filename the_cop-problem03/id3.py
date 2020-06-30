#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
def get_prim(i):
    return_list = []
    for x in range(1,i):
        for y in range(2,x):
            if (x%y) == 0:
                break
        else:
           return_list.append(x)
    return return_list 
  

def get_prim_factors(i):
    prim_list = get_prim(10000)
    factors = []
    n = 1
    while i != 0:
        if int(i) in prim_list:
            factors.append(int(i))
            break
        if (i % prim_list[n]) == 0:
            i = (i / prim_list[n])
            factors.append(prim_list[n])
            n=1
        else:
            n = n + 1
            if n >= len(prim_list):
                print("Could not calculate factors with this prim list. Heighten the max factor on get_prim.")
                break
    return factors

if __name__ == "__main__":
    print(get_prim_factors(600851475143))
    pass
    