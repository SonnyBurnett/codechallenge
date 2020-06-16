from math import sqrt, hypot
from typing import List

def __calculate_product(triplet: List[int]):
  x=1
  for i in triplet:
         x *= i
  if not sum(triplet)==0:
    return x
  else:
    return 0

def SpecialTriplet(x: int):
  if not 0<x<10000:
    raise ValueError("input should be an integer between 1 and 10000")
  return next(([int(a),int(b),int(hypot(a,b))] for a in range(1,x+1) for b in range(1,x+1)
    if a+b+hypot(a,b)==x), [])

def main():
  spT=SpecialTriplet(1000)
  print("The product of the special Pythagorean triplet "+str(spT)+" equals "+
    str(__calculate_product(spT)))

if __name__ == '__main__':
    main()