def __isEven(limit):
  if limit%2==0:
    return True
  return False

def __next_prime(limit):
  for i in range(3,limit,2):
    if limit%i==0:
      return i
  return limit

def get_prime_factors(limit: int):
  if limit<=0:
    raise ValueError("input should be a positive integer")

  primes=[]
  p=1

  even=__isEven(limit)
  while even:
    limit=int(limit/2)
    primes.append(2)
    even=__isEven(limit)
  while p<limit:
    p=__next_prime(limit)
    limit=int(limit/p)
    primes.append(p)

  return primes

def main():
  c=600851475143
  print("The largest prime factor of "+str(c)+" is: "+str(max(get_prime_factors(c))))

if __name__ == '__main__':
    main()