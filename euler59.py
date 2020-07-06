def encrypt(message, key):
    encrypted_msg = []
    i = 0
    for m in message:
        encrypted_msg.append(ord(m) ^ ord(key[i%len(key)]))
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
    maxsize = int(max(bmsg))
    piles = [[0 for x in range(maxsize+1)] for y in range(keylength)]
    key = [0 for x in range(3)]
    i = 0
    for b in bmsg:
        b = int(b)
        j = i % keylength
        piles[j][b] = piles[j][b] + 1
        if piles[j][b] > piles[j][key[j]]:
            key[j] = b
        i += 1

    space = ord(' ')
    keys = [k ^ space for k in key ]
    the_key = ''
    for k in keys:
        the_key += chr(k)
    return the_key


with open('p059_cipher.txt', 'r') as f:
    encrypted = f.read()

bmsg = encrypted.split(',')
the_key = analysis(bmsg)
clear_msg = decrypt(bmsg, the_key)
result = sum(ord(c) for c in clear_msg)
print(result)