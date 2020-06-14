from typing import List

def __next_prime(primes: List[int]):
  i=primes[-1]+2
  while not all(i%j!=0 for j in primes):
    i+=2
  return i

def __calculate_sum(list_to_sum: List[int]):
  x=0
  for i in list_to_sum:
         x += i
  return x

def calculate_primes(c: int):
  if not 3<c<10000000:
    raise ValueError("input must be an integer between 3 and 10.000.000")
  primes=([2,3])
  while primes[-1]<c:
    primes.append(__next_prime(primes))
  return primes[:-1]

def main():
  print("The sum of all primes below 2.000.000 is: " + str(__calculate_sum(calculate_primes(2000000))))

if __name__ == '__main__':
    main()