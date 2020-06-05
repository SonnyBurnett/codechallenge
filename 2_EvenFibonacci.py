total=0
fib1=1
fib2=2
fibonacci=[fib1,fib2]
evens=[fib2]
while fib1+fib2<4000000:
#while fib<4000:
  fib_new=fib1+fib2
  fib1=fib2
  fib2=fib_new
  fibonacci.append(fib_new)
  if(fib_new%2==0):
    evens.append(fib_new)

#print(fibonacci)
print(sum(evens))