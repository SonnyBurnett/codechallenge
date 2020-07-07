'''

encryption key = xor
the key is repeated cyclically throughout the message

p059_cipher.txt is file containing the encrypted ASCII codes
decrypt the message and find the sum of the ASCII values in the original text

ASCII bytes <> [XOR, key] <> decrypted value


'''
from string import ascii_lowercase as lowc
from string import ascii_letters as asciilet
from nltk.corpus import words
import time

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

def findKey(message, keyLenght):
    maxSize = 0
    for m in message:
        if m > maxSize:
            maxSize = m

    print(f'MaxSize: {maxSize}')

    
    aMessage = {}
    for i in range(0, keyLenght):
        aMessage[i] = []
        for j in range(0,maxSize+1):
            aMessage[i].append(0)
    
    print(f'aMessage size is {len(aMessage[0])}')

    key = []
    for i in range(0,keyLenght):
        key.append(0)
    print(f'Key entries = {len(key)}')
    

    for ind, m in enumerate(message):
        j = ind % keyLenght
        #print(f'Letter is {m} j is {j} and index = {ind}')
        aMessage[j][ind] += 1

    
    for ind, m in enumerate(message):
        j = ind % keyLenght
        #print(f'{aMessage[j][message[ind]]} compared to {aMessage[j][key[j]]}')
        if aMessage[j][message[ind]] > aMessage[j][key[j]]:
            #print(f'Add to key {message[ind]}')
            key[j] = message[ind]


    """ spaceASCII = 32
    for i, c in enumerate(key):
        key[i] = c ^ spaceASCII """


    print(aMessage)
    print(key)
        

def findKey2(message, keyLenght):
    '''
    Pass each lowercase letter through the encrypted message and xor the ASCII characters. 
    if the xor result is a lowercase character then it is a pass. Summ all the results and provide a score %.
    '''
    
    keys = {}
    for k in range(0, keyLenght):
        lowcDict = {}
        for lc in lowc:
            lowcDict[lc] = 0
        keys[k] = lowcDict

       
    #print(len(keys[0][1]))

    for i, c in enumerate(message):
        #For each letter in a message
        j = i % keyLenght
        #Get value of a keys dictionary 
        #Loop through the alphabet and xor the value
        for l in lowc:
            x = ord(l) ^ c
            #print(chr(x))
            if chr(x) in asciilet:
                #print(f'Index: {i} Letter: {chr(c)}, Key: {j}, Lowc: {l}, xor: {chr(x)}')
                keys[j][l] += 1

    for x in keys:
        print(x)
        print({k: v for k, v in sorted(keys[x].items(), key=lambda item: item[1],reverse=True)})
        sum(keys[x].values())





    


def sum(list):
    sum = 0
    for c in list:
        sum += c
    print(sum)  

def bruteForce(message):
    start = time.time()
    cnt = 0
    answ = []
    try:
        for k1 in lowc:
            
            for k2 in lowc:
                for k3 in lowc:
                    
                    key = k1+k2+k3
                    #print(f'{cnt}', end=",", flush=True)
                    gkey = genkey(message,key)
                    decryptedtext = xor_strings(message,gkey)
                    wrds = "".join(chr(a) for a in decryptedtext).split()
                    cntw = 0
                    for w in wrds[0:10]:
                        if w in words.words():
                            cntw+=1
                    if cntw/10 > 0.7:
                        answ.append(key)


                    cnt +=1
                print("---Total %s seconds ---" % (time.time() - start))
        print(answ)
            
    except:
        print(f'Error #{cnt} and {key}')
                    


                    


if __name__ == "__main__": 

    #print("fine" in words.words())
    # message = "This is a secret message"

    # key = "tes"
    # fkey = "aaa"
    # gkey = genkey(message,key)
    # encryptedtext = xor_strings(message,gkey)
    # print(f'Encrypted: {encryptedtext}')
    # #res = bruteForce(message,3)
    # #print(res)
    # back = xor_strings(encryptedtext,genkey(message,fkey))
    # print(f'Back: {back}')
    # wrds = "".join(chr(a) for a in back).split()
    # print(wrds)
    
    #print(analysis(encryptedtext))

     
    with open("euler59/p059_cipher.txt") as f:
    
        line  = f.readlines()
        message = line[0].split(',')
        
        for ind, m in enumerate(message):
            message[ind] = int(m)
        back = xor_strings(message,genkey(message,genkey(message,"exp")))
        #print(f'Back: {back}')
        wrds = "".join(chr(a) for a in back)
        print(wrds)

        sum(back)


        #bruteForce(message)

    


      







    
       
