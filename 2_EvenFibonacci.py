def calculate_fibonacci(max):
  fib1=1
  fib2=2
  fibonacci=[fib1,fib2]
  while fib1+fib2<max:
    fib_new=fib1+fib2
    fib1=fib2
    fib2=fib_new
    fibonacci.append(fib_new)
  return(fibonacci)

def evens_from_list(MixedList):
  evensList=[x for x in MixedList if x % 2 == 0]
  return(evensList)

fibonacci=calculate_fibonacci(4000000)
evens = evens_from_list(fibonacci)

print("The sum of all evens in the list of Fibonacci numbers below 4 million equals "
  + str(sum(evens)))