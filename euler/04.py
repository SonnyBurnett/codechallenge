'''
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''


MAX_DIGITS = 3
print(max([(x * y) for x in range(10**MAX_DIGITS) for y in range(10**MAX_DIGITS) if len(str(x * y)) % 2 == 0 and str(x * y) == str(x * y)[::-1]]))
