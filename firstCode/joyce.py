"""Score:
    Run1
    NamesOK1
    Linted1
    Libraries list / 0.5 would like to see a for loop next time
    SingleResponsibility/0
    Deepsource/1
    Testing 0/3
    
Score 4.5/10
"""


#Project Euler problem 1
#https://projecteuler.net/problem=1

number = 3
sum = 0
while number < 1000:
    if (number % 3 == 0) or (number % 5 == 0):
        sum += number

    number += 1

print("sum = "+ str(sum))
