from typing import List

def __next_prime(primes: List[int]):
  i=max(primes)+2
  while not all(i%j!=0 for j in primes):
    i+=2
  return i

def calculate_primes(c: int):
  if not 3<c<100000:
    raise ValueError("input must be an integer between 3 and 100.000")
  primes=([2,3])
  while len(primes)<c:
    primes.append(__next_prime(primes))
  return primes[-1]

def main():
  print("The 10.001st prime is: " + str(calculate_primes(10001)))

if __name__ == '__main__':
    main()