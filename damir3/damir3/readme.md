# Challenge #3

## Beginners challenge

### Euler 041 - Pandigital prime

Using a loop variable starting with 9 and ending with 3, prime numbers
are looked for with the length of the loop variable.
Max number is returned out of any loop variable long pandigital prime
numbers that are found.

## Experts challenge

### Euler 059 - XOR decryption

Used following english words:
[https://github.com/dwyl/english-words/blob/master/words_alpha.txt]

Method *decode_data* loops through possible 3 letter combinations
of small letters and uses them as a password phrase to execute the
XOR operations on the input string.

Once the decode operations is done, regular expression extracts the
words longer than 2 characters, without digits, that are surrounded
by space, these words are potential words that we are going to compare
with the english dictionary. All words are also extracted using regular
expression with just a word boundaries. Percentage of potential words
against the number of all words found gets compared against the confidence
factor.

At the end, if number of potential words is larger than 4, then all
words get compared with the english words from the dictionary file.
If number of matched words is above 95%, method returns the sum of
the ascii codes of the decoded text.

*Almost all paramters are configurable while creating the Cipher
class object*
