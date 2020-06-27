#libraries
import itertools
import os
from nltk.corpus import brown

#functions
def f_txt_to_int(file_name, no_bytes):
    max_bytes = os.path.getsize(file_name)
    if no_bytes > max_bytes:
        no_bytes = max_bytes
    with open(file_name) as f:
        return list(map(int,f.read().split(',')))[:(no_bytes-(no_bytes%key_size))]

def gen_cyphers(range_low, range_high, no_letters):
    return ([p for p in itertools.product(range(range_low,range_high+1), repeat=no_letters)])

def list_split(list, no_elements):
    return [list[x:x + no_elements] for x in range(0, len(list), no_elements)]

def decrypt(split_list,cypher):
    decrypted_elem = list()
    for element in split_list:
        decrypted_txt = ""
        i = 0
        for number in cypher:
            decrypted_elem.append(chr(element[i] ^ number))
            i += 1
        str = ''.join([elem for elem in decrypted_elem])
        decrypted_txt = decrypted_txt + str
    return decrypted_txt

def count_words(words_list):
    count = 0
    for word in words_list:
        if word in all_words:
            count += 1
    return count

def total_ascii_value(text):
    sum = 0
    for c in text:
        sum += ord(c)
    return sum


#init variables
all_words = set()
for word in brown.words():
    all_words.add(word)

file_name = "p059_cipher.txt"
key_size = 3
sample_size = 100
ascii_range_low = 97
ascii_range_high = 122

decrypted_samples = []
words_in_sample = []

cyphers = gen_cyphers(ascii_range_low,ascii_range_high,key_size)
f_sample_split = list_split(f_txt_to_int(file_name,sample_size),key_size)

#main
for cypher in cyphers:
    decr_txt_split = decrypt(f_sample_split,cypher).split()
    decrypted_samples.append(decr_txt_split)
    if len(decr_txt_split) > 5:
        words_in_sample.append(count_words(decr_txt_split))
    else:
        words_in_sample.append(0)

decrypted_file = decrypt(list_split(f_txt_to_int(file_name,os.path.getsize(file_name)),key_size),cyphers[words_in_sample.index(max(words_in_sample))])
decr_ascii_value = total_ascii_value(decrypted_file)

print(decrypted_file)
print("Totasl ASCII value: ", decr_ascii_value)


