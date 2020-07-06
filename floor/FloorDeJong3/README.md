<h1> XOR decryption</h1>

Solution Euler challenge 59: XOR decryption.

xor_decrypt_encrypt_ascii_list is the method to decrypt the data. 

| Variable | Description |
| -------- |:-----------:|
| Input_data | List of ASCII values |
| key | Key used for the decryption | 

To check whether text is English, two methods can be used.
1. is_english checks how many of the words of a list of 100 common words are present in the text.
It returns the number of common words that where present. Pitfall: if a text does not have any of these common words, 
but is correct english, the score will be zero.
2. is_english1 uses enchant package, which can check every word that is in the text.
It returns the number of english words found. This method is more accurate, however, it is very 
slow. For this reason, is not used. 

decrypt_using_three_lower_letters is the method that decrypts the data using three lower letter characters. 
Per key the number of english words in the decrypted text is calculated, and the one with the highest score is the 
decrypted text.

<h3> Tests  </h3>

