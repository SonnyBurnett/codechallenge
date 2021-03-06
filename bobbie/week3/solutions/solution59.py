from itertools import product, cycle


def keyGen():
    a, z = 97, 122
    return product(range(a, z+1), repeat=3)


def xorMessage(message, key):
    return [x ^ y for x, y in zip(message, cycle(key))]


def convertToAscii(message):
    return [chr(x) for x in message]


def decryptMessage(encrypted, key):
    return ''.join(convertToAscii(xorMessage(encrypted, key)))


def scoreEnglish(text):
    """Give a text a score based on the occurence of the top 10
    most common English words.
    Based on: https://en.wikipedia.org/wiki/Most_common_words_in_English

    Returns a score as an integer between 0 and 10
    """
    top10 = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'it']
    return sum([1 for x in top10 if x in text.lower().split()])


def sumIfEnglish(message):
    mostLikely = (0, None)
    for key in keyGen():
        originaltext = decryptMessage(message, key)
        score = scoreEnglish(originaltext)
        if score > mostLikely[0]:
            mostLikely = (score, originaltext)
    return sum([ord(x) for x in mostLikely[1]])


def main():
    with open('../resources/p059_cipher.txt') as file:
        message = [int(x) for x in file.readline().split(',')]
    print(sumIfEnglish(message))
