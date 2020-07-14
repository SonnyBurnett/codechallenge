# This code calculates the sum of all the multiples of 3 and 5 below 1000
total = 0
for n in range(1000):
    if ( n % 3 == 0 ) or ( n % 5 == 0 ):
        total += n
print("The sum of all the multiples of 3 or 5 below 1000 is: " + str(total))

"""Score:
    Run1
    NamesOK1
    Linted1
    Libraries list / 1  Nice to see the for loop
    SingleResponsibility/0
    Deepsource/1  <------ Taco to check
    Testing 0/3
    
Score 5/10
"""
