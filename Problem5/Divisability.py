from math import factorial

def divisability(c: int):
  if not 1<c<25:
    raise ValueError("input must be an integer between 1 and 25")
  div=[]
  maxc=int(factorial(c))
  next(div.append(x) for x in range(c,maxc+1,c) if all(x%i==0 for i in range(1,c+1)))
  return min(div)

def main():
  print("The smallest possible number that is divisable by all the numbers up to "+str(20)+" is: "+
    str(divisability(20)) )

if __name__ == '__main__':
    main()