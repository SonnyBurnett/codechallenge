'''

encryption key = xor
the key is repeated cyclically throughout the message

p059_cipher.txt is file containing the encrypted ASCII codes
decrypt the message and find the sum of the ASCII values in the original text

ASCII bytes <> [XOR, key] <> decrypted value


'''

def pwd_string(message, key):

    keyString = ""
    tmp = 0
    for i in range(0,len(message)):
        
        if tmp < len(key):
            keyString += key[tmp]
            tmp +=1
        else:
            tmp = 0
            keyString += key[tmp]
            tmp +=1

    return(keyString)


def xor_strings(s, t) -> bytes:
    """xor two strings together."""
    if isinstance(s, str):
        # Text strings contain single characters
        return b"".join(chr(ord(a) ^ ord(b)) for a, b in zip(s, t))
    else:
        # Python 3 bytes objects contain integer values in the range 0-255
        return bytes([a ^ b for a, b in zip(s, t)])
    
  


if __name__ == "__main__": 

    key = pwd_string("THis is a message", "xor")

    

    with open("euler59/p059_cipher.txt") as f:
        
        line  = f.readlines()
        #data = line[0].split(',')


        ciphertext = xor_strings(line, key)

        print(ciphertext)
            
