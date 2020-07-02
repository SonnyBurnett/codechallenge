import string
from itertools import cycle
import enchant
from itertools import product
import sys


def xor_decrypt_encrypt_ascii_list(input_data, key, encryption):
    # if not encryption:
    #     input_data = []
    new_data = ''.join(chr(int(x) ^ ord(y)) for (x, y) in zip(input_data.split(","), cycle(key)))

    return new_data

def is_english_line(input_data):
    common_words = ["a", "the", "I", "and", "if", "of", "or", "to", "is", "you", "that", "it", "he", "was", "for", "are"
                    , "as", "with", "his", "they", "at", "be", "this", "have", "from", "one", "had", "by", "word", "but"
                    , "not", "what", "were", "all", "we", "when", "your", "can", "said", "there", "some", "my", "use"
                    , "her", "than", "an", "would", "first", "each", "make", "water", "which", "like", "been", "she"
                    , "him", "call", "do", "into", "who", "how", "time", "oil", "their", "has", "its", "look", "now"
                    , "will", "two", "find", "up",  "more", "long", "other", "write", "down", "about", "go", "day"
                    , "out", "see", "did", "many", "number", "get", "then", "no", "come", "them", "way", "made", "these"
                    , "could", "may", "so", "people", "part"]

    return [(word.lower() in input_data.lower().split()) for word in common_words].count(True) >= len(common_words)/4


def is_english2(input_data, language):
    d = enchant.Dict(language)
    return [d.check(word) for word in input_data.split()].count(True) >= (len(input_data.split()) * 2 / 3)


def decrypt_using_three_lower_letters(input_data):
    letters = string.ascii_lowercase
    for i, j, k in product(letters, repeat=3):
        decrypted = xor_decrypt_encrypt_ascii_list(input_data, i + j + k, False)

        if is_english_line(decrypted):
            return decrypted

    sys.exit("No three lower lettered key found, that encrypts data to correct english")


if __name__ == "__main__":
    filename = "p059_cipher.txt"
    try:
        file = open(filename, "r", encoding="ASCII")
    except FileNotFoundError:
        sys.exit("Opening %s failed" % filename)

    data = file.read()
    decrypted_data = decrypt_using_three_lower_letters(data)
    ascii_sum = sum([ord(character) for character in decrypted_data])

    print(len(decrypted_data.split()))
    print(ascii_sum)

