def is_palindrome(number):
    number_as_string = str(number)
    print(len(number_as_string))
    character_list = [c for c in range(len(number_as_string)) if number_as_string[c] == number_as_string[len(number_as_string)-c-1]]
    if len(character_list) == len(number_as_string):
        return True
    else:
        return False


print(is_palindrome(9109))
# primelist = [i for i in range(1,99) if is_palindrome(i)]
