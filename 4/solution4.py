def is_palindrome(number):
    number_as_string = str(number)
    character_list = [c for c in range(len(number_as_string)) if number_as_string[c] == number_as_string[len(number_as_string)-c-1]]
    if len(character_list) == len(number_as_string):
        return True
    else:
        return False

totallist = []
for a in range(100,999):
    list = [a*b for b in range(100,999) if is_palindrome(a*b)]
    if len(list) > 0:
        totallist.append(max(list))
print(max(totallist))