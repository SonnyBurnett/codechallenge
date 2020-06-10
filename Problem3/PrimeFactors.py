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

def get_prime_factors(max: int):
  if max<=0:
    raise ValueError("input should be a positive integer")

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
  c=600851475143
  print("The largest prime factor of "+str(c)+" is: "+str(max(get_prime_factors(c))))

if __name__ == '__main__':
    main()