'''
Score: 5
    Run1
    NamesOK1
    Linted1
    Libraries list / 1  Nice to see the for loop
    SingleResponsibility/0
    Deepsource/1  <------ Taco to check
    Testing 0/3
    
Score 5/10
'''
numbers = range(1000)
total = 0

for number in numbers:
    if number % 3 == 0 or number % 5 == 0:
      total += number
      print(total)
