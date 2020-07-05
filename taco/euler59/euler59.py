import csv

KEY_LEN = 3


def read_encrypted_txt_in_list(file_name):
    try:
        with open(file_name) as csv_file:
            x = [r for r in csv.reader(csv_file, delimiter=',')]
        return [int(i) for i in x[0]]
    except:
        print("File not found!")
        return []


def split_list(original_list, start_pos):
    return original_list[start_pos::KEY_LEN]


def count_occurrences(input_list):
    return [(x, input_list.count(x)) for x in range(min(input_list), max(input_list)+1)]


def sort_list(unsorted_list):
    return sorted(unsorted_list, key=lambda x: x[1], reverse=True)


def get_first(sorted_list):
    return sorted_list[0][0]


def decrypt_list(encrypted_list, key):
    return [chr(x ^ key) for x in encrypted_list]


def make_text_from_lists(list_of_lists):
    decrypted_txt = ""
    for i in range(len(list_of_lists[0])):
        for x in range(KEY_LEN):
            decrypted_txt += list_of_lists[x][i]
    return decrypted_txt


def count_ascii_values(text_string):
    return sum([ord(char) for char in text_string])


def find_key(encrypted_char):
    return encrypted_char ^ ord(' ')


def decrypt_txt(encrypted_txt_in_list):
    encrypted_lists, decrypt_lists, key_lists = ([] for i in range(3))
    for a in range(KEY_LEN):
        encrypted_lists.append(split_list(encrypted_txt_in_list, a))
        key_lists.append(find_key(get_first(sort_list(count_occurrences(encrypted_lists[a])))))
        decrypt_lists.append(decrypt_list(encrypted_lists[a], key_lists[a]))
    return make_text_from_lists(decrypt_lists)


def main():
    print(count_ascii_values(decrypt_txt(read_encrypted_txt_in_list('p059_cipher.txt'))))


if __name__ == '__main__':
    main()

