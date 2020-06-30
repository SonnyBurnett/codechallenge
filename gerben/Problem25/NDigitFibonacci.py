def calculate_first_to_n_fibonacci(n: int):
  if not 0<n<10000:
    raise ValueError("Input should be an integer between 0 and 10.000")
  a, b, index = 0, 1, 0
  while len(str(a))<n:
    index+=1
    a, b = b, a + b
  return index

def main():
  print("The index of the first Fibonacci number with 1000 digits is: " +
    str(calculate_first_to_n_fibonacci(1000)))

if __name__ == '__main__':
    main()