'''

encryption key = xor
the key is repeated cyclically throughout the message

p059_cipher.txt is file containing the encrypted ASCII codes
decrypt the message and find the sum of the ASCII values in the original text

ASCII bytes <> [XOR, key] <> decrypted value


'''

def genkey(message, key):


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

    return keyString


def xor_strings(s, t):
    """xor two strings together."""
    if isinstance(s, str):
        # Text strings contain single characters
        return [ord(a) ^ ord(b) for a, b in zip(s, t)]
    else:
        #print("Not a string")
        # Python 3 bytes objects contain integer values in the range 0-255
        return [a ^ ord(b) for a, b in zip(s, t)]

    
#https://www.mathblog.dk/project-euler-59-xor-encryption/

def analysis(message):
    ''' 
        Input is an array of ASCII characters. 
    '''
    
    charDict = {}
    for ch in message:
        if ch not in charDict:
            charDict[ch] = 1
        else:
            charDict[ch] = charDict[ch]+1
    
    charDictSorted = {k: v for k, v in sorted(charDict.items(), key=lambda item: item[1], reverse=True)}

    
    for k in charDictSorted.keys():
        charDictSorted[k] = round(charDictSorted[k]/len(message),2)

    return charDictSorted




    
        
    

if __name__ == "__main__": 

    """  message = "This is a secret message"
    key = "test"

    gkey = genkey(message,key)
   

    encryptedtext = xor_strings(message,gkey)

    print(f'Encrypted: {encryptedtext}')

    decreptedtext = xor_strings(encryptedtext,gkey)
    

    print(f'Decrypted: {decreptedtext}')

    print("".join(chr(a) for a in decreptedtext)) """
    



    """ output = []
    for a, b in zip(message,genkey):
        x = ord(a) ^ ord(b)
        output.append(x)
        #print(f'A: {ord(a)} B: {ord(b)} xor: {x}')
        
    print(output)
    

    for a, b in zip(output,genkey):
        x = a ^ ord(b)
        #output.append(x)
        print(f'A: {a} B: {b} xor: {chr(x)}') """



    








    with open("euler59/p059_cipher.txt") as f:
    
        line  = f.readlines()
        message = line[0].split(',')
        
        for ind, m in enumerate(message):
            message[ind] = int(m)
        
        #print(message)
        #print(genkey(message,"god"))
        decryptedtext = xor_strings(message,genkey(message,"fur"))
        print("".join(chr(a) for a in decryptedtext))
       
