i = 1
iMax = int(input(“Give highest number: “))
sum = 0
while i < iMax:
                if i % 3 == 0: 
                                sum = sum + i
                elif i % 5 == 0:
                                sum = sum + i
                i = i + 1
print(sum)

"""
 Score: 3.5/10
    Run 1 Not sure if it works. Would need to check
    NamesOK 1.
    Linted 1
    Libraries list / 0.5  Would like to see a for loop instead of a home brew while
    SingleResponsibility/0
    Deepsource/1
    Testing -1/3   This is extremely hard to test and use. It requires manual input, and there is no reason for that.
    
Score 3.5/10
"""

