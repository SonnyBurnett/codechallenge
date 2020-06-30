import csv


def read_csv_cipher(file):
    cipher = []
    with open(file, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            for char in row:
                cipher.append(int(char))
    return cipher


def freq(chars):
    freqs = {}
    for c in chars:
        if c not in freqs:
            freqs[c] = 0
        freqs[c] += 1
    return freqs


def cyclic_slice(chars, n):
    split = []
    for _ in range(n):
        split.append([])
    for i, c in enumerate(chars):
        split[i % n].append(c)
    return split


def find_encoded_space_char(cipher):
    return max(freq(cipher).items(), key=lambda x: x[1])[0]


def crack_key(cipher, keyLength):

    def decode_key_char_from_knowing_encoded_space(encoded_space):
        return encoded_space ^ 32

    key = []
    for cipher_slice in cyclic_slice(cipher, keyLength):
        space_char = find_encoded_space_char(cipher_slice)
        key_char = decode_key_char_from_knowing_encoded_space(space_char)
        key.append(key_char)
    return key


def decrypt(cipher, key):
    text = []
    keyLength = len(key)
    for i, c in enumerate(cipher):
        text.append(c ^ key[i % keyLength])
    return text


def main():
    cipher = read_csv_cipher('p059_cipher.txt')
    key = crack_key(cipher, 3)
    decoded = decrypt(cipher, key)

    print("".join(map(lambda x: chr(x), decoded)))

    print("The sum of the decoded ASCII codes is {}".format(sum(decoded)))


if __name__ == "__main__":
    main()
