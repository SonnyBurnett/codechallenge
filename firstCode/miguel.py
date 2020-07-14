total = 0
for num in range(1, 1000):
    if num % 3 == 0:
        total += num
        continue
    if num % 5 == 0:
        total += num
        continue

print(total)

"""
 Score:
    Run 1
    NamesOK 1. 
    Linted 1
    Libraries list / 0 This point is really for the way you have structured the loop, and this use of continue is bad, as is the repeated business logic.
    SingleResponsibility/0
    Deepsource/1
    Testing 0/3
    
Score 4/10
"""
