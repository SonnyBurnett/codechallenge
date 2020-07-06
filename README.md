# Code Context - EULER 59 problem

[![Build Status](https://dev.azure.com/xmayeur/Euler59/_apis/build/status/xmayeur.euler59?branchName=master)](https://dev.azure.com/xmayeur/Euler59/_build/latest?definitionId=16&branchName=master)



## Problem description
    Your task has been made easy, as the encryption key consists of three lower case characters. 
    Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing 
    the encrypted ASCII codes, and the knowledge that the plain text must contain common English words,
    decrypt the message and find the sum of the ASCII values in the original text.
Link: [Euler59](https://projecteuler.net/problem=59)

## Results
Result is: 129448

![](.images/waldorf_statler.jpg)

    - "Do you really think that this dummy old chap 
    looking like Einstein would ever find the solution?"
    - "I will eat my hat if he does!! Hahaha!"

## Approach
We avoid the brute force approach.
We will try to find the encryption key by analysing the encrypted message.

Each encrypted value corresponds to a character of the clear text original message. 
As the encryption key is only three characters, we will create three stacks of encrypted value,
each stack being XOR'ed by one of the key character.

Then,we will look for the encrypted value occurring the most frequently, in each stack.
And we will assume that this most frequently appearing value matches the most appearing character in the clear text message, which is usually the space character (followed by the 'e' character at least in English language)

So, if we XOR the most frequent encrypted value in each stack with space, we have the most probable key.
Decrypting the crypted message with this key should lead to the text we want to use.

If the test is not readable by a normally constituted human being, understanding common English language, we can try a key using the second most frequent values, or a combination of the first and second most frequent values. But if the method with the most frequent value functions, we will stop there and not develop the code for more complex algorithm.

If the decrypted text is still unreadable, we will try another receipt from the Muppet's Swedish Chef cookbook.

![](.images/swedish_chef.jpg)


# Test
All tests passed:
- testing the encryption/decryption mechanism
- testing the key finding based on analysis
 