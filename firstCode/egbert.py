#Solve Euler Problem 1 

#sum of all multiples  
sum=0
#i counter
i=0 
while i<1000:
  if i%3==0 or i%5==0:
    sum+=i
  #increase counter i for next iteration    
  i+=1 
print(sum)

"""
Score:
    Run1
    NamesOK1
    Linted1
    Libraries list / 0.5 would like to see a for loop next time
    SingleResponsibility/0
    Deepsource/1
    Testing 0/3
    
Score 4.5/10
"""
