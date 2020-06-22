"""
@_author - Gautam Shah 
@_sourceURL - https://code.sololearn.com/cG6yvIFLE3ra/#py
@_purpose - 
      We are summing up all the numbers which is multiples of 2 under 4M in fibonacci series.

@_facts -
  Below we have declared maxNumber which can be reusable and user can get sum of any given max limit of fibonacci series.{code reusability}

"""

"""
function : getSum

parameter1 - Max limit to sum of fibonacci
return {sum} - returning  sum up all the numbers which is multiples of 2 under 4M in fibonacci series.

"""

def getSum( maxNumber ):
    temp = 0
    increment = 1
    sum = 0
    
    while increment < maxNumber:
        if( increment % 2 == 0 ):
            sum += increment
           
        temp,increment = increment, temp+increment
    return sum
    
# change the maxNumber where you want to get sum of febonacci  
maxNumber = 4000000
print("Sum of all the numbers which is multiples of 2 under 4M in fibonacci series -",getSum(maxNumber))
