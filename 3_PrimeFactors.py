def prime(max):
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
while p<max:
  p=prime(max)
  max=int(max/p)
  primes.append(p)

print("The prime factors of "+str(orig_max)+" are: "+str(primes))