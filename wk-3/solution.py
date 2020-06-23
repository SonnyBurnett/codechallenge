import csv


def freq(chars):
    freqs = {}
    for c in chars:
        if c not in freqs:
            freqs[c] = 0
        freqs[c] += 1
    return freqs


def cyclic_split(chars, n):
    split = []
    for _ in range(n):
        split.append([])
    for i, c in enumerate(chars):
        split[i % n].append(c)
    return split


def read_csv_cipher(file):
    cipher = []
    with open(file, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            for char in row:
                cipher.append(int(char))
    return cipher


def main():
    print(read_csv_cipher('p059_cipher.txt'))


if __name__ == "__main__":
    main()
