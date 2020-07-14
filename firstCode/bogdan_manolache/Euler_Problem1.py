list = []
for i in range(1000):
 if i % 3 == 0:
  list.append(i)
 elif i % 5 == 0:
  list.append(i)
print (sum(list))
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
