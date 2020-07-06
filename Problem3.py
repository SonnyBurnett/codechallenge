"""
@_author - Gautam Shah 
@_sourceURL - https://code.sololearn.com/cadi4WE6ajq4/#py
@_purpose - 
     Getting the largest existing n-digit pandigital prime number.

@_facts -
  Based on divisibility rule pandigital numbers of length 4 and 7 can form a prime number, since we have to find larget pandigital number so calculation starts consideration with 7 digit numbers.
  
  Checking all decreasing odd number for being pandigital and prime.

"""
def isPandigital( nDigitNumber, maxDigitRangeLength=9 ):
    
    nDigitNumber = str( nDigitNumber );
    return len( nDigitNumber ) == maxDigitRangeLength and not '1234567890'[:maxDigitRangeLength].strip( nDigitNumber )

def isPrime( nDigitNumber ):
    
    if nDigitNumber <= 1:
        return False
    if nDigitNumber <= 3:
        return True
    if nDigitNumber % 2 == 0 or nDigitNumber % 3 == 0:
        return False
        
    round = int( nDigitNumber**0.5 )
    factAssumptionNumber = 5
    while factAssumptionNumber <= round:
        
        if nDigitNumber % factAssumptionNumber == 0 or nDigitNumber % ( factAssumptionNumber + 2 ) == 0:
            return False
        factAssumptionNumber += 6
    return True
    
    

nDigitNumber = 7654321
maxDigitRangeLength = 7

while not( isPandigital( nDigitNumber, maxDigitRangeLength ) and isPrime( nDigitNumber ) ): nDigitNumber -= 2

print ( "The largest existing n-digit pandigital prime number is", nDigitNumber )
