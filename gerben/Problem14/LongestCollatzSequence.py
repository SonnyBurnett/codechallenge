def __Collatz_Even(x: int):
  return int(x/2)

def __Collatz_Odd(x: int):
  return int(x*3+1)

def __calculate_Collatz_Sequence(x: int):
  counter=0
  while x>1:
    if x<1:
      raise ValueError("input smaller than 1")
    if x%2==0:
      x=__Collatz_Even(x)
    else:
      x=__Collatz_Odd(x)
    counter+=1
  return counter

def calculate_longest_sequence(n: int):
  if not 1<n<10000000:
    raise ValueError("Input should be an integer between 1 and 10 million")
  longest_sequence=0
  for i in range(2,n):
    sequence=__calculate_Collatz_Sequence(i)
    #print(str(i), str(sequence))
    if sequence>longest_sequence:
      longest_sequence=sequence
      i_longest=i
  return i_longest

def main():
  print("The number below 1 million having the longest Collatz sequence is: " + str(calculate_longest_sequence(1000000)))

if __name__ == '__main__':
    main()