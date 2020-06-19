def __sum_of_squares(c):
  x=[i**2 for i in range(c+1)]
  return sum(x)

def __square_of_sum(c):
  x=[i for i in range(c+1)]
  return sum(x)**2

def sum_square_difference(c: int):
  if not 1<c<250:
    raise ValueError("input must be an integer between 1 and 250")
  ssq=__sum_of_squares(c)
  sqs=__square_of_sum(c)
  return sqs-ssq

def main():
  print("The difference between the sum of squares of the first one hundred natural numbers" +
    " and the square of the sum is: " + str(sum_square_difference(100)) )

if __name__ == '__main__':
    main()