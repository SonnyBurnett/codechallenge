from string import ascii_lowercase
import urllib
import itertools

common_words = ['and', 'or', 'the']

def get_text():
    # return list of encrypted ascii codes
    enc = urllib2.urlopen("http://projecteuler.net/project/cipher1.txt").read()
    return map(int, enc.strip().split(','))


def password_to_key(passwd, l):
    # given password string, return list of integers as encyrption key of len l
    pass_ascii_codes = map(ord, passwd)
    enc_key = pass_ascii_codes * (l / len(passwd) + 1)
    enc_key = enc_key[:l]
    return enc_key

def euler_59():
    with open("euler59/p059_cipher.txt") as f:
    
        line  = f.readlines()
        message = line[0].split(',')
        
        for ind, m in enumerate(message):
            message[ind] = int(m)
        
        for passwd_str in itertools.permutations(ascii_lowercase, 3):
            enc_key = password_to_key("".join(passwd_str), len(message))
            decyrpted = [x ^ y for x,y in zip(message, enc_key)]
            decyrpted_text = "".join(chr(x) for x in decyrpted)
            if all(x in decyrpted_text
                    for x in ['the', 'and', 'of', 'to', 'it', 'world']):
                print(decyrpted_text)
                print(f'sum of ascii values {sum(decyrpted)}')
    
    
    
    
   
