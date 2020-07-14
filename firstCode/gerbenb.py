import numpy as np

def multiples(big_amount, divlist):
  '''
  This function returns a list of multiples in the divlist list below big_amount.
  It accepts two arguments:
  - big_amount, which should be a number
  - divlist, which should be a list of numbers
  '''
  divisors=[]
  for i in range(big_amount):
    for j in divlist:
      if(i%j==0):
        divisors.append(i)
  return np.unique(divisors)

result=multiples(1000,[3,5]) 
#print(divisors)
print("The sum of all multiples of 3 and 5 below 1000 is: " + str(sum(result)))
"""
Score 5/10
  runes 1
  Names 1
  Linted 1
  Easy to change acceptance criteria 1
  Loops separated from business logic 0
  Deep source 1
  Tests 0 (but we like the fact you have a testable thing!)
  
Observation: You make a list. The list consumes memory. You didn't need to make the list
  """
  
  

  
  
