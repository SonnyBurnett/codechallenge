import numpy as np

def multiples(big_amount, divlist):
  if type(big_amount) != int:
    raise TypeError("big_amount should be of type integer")
  if big_amount<=1:
    raise ValueError("big_amount should be a positive integer larger than 1")
  if type(divlist) != list:
    raise TypeError("divlist should be of type list")
  if len(divlist) <= 1:
    raise ValueError("divlist should contain more than 1 integers")
  if not all(isinstance(x, int) for x in divlist):
    raise TypeError("only positive integers larger than 1 are allowed in this list")
  if not all(x>1 for x in divlist):
    raise ValueError("only positive integers larger than 1 are allowed in this list")

  divisors=[]
  [[ divisors.append(i) for j in divlist if i%j==0 ] for i in range(1,big_amount) ]
  return np.unique(divisors)

def main():
  result=multiples(1000,[3,5])
  #print(divisors)
  print("The sum of all multiples of 3 and 5 below 1000 is: " + str(sum(result)))

if __name__ == '__main__':
    main()