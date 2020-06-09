def isPalindrome(num):
  '''
  This function checks and reports if the input number is a palindrome or not.
  It expects one argument, which should be an integer.
  '''
  if str(num)==str(num)[::-1]:
    return True
  else:
    return False

palindromes=[]
[palindromes.append(i*j) for i in range(999,900,-1) for j in range(999,900,-1) if isPalindrome(i*j)]

print("The highest palindrome result of the product of two 3-digit numbers is: "+str(max(palindromes)))