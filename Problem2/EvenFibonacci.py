def calculate_fibonacci(max: int):
  if max<=1:
    raise ValueError("max should be a positive integer larger than 1")

  fib1=1
  fib2=2
  fibonacci=[fib1,fib2]
  while fib1+fib2<max:
    fib_new=fib1+fib2
    fib1=fib2
    fib2=fib_new
    fibonacci.append(fib_new)
  return(fibonacci)

def __evens_from_list(MixedList):
  evensList=[x for x in MixedList if x % 2 == 0]
  return(evensList)

def main():
  fibonacci=calculate_fibonacci(4000000)
  evens = __evens_from_list(fibonacci)

  print("The sum of all evens in the list of Fibonacci numbers below 4 million equals "
    + str(sum(evens)))

if __name__ == '__main__':
    main()