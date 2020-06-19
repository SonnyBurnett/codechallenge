'''
Author: Mike van den Berge
Date: 07-Jun-2020
Project Euler problem: 2
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

prev_value = 1
value = 1
new_value = 0
sum_values = 0

max_result = int(input("Max result eg 4000000: "))
while value < max_result:

    new_value = prev_value + value
    # calc sum of even valued values
    if new_value % 2 == 0:
        sum_values += new_value
    prev_value = value
    value = new_value

print("found it: " + str(sum_values))