import argparse
from itertools import permutations

lower_case_letters = "abcdefghijklmnopqrstuvwyxz"


def all_combos(length):
    return permutations(lower_case_letters, length)


def concatenate(tuple_in):
    return ''.join(tuple_in)


def chr_tuple2int_tuple(tuple_in):
    return tuple(ord(num) for num in tuple_in)


def cipher(a, b):
    return a ^ b


def expand_cipher(tuple_in, size):
    helper = []
    for i in range(0, size - 1):  # TODO: how to fix this DeepSource false positive?
        helper.append(chr_tuple2int_tuple(tuple_in))
    return helper


def read_by_chars(line_in, size):
    by_tubles_of_size = []
    for letter in range(0, len(line_in) - 1, size):
        helper = []
        for char in range(0, size):
            helper.append(int(line_in[letter + char]))
        by_tubles_of_size.append(tuple(helper))
    return by_tubles_of_size


def eproblem59(file_in, decrypt):
    best_match = 0
    brute_combo = []
    result = ""

    if len(decrypt) > 0:
        brute_combo.append(tuple(list(decrypt)))
    else:
        brute_combo = list(all_combos(3))

    with open(file_in, "r") as f:
        for line in f:
            chars = line.split(",")

        for cur_combi in brute_combo:
            cur_repeated_cipher = expand_cipher(cur_combi, len(chars))
            by_tuples = read_by_chars(chars, 3)
            tuples_by_two = list(zip(by_tuples, cur_repeated_cipher))
            decrypted_text = ""
            total_sum = 0

            for sets in tuples_by_two:
                for i in range(0, 3):
                    helper: int = cipher(sets[0][i], sets[1][i])
                    total_sum += helper
                    decrypted_text += chr(helper)

            if decrypted_text.count('the') > best_match:
                print(str(list(cur_combi)), " : the count = ", decrypted_text.count('the'), " :", total_sum)
                best_match = decrypted_text.count('the')
                result = str(list(cur_combi))

    f.close()
    return result


def main():
    """"Main is the interactive method start of the second project Euler problem,
        reasoning is documented in the '../notebooks/Project Euler Problem 59.ipynb' notebook.
        This method has anti pattern (Input kludge) and cannot be tested without a human or screen scraper,
         but used for the interactive guided demonstration of the Notebooks.

    """
    file_name = input("File Name to read: ")
    key_str = input("Cipher key: ")
    eproblem59(file_name, key_str)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", help="Set input file")
    parser.add_argument("--key", "-k", help="Set cipher key")
    args = parser.parse_args()

    if not isinstance(args.file, type(None)):
        eproblem59(args.file, args.key)
    else:
        main()
