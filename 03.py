'''
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

#function to get all prime factors of a number
def _calc_prime_factors(number):
  ret = []
  if (None == number or number < 2):
    return ret
  for x in range(2, number + 1):
    while (number % x == 0):
      ret.append(x)
      number = int(number / x)
      if (number == 1):
        #reached the end of the divisions, no need to loop further
        return ret
  return ret

print(max(_calc_prime_factors(600851475143)))
