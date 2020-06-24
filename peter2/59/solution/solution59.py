import string


def decrypt_characters(letter1, letter2, letter3, int_list):
    line = ''
    for i in range(0, len(int_list)-1, 3):
        xorred_letter1 = ord(letter1) ^ int_list[i + 0]
        xorred_letter2 = ord(letter2) ^ int_list[i + 1]
        xorred_letter3 = ord(letter3) ^ int_list[i + 2]
        line += chr(xorred_letter1)
        line += chr(xorred_letter2)
        line += chr(xorred_letter3)
    if 'is' in line and 'the' in line and ' a ' in line and ' of ' in line:
        print(line)
        print(sum(ord(letter) for letter in line))
    # print(line)


def start():
    if __name__ == '__main__':
        input_file = open("p059_cipher.txt", "r")
        string_list = [v.rstrip().split(",") for v in input_file]
        lowercase_list = string.ascii_lowercase
        int_list = [int(num) for num in string_list[0]]
        # print(len(int_list))
        [decrypt_characters(letter1, letter2, letter3, int_list) for letter1 in lowercase_list for
         letter2 in lowercase_list for letter3 in lowercase_list]


start()
