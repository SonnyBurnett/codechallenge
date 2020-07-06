#
#   Euler 59
#
#   Author X.MAYEUR
#


def encrypt(message, key):
    encrypted_msg = []
    i = 0
    for m in message:
        encrypted_msg.append(str(ord(m) ^ ord(key[i%len(key)])))
        i += 1
    return encrypted_msg


def decrypt(message, key):
    msg = ''
    i = 0
    for m in message:
        msg += chr(int(m) ^ ord(key[i%len(key)]))
        i += 1
    return msg


def analysis(bmsg, keylength=3):
    # convert array of string to array of integer
    bmsg = [int(b) for b in bmsg]
    maxsize = max(bmsg)
    # create 3 piles corresponding to the encryption of a character by each key character
    piles = [[0 for x in range(maxsize+1)] for y in range(keylength)]
    # top 3-items array
    top3 = [0 for x in range(3)]
    i = 0
    # loop on the encrypted message
    for b in bmsg:
        b = int(b)
        j = i % keylength
        # count the frequency of each encrypted byte
        piles[j][b] += 1
        # and retain the most frequent ones for each key
        if piles[j][b] > piles[j][top3[j]]:
            top3[j] = b
        i += 1

    # Assume the space character is the most frequent in a text
    space = ord(' ')
    # and decrypt the key
    top3 = [k ^ space for k in top3]
    # get the key as a string
    the_key = ''
    for k in top3:
        the_key += chr(k)
    return the_key


def main():
    # read the encrypted message
    with open('p059_cipher.txt', 'r') as f:
        encrypted = f.read()
    bmsg = encrypted.split(',')

    # guess the key
    the_key = analysis(bmsg)
    clear_msg = decrypt(bmsg, the_key)
    # print the decrypted message and see whether is is readable
    print(clear_msg)
    # calculate the requested result
    result = sum(ord(c) for c in clear_msg)
    print(result)


if __name__ == '__main__':
   main()
