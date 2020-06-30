import itertools, math

def is_prime(n):
  if n % 2 == 0 and n > 2: 
    return False
  for i in range(3, int(math.sqrt(n)) + 1, 2):
    if n % i == 0:
      return False
  return True

for a in list(map("".join, itertools.permutations( list("7654321") ))):
  if is_prime(int(a)):
    print(a) 
    break