import string
from itertools import product


def contains_all_words(list_of_words, line_of_text):
    return [word in line_of_text for word in list_of_words].count(True) == len(list_of_words)


def decrypt_list_of_ascii_codes(key, ascii_code_list):
    return ''.join(
        [chr(k ^ ascii_code_list[key.index(k) + i]) for i in range(0, len(ascii_code_list) - 2, len(key)) for k in key])


def sum_of_ascii_codes(line_of_text):
    return sum(ord(letter) for letter in line_of_text)


def start():
    if __name__ == '__main__':
        input_file = open("p059_cipher.txt", "r")
        words_list = [' a ', ' in ', ' the ', ' of ']
        string_list = [value.rstrip().split(",") for value in input_file]
        ascii_code_list = [int(ascii_code_string) for ascii_code_string in string_list[0]]

        keys = ([ord(a), ord(b), ord(c)] for a, b, c in product(string.ascii_lowercase, repeat=3))

        [print(sum_of_ascii_codes(decrypt_list_of_ascii_codes(key, ascii_code_list))) for key in keys
         if contains_all_words(words_list, decrypt_list_of_ascii_codes(key, ascii_code_list))]


start()
