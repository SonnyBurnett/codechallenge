import os


_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
filename = 'p013-input.txt'
big_sum = 0.0

with open(os.path.join(_location, filename)) as input_file:
  oneline = input_file.readline()
  while oneline:
    big_sum += int(oneline)
    oneline = input_file.readline()

print(format(big_sum, '.0f')[:10])
