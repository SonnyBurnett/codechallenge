from itertools import chain, combinations
from math import sqrt

def __list_of_divisors(inp: int):
  l = list(chain.from_iterable((i,inp/i) for i in range(2,int(sqrt(inp))+1) if inp%i == 0))
  l.append(1)
  s = set((int(x) for x in l))
  return list(s)

def __isAbundant(n: int):
  if sum(__list_of_divisors(n))>n:
    return True
  return False

def __list_of_abundant_numbers(maximum: int):
  return [i for i in range(1,maximum) if __isAbundant(i)]

def main():
  maximum=28123
  lan=__list_of_abundant_numbers(maximum)
  list_of_sums=[h*2 for h in lan]
  generator=list(combinations(lan,2))
  for i in generator:
    list_of_sums.append(sum(i))
  list_of_no_sums=[j for j in range(1,maximum+1) if j not in list_of_sums]
  print("The sum of all integers that cannot be summed by two abundant numbers is: " +
    str(sum(list_of_no_sums)))

if __name__ == '__main__':
    main()