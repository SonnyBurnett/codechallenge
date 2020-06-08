numbers = range(1000)
total = 0

for number in numbers:
    if number % 3 == 0 or number % 5 == 0:
      total += number
      print(total)
