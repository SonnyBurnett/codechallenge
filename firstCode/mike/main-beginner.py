'''
Author: Mike van den Berge
Date: 07-Jun-2020
'''
sum_of_multiples = 0
for i in range(1,1000):
    if ((i % 3) == 0) or ((i % 5)==0):
        sum_of_multiples += i
print("Sum of multiples of 3 or 5 below 999: " + str(sum_of_multiples))


 Score:
    Run 1 Not sure if it works. Would need to check
    NamesOK 1. 
    Linted 1
    Libraries list / 1  For loop nice. Would like to see a list comprehension / filter but this was ok
    SingleResponsibility/0
    Deepsource/1
    Testing 0/3
    
Score 5/10
