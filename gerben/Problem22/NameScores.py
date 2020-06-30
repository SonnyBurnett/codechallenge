import csv

def wordvalue(name: str):
  if not type(name) is str:
    raise TypeError("Input should be a string of characters in the alphabet")
  if not name.isascii():
    raise ValueError("Input should be a string of characters in the alphabet")
  return sum([ord(char) - 96 for char in name.lower()])

def main():
  with open('p022_names.txt', 'r') as f:
    names = sorted([row for row in csv.reader(f)][0])

  total=0
  for index, name in enumerate(names,1):
    total+=(index)*wordvalue(name)

  print("The sum of all name scores is: " + str(total))

if __name__ == '__main__':
    main()
