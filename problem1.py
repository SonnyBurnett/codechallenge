"""
@_author - Gautam Shah 
@_sourceURL - https://code.sololearn.com/czc6Q6wrTfw7/#py
@_purpose - 
       We are summing up all the numbers which is multiples of 3 or 5 below 1000.
       
@_facts -
      Below we have declared firstNumber, secondNumber, minRange, maxRange as a separate variable sothat it can be reusable and user can get sum of any given two numbers and within specified range. - { code reusability }

"""

"""
function : getSum

parameter1 - first number for multiply checking
parameter2 - second number for multiply checking
parameter3 - starting range number for sum 
parameter4 - end range number for sum

return {sum} - returning sum of multiples of firstNumber and secondNumber of given range number
"""
def getSum( firstNumber, secondNumber, minRange, maxRange ):

  sum = 0
  for incrementedNumber in range( minRange, maxRange ):
    if incrementedNumber % firstNumber == 0 or incrementedNumber % secondNumber == 0:
      sum += incrementedNumber
  return sum


firstNumber = 3
secondNumber = 5
minRange = 1
maxRange = 1000

finalSum = getSum( firstNumber, secondNumber, minRange, maxRange )
print( 'Sum of all the multiples of',  firstNumber , 'or', secondNumber, 'below', maxRange, 'is -',  finalSum )
