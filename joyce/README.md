# GEP_Python_Challenge
GEP Coding Python Challenge

This is a repository for the GEP Python Coding Challenge Assignments.
1.  Assignment 1 is a Python program to solve Project Euler problem 1.  
    https://projecteuler.net/problem=1  
    
2.  Assignment 2 is a Python program to solve Project Euler problem 2.  
    https://projecteuler.net/problem=2  
    
    This function is made to run on different ranges within the Fibonacci sequence.  
    The first parameter determines where the range of the Fibonacci sequence should start.  
    If the first parameter is a Fibonacci number, the range will start with that number.   
    If the first parameter is not a Fibonacci number, the range will start with first 
    Fibonacci number that comes after this parameter.  
    The second parameter is the maximum value for the range. The last Fibonacci number 
    used in the function should be below this value.  
    The result is a sum of all even Fibonacci numbers in the specified range.
    
3.  Assignment 3 is Python program to solve Project Euler 41.  
    https://projecteuler.net/problem=41
    
    This function is made to run on numbers where the number of digits is in a specified range.
    The digits are assumed to be part of the base-10 numbering system.  
    The pandigital with 1 digit is excluded, because it only consists of the number 1 and 
    that's not a prime number.  
    Pandigitals of 2, 3, 5, 6, 8 and 9 digits are also excluded, because their digits add up to a 
    number that is divisible by 3. If the digits of a number add up to a multiple of 3, 
    the number is divisible by 3 and can therefore not be a prime number. If you have never 
    heard of this rule, you can find a nice explanation here:  
    https://www.khanacademy.org/math/pre-algebra/pre-algebra-factors-multiples/pre-algebra-divisibility-tests/v/the-why-of-the-3-divisibility-rule  
    It is still possible to select a range that includes pandigitals with the excluded number of digits, 
    but they will be skipped in the function.  
    The function returns the largest prime pandigital number for numbers with a number of digits 
    that is in the specified range. If the range is (7,7), then only the largest pandigital 
    prime number with 7 digits is returned.
    
    
    
   