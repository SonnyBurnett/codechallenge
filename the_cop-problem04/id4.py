# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
def reverse(text):
    return text[::-1] 

def check_palindrome(n):
    n_length = len(str(n))
    n_string = str(n)
    if n_length < 2:
        return False
    if (n_length % 2) == 0:
        halfway_index = int(n_length/2)
        first_half = n_string[halfway_index:]
        second_half = n_string[:halfway_index]
        if reverse(first_half) == second_half:
            return True
    return False

if  __name__ == "__main__":
    if check_palindrome(22):
        print("Number is palindrome")
    if not check_palindrome(25):
        print("Number is not palindrome")
    pass
    max_int = 999
    answers_list = []
    for x in range(1, max_int):
        for y in range(1, x):
            if check_palindrome(x*y):
                answers_list.append(x*y)
    print(answers_list)
    print("Biggest number on the list is: {}".format(max(answers_list)))