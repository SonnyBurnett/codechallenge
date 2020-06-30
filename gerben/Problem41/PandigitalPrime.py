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

def calculate_pandigital_prime():
  digits='987654321'
  for _ in range(len(digits)):
    generator=list(permutations(digits))
    for i in generator:
      if __isPrime(int(''.join(i))):
        return(''.join(i))
    digits=digits[1:]

def main():
  print("The largest pandigital prime is: " + calculate_pandigital_prime())

if __name__ == '__main__':
    main()