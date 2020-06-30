from itertools import chain
from math import sqrt

def __list_of_divisors(inp: int):
  l = list(chain.from_iterable((i,inp/i) for i in range(2,int(sqrt(inp))+1) if inp%i == 0))
  l.append(1)
  s = {int(x) for x in l}
  return list(s)

def sum_of_amicable_numbers(maximum: int):
  if not 0<maximum<1000000:
    raise ValueError("Input should be an integer between 0 and 1.000.000")
  amicable_numbers=[]
  for x in range(2,maximum+1):
    f=sum(__list_of_divisors(x))
    if x==sum(__list_of_divisors(f)) and x!=f:
      amicable_numbers.append(x)
  return sum(amicable_numbers)

def main():
  print("The sum of all amicable numbers below 10.000 is: " + str(sum_of_amicable_numbers(10000)))

if __name__ == '__main__':
    main()

