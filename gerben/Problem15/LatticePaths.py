#from numpy import binary_repr
from math import factorial

#def lattice_paths_strings(x: int, y: int):
#  return [binary_repr(i) for i in range(2**(x+y)) if binary_repr(i).count('1')==min(x,y)]

def lattice_paths(x: int, y: int):
  if not 0<x<100 or not 0<y<100:
    raise ValueError("input should be two integers between 0 and 100")
  return int(factorial(x+y)/(factorial(x)*factorial(y)))

def main():
  print("The number of Lattice paths in a 20x20 matrix is: " + str(lattice_paths(20,20)))

if __name__ == '__main__':
    main()