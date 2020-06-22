def __isPalindrome(num):
  if str(num)==str(num)[::-1]:
    return True
  return False

def highest_palindrome(c: int):
  if not 1<c<6:
    raise ValueError("Value should be between 1 and 6")
  palindromes=[]
  maxc=int(c*"9")+1
  minc=round(maxc*.9)
  [palindromes.append(i*j) for i in range(minc,maxc) for j in range(minc,maxc)
    if __isPalindrome(i*j)]
  return max(palindromes)

def main():
  print("The highest palindrome result of the product of two 3-digit numbers is: "
    +str(highest_palindrome(3)))

if __name__ == '__main__':
    main()