def __isEven(max):
  if max%2==0:
    return True
  else:
    return False

def __next_prime(max):
  for i in range(3,max,2):
    if max%i==0:
      return i
  return max

def get_prime_factors(max):
  if type(max) != int:
    raise TypeError("max should be of type integer")
  if max<=0:
    raise ValueError("max should be a positive integer")

  orig_max=max
  primes=[]
  p=1

  even=__isEven(max)
  while even==True:
    max=int(max/2)
    primes.append(2)
    even=__isEven(max)
  while p<max:
    p=__next_prime(max)
    max=int(max/p)
    primes.append(p)

  return primes

def main():
  max=600851475143
  print("The prime factors of "+str(max)+" are: "+str(get_prime_factors(max)))

if __name__ == '__main__':
    main()