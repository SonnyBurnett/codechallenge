a = 3
b = 5
r1 = 0
r2 = 1000
step = 1
dividers = [a, b]

def find_sum():
  return sum([i for i in range(r1, r2, step) if check_division(i, dividers)])

def check_division(i, dividers):
  for x in dividers:
    if i % x == 0:
      return True

print(find_sum())