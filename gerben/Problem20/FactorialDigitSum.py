from math import factorial

def calculate_digit_sum(x: int):
  if not 0<x:
    raise ValueError("input should be a positive integer")
  return sum([int(str(x)[i]) for i in range(len(str(x)))])

def main():
  print("The sum of all digits in the 100 factorial is: "
    + str(calculate_digit_sum(factorial(100))))

if __name__ == '__main__':
    main()