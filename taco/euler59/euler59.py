import csv

KEY_LEN = 3


def read_csv_in_list(fn):
    with open(fn) as csv_file:
        x = [r for r in csv.reader(csv_file, delimiter=',')]
    return [int(i) for i in x[0]]


def split_list(cl, n):
    return cl[n::KEY_LEN]


def count_occurrences(cl):
    return [(x, cl.count(x)) for x in range(min(cl), max(cl)+1)]


def sort_the_list(sc):
    return sorted(sc, key=lambda x: x[1], reverse=True)


def find_most_common(cl):
    return cl[0][0]


def decrypt_list(cl, kl):
    return [chr(x ^ kl) for x in cl]


def make_text_from_lists(sp):
    decrypted_txt = ""
    for i in range(len(sp[0])):
        decrypted_txt += sp[0][i] + sp[1][i] + sp[2][i]
    return decrypted_txt


def count_ascii_values(st):
    return sum([ord(char) for char in st])


def decrypt_txt(dt):
    encrypted_lists, decrypt_lists, key_lists = ([] for i in range(3))
    for a in range(KEY_LEN):
        encrypted_lists.append(split_list(dt, a))
        key_lists.append(find_most_common(sort_the_list(count_occurrences(encrypted_lists[a]))) ^ ord(' '))
        decrypt_lists.append(decrypt_list(encrypted_lists[a], key_lists[a]))
    return make_text_from_lists(decrypt_lists)


def main():
    print(count_ascii_values(decrypt_txt(read_csv_in_list('p059_cipher.txt'))))


if __name__ == '__main__':
    main()

