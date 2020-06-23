# XOR decryption

## Problem analysis

To XOR bytes we apparently need all ascii characters to consist of the same number of bytes. Now, we can actually look
at wikipedia, see that ASCII chars have 7 bytes and go through the entire encoding. However, we don't really need to I
guess. Instead, we can stay on the level of representing characters as integers (including 0, since that appears in the
cypher) and define the XOR funtion as operation on that group.

Given is that `xor(x, y) = z IFF xor(z, y) = x`, where `y` is a character from the key. Since the key consists of three
characters only, we thus end up we three separate functions `xor_1`, `xor_2` and `xor_3` that bijectively map integers
onto one another. So, `xor_i(x) = z IFF xor_i(z) = x`.

Let's now use out knowledge of the english language, and analyse the frequency of letters in a random english text,
including the space character, and analyse the text.

![letter frequency](/letter-freq.png)

Looking for the letter frequency in english text I also found the occurence statistics of three letters in a row
[here](https://web.archive.org/web/20170918020907/http://www.data-compression.com/english.html), which may be perfect
given that we have a three letter key. However, let's continue with the first order statistics.

## Step 1. 'letter' frequency per mapping function

Given that the key is rotated we know that every third character is mapped by the same mapping function. So, let's see
where we get by analysing the frequency of cyphered chars encoded by each function.
