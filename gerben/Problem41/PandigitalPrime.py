from itertools import permutations

def __isPrime(n: int):
  if n<=3:
    return n > 1
  if n%2==0 or n%3==0:
    return False

  i=5
  while i*i<=n:
    if n%i==0 or n%(i+2)==0:
      return False
    i+=6

  return True

def __generator(digits: str):
    generator=list(permutations(digits))
    for i in generator:
      yield ''.join(i)

def calculate_pandigital_prime(n):
  if not 0<n<10:
    raise ValueError("Input should be an integer between 0 and 10")
  digits=''.join([str(x) for x in range(n,0,-1)])
  for _ in range(len(digits)):
    for i in __generator(digits):
      if __isPrime(int(i)):
        return(i)
    digits=digits[1:]
  return 'not found in this range'

def main():
  print("The largest pandigital prime is: " + calculate_pandigital_prime(9))

if __name__ == '__main__':
    main()