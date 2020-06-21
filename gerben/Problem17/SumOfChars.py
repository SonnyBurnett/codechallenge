from num2words import num2words

def __stripchars(s: str):
  return ''.join([i for i in s if i.isalpha()])

def count_alphabetic_chars_in_numbers(nstart: int,nstop: int):
  if not -1000000<nstart<1000000:
    raise ValueError("start number should be an integer between -1 million and 1 million")
  if not -1000000<nstop<1000000:
    raise ValueError("stop number should be an integer between -1 million and 1 million")
  if nstop<nstart:
    raise ValueError("stop number should be larger than start number")
  total=0
  for i in range(nstart,nstop):
    l=len(__stripchars(num2words(i)))
    total+=l
  return total

def main():
  print("The sum of all alphabetic characters in the words one to one thousand is: "
    + str(count_alphabetic_chars_in_numbers(1,1001)))

if __name__ == '__main__':
    main()