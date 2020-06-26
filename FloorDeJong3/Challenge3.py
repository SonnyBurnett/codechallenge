import re
import string
from itertools import cycle
from langdetect import detect


def xor_decrypt(data, key):

    xored = ''.join(chr(int(x) ^ ord(y)) for (x, y) in zip(data.split(","), cycle(key)))
    return xored


if __name__ == "__main__":
    filename = "p059_cipher.txt"
    try:
        file = open(filename, "r", encoding="ASCII")
    except Exception:
        import sys

        sys.exit("Opening %s failed" % filename)

    line = file.read()
    # print(line)

    words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

    bla = 0

    letters = string.ascii_lowercase
    # print(letters)
    #
    # for i in letters:
    #     for j in letters:
    #         for k in letters:
    #             key = i + j + k
    #             decrypted = xor_decrypt(line, key)
    #             print(key + ":" + decrypted.split()[0])
    #             if detect(decrypted.split()[0]) == "en":
    #                 print(key + ":" + decrypted)

                # if detect(decrypted) == "en":
                #     print(key + ": " + decrypted)
                #     print("---------------------------------------------------------------------------------------")

    # print("bla")
    # import nltk
    # nltk.download()
    # from nltk.corpus import stopwords
    # word_list = stopwords.words()
    # # prints 236736
    # print(len(word_list))
    # print(word_list[:100])
    newData = "GeeksforGeeks, is_an-awesome ! app + too and "
    print(re.split(', |_|-|!', newData))
    print(re.split(',| |_|-|!', newData))
