'''
Author: Mike van den Berge
Date: 07-Jun-2020
'''
sum_of_multiples = 0
for i in range(1,1000):
    if ((i % 3) == 0) or ((i % 5)==0):
        sum_of_multiples += i
print("Sum of multiples of 3 or 5 below 999: " + str(sum_of_multiples))
