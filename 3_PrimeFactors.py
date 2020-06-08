def isEven(max):
  '''
  This function reports if the input is even.
  One argument is accepted, and it should be an integer.
  '''
  if max%2==0:
    return True
  else:
    return False

def next_prime(max):
  '''
  This function calculates the first prime factor for the input.
  One argument is accepted, and it should be an integer.
  '''
  for i in range(3,max,2):
    if max%i==0:
      return i
  return max

p=1
max=600851475143
orig_max=max
primes=[]

even=isEven(max)
while even==True:
  max=int(max/2)
  primes.append(2)
  even=isEven(max)
while p<max:
  p=next_prime(max)
  max=int(max/p)
  primes.append(p)

print("The prime factors of "+str(orig_max)+" are: "+str(primes))