import string
from itertools import cycle
import enchant
from itertools import product
import sys


def xor_decrypt_encrypt_ascii_list(input_data, key):
    return ''.join(chr(int(x) ^ ord(y)) for (x, y) in zip(input_data.split(","), cycle(key)))


def is_english(input_data):
    common_words = ["a", "the", "I", "and", "if", "of", "or", "to", "is", "you", "that", "it", "he", "was", "for", "are"
                    , "as", "with", "his", "they", "at", "be", "this", "have", "from", "one", "had", "by", "word", "but"
                    , "not", "what", "were", "all", "we", "when", "your", "can", "said", "there", "some", "my", "use"
                    , "her", "than", "an", "would", "first", "each", "make", "water", "which", "like", "been", "she"
                    , "him", "call", "do", "into", "who", "how", "time", "oil", "their", "has", "its", "look", "now"
                    , "will", "two", "find", "up",  "more", "long", "other", "write", "down", "about", "go", "day"
                    , "out", "see", "did", "many", "number", "get", "then", "no", "come", "them", "way", "made", "these"
                    , "could", "may", "so", "people", "part"]

    return [(word.lower() in input_data.lower().split()) for word in common_words].count(True)


def is_english1(input_data, language):
    d = enchant.Dict(language)
    return [d.check(word) for word in input_data.split()].count(True)


def decrypt_using_three_lower_letters(input_data):
    nr_common_words = 0
    letters = string.ascii_lowercase
    english_decrypted = None
    for i, j, k in product(letters, repeat=3):
        decrypted = xor_decrypt_encrypt_ascii_list(input_data, i + j + k)

        this_nr_common_words = is_english(decrypted)
        if this_nr_common_words > nr_common_words:
            nr_common_words = this_nr_common_words
            english_decrypted = decrypted

    return english_decrypted


if __name__ == "__main__":
    filename = "p059_cipher.txt"
    try:
        file = open(filename, "r", encoding="ASCII")
    except FileNotFoundError:
        sys.exit("Opening %s failed" % filename)

    data = file.read()
    decrypted_data = decrypt_using_three_lower_letters(data)
    ascii_sum = sum([ord(character) for character in decrypted_data])

    print(ascii_sum)

