from itertools import permutations

def calculate_xth_permutation(number: int):
  if not 0<number<10**8:
    raise ValueError("input should be a positive integer below 100 million")
  digits='0123456789'
  generator=list(permutations(digits))
  for count, i in enumerate(generator,1):
    if count==number:
      return ''.join(i)

def main():
  print("The 1 millionth lexicographic permutation of the digits 0..9 is: " +
    calculate_xth_permutation(1000000))

if __name__ == '__main__':
    main()