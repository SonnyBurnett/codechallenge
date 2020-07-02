import re
from decimal import Decimal, getcontext

def longest_reciprocal_cycle(n: int):
  if not 0<n<10000:
    raise ValueError("input should be an integer between 0 and 10.000")
  getcontext().prec=1
  maximum=1
  while maximum/getcontext().prec>.4:
    getcontext().prec*=50
    regex = re.compile(r'(.+?.+?)(\1)')
    for x in range(1,n,2):
      fraction=Decimal(1)/Decimal(x)
      match = regex.search(str(fraction))
      if match:
        mg1=match.group(1)
        if not mg1==len(mg1)*mg1[0]:
          if len(mg1)>maximum:
            xmax,mgmax,maximum=x,mg1,len(mg1)
  return xmax

def main():
  xmax=longest_reciprocal_cycle(1000)
  print("The largest reciprocal cycle in the unit fractions below 1000 is in 1 divided by " + str(xmax))

if __name__ == '__main__':
    main()
