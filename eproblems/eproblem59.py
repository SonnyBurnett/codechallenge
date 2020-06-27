import argparse
from itertools import permutations

lower_case_letters = "abcdefghijklmnopqrstuvwyxz"
the_word = 'the'
average_the_occurrence = 1
average_words_lng = 5
average_sentence_lng = 17


def all_combos(length):
    """Generate all permutations for (brute) force calculations.

    :param length: The length of the cypher.
    :type length: int
    :return list: List of tuples representing all possible combinations.
    """
    return permutations(lower_case_letters, length)


def concatenate(object_in):
    """Make a string of the characters in a tuple.

    :param object_in: the object that needs to br reformatted into a string.
    :type object_in: tuple or list of characters.
    :return str: string of the characters of the given tuple.
    """
    return ''.join(object_in)


def chr_tuple2int_tuple(tuple_in):
    """Generate the the ascii numbers of the characters in the tuple.

    :param tuple_in:
    :type tuple_in: tuple og characters.
    :return tuple:
    """
    return tuple(ord(num) for num in tuple_in)


def cipher(a, b):
    """The XOR encryption method for this euler problem assignment.

    :param a: the encrypted number value.
    :type a: int
    :param b: the cypher number value.
    :type b: int
    :return int: the decrypted number value.
    """
    return a ^ b


def expand_cipher(tuple_in, size):
    """In order to decrypt the file the size of the cypher needs to match the characters in the given file.

    :param tuple_in: the cipher, as tuple of in that need to match the file length in.
    :type tuple_in: tuple of chr
    :param size: the duplication size for replicating the tuple_in.
    :type size: int
    :return list: the list of tuples in ascii int values matching the length of size.
    """
    helper = []
    for _ in range(0, size - 1):
        helper.append(chr_tuple2int_tuple(tuple_in))
    return helper


def read_by_chars(line_in, size):
    """Break up the line_in in to tuple of ascii int's strings into the given size.

    :param line_in: The list of one line containing the string integers of the ascii value.
    :type line_in: list of strings
    :param size: the breakup length of the chunks.
    :type size: int
    :return list: the list of tuples in size of the decrypt cypher.
    """
    by_tuples_of_size = []
    for letter in range(0, len(line_in), size):
        helper = []
        for char in range(0, size):
            helper.append(int(line_in[letter + char]))
        by_tuples_of_size.append(tuple(helper))
    return by_tuples_of_size


def decrypt_text(length, tuples_by_two):
    """This methods decrypts the paired tuples with the given length.

    :param length: the length of the cypher phrase.
    :type length: int
    :param tuples_by_two: a list of tuples containing two tuples with the same length.
    :return: the total sum of integers of the text and the decrypted text it self.
    """
    total_sum = 0
    decrypted_text = ""
    for sets in tuples_by_two:
        for i in range(0, length):
            helper: int = cipher(sets[0][i], sets[1][i])
            total_sum += helper
            decrypted_text += chr(helper)

    return total_sum, decrypted_text


def the_test(length, tuples_by_two):
    """This is an assumption method that tests if the is occurring in the decryption of the first 150 characters,
        ea assuming 4,7 letter length and 10 words in a sentence

    :param length: cypher length
    :type length: int
    :param tuples_by_two: a list of tuples containing two tuples with the same length.
    :return: boolean
    """
    _, decrypted_text = decrypt_text(length, tuples_by_two)
    return decrypted_text.count(the_word) > average_the_occurrence


def eproblem59(file_in, decrypt_str, length):
    """This is the main control method to guide the logic programing by brute force and then based on the occurrence
     of the word "the" (one of the most words used in English sentences) to select the best guess for the cipher.

    :param file_in: The file name containing the encrypted text.
    :type file_in: str
    :param decrypt_str: If given the decryption cypher string.
    :type decrypt_str: str
    :param length: If given the length of the cypher.
    :type length: int
    :return str: The result of the sum of all the decrypted charters integer values.
    """
    best_match = 0
    best_sum = 0
    brute_combo = []
    result = ""

    if len(decrypt_str) > 0:
        brute_combo.append(tuple(list(decrypt_str)))
        length = len(decrypt_str)
    else:
        brute_combo = list(all_combos(length))

    with open(file_in, "r") as f:
        for line in f:
            chars = line.split(",")
            the_guess = (len(chars)) // (average_words_lng * average_sentence_lng)

        for cur_combo in brute_combo:
            cur_repeated_cipher = expand_cipher(cur_combo, len(chars))
            by_tuples = read_by_chars(chars, length)
            tuples_by_two = list(zip(by_tuples, cur_repeated_cipher))

            if the_test(length, tuples_by_two[0:average_words_lng * average_sentence_lng]):
                total_sum, decrypted_text = decrypt_text(length, tuples_by_two)
                count_the = decrypted_text.count(the_word)
                if count_the > best_match:
                    print(concatenate(list(cur_combo)), ":", the_word, "count =", count_the, ":", total_sum)
                    best_match = count_the
                    best_sum = total_sum
                    result = concatenate(list(cur_combo))
                    if count_the > the_guess:
                        break  # Anti-pattern to knock-out the brute  if the word "the" seems to be average in the text.

    f.close()
    return result + ": " + str(best_sum)


def main():
    """"Main is the interactive method start of the second project Euler problem,
        reasoning is documented in the '../notebooks/Project Euler Problem 59.ipynb' notebook.
        This method has anti pattern (Input kludge) and cannot be tested without a human or screen scraper,
         but used for the interactive guided demonstration of the Notebooks.

    """
    file_name: str = input("File Name to read: ")
    key_str: str = input("Cipher key: ")
    key_lng: int = int(input("Cipher key length: "))
    eproblem59(file_name, key_str, key_lng)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", help="Set input file")
    parser.add_argument("--key", "-k", help="Set cipher key")
    parser.add_argument("--length", "-l", help="Set cipher key length")
    args = parser.parse_args()

    if not isinstance(args.file, type(None)):
        eproblem59(args.file, args.key, args.lenght)
    else:
        main()
