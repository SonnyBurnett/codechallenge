def calculate_digit_sum(x: int):
  if not 0<x:
    raise ValueError("input should be a positive integer")
  return sum([int(str(x)[i]) for i in range(len(str(x)))])

def main():
  print("The sum of all digits in the number 2 to the power 1000 is: "
    + str(calculate_digit_sum(2**1000)))

if __name__ == '__main__':
    main()