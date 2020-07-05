'''

encryption key = xor
the key is repeated cyclically throughout the message

p059_cipher.txt is file containing the encrypted ASCII codes
decrypt the message and find the sum of the ASCII values in the original text

ASCII bytes <> [XOR, key] <> decrypted value


'''

def genkey(message, key) -> bytes:

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

    return(bytes(keyString.encode('utf8')))


def xor_strings(s, t):
    """xor two strings together."""
    if isinstance(s, str):
        # Text strings contain single characters
        return b"".join(chr(ord(a) ^ ord(b)) for a, b in zip(s, t))
    else:
        # Python 3 bytes objects contain integer values in the range 0-255
        return bytes([a ^ b for a, b in zip(s, t)])
    
#https://www.mathblog.dk/project-euler-59-xor-encryption/

def analysis(message, keyLenght):
    maxsize = 0

    for m in message:
        if int(m) > maxsize:
            maxsize = m
    print(maxsize)

    aMessage = [keyLenght][maxsize+1]
    #print(len(aMessage))

if __name__ == "__main__": 

   
    






    with open("euler59/p059_cipher.txt") as f:
    
        line  = f.readlines()
        message = line[0].split(',')
        
        for ind, m in enumerate(message):
            message[ind] = int(m)
        
        analysis(message,3)
            
       
