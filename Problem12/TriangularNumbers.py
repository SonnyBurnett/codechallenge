import math
from itertools import chain

def __number_of_factors(triangular: int):
  return len(list(chain.from_iterable((i,triangular/i) for i in range(2,int(math.sqrt(triangular))+1)
    if triangular%i == 0)))+2

def triangular_exceeding_divisors(maximum: int):
  if not 0<maximum<750:
    raise ValueError("input must be an integer between 0 and 750")
  triangular=1
  triangular_factors=0
  counter=0
  while triangular_factors<maximum:
    counter += 1
    triangular += counter +1
    triangular_factors=__number_of_factors(triangular)
  return triangular

def main():
  print("The lowest triangular number with more than 500 divisors is: "+ str(triangular_exceeding_divisors(500)))

if __name__ == '__main__':
    main()