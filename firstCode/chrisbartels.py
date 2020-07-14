#Initialize variable
sum =0

#Find and count multiple of 3 or 5
for i in range(1000):
    if (i % 3 == 0 or i % 5 == 0):
        sum += i
print("Sum of all multiples of 3 or 5 below 1000: " + str(sum))
"""

Score:
    Run1
    NamesOK 1
    Linted 0.5
    Libraries list / 1 nice use of for loop
    SingleResponsibility/0
    Deepsource/1
    Testing 0/3
    
Score 4.5/10
"""
