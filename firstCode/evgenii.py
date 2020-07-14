a = 3
b = 5
c = 1000
i = 0
total = 0

while i < c:

  if i % a == 0 or i % b == 0:
    total += i
    print(i)

  i += 1

print(total)

"""
Score:
    Run1
    NamesOK 0.5. Total nice. But WTF is a/b/c
    Linted1
    Libraries list / 0.5 would like to see a for loop next time
    SingleResponsibility/.5 // the variables a,b,c help us handle change, and that's what these points are about
    Deepsource/1
    Testing 0/3
    
Score 4.5/10
"""
