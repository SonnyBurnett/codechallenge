The approach I have taken for this exercise is straightforward. After all, it is barbecue weather these weeks.

### Approach
My approach iterates all possible keys, generating all possible solutions. Each solution is stored and then all 
solutions are sorted by the probability of them being correct. A few heuristics I could think of were:
* Picking the generated text with the largest number of letters
* Followed by, picking the text which has the most realistic distribution of letters (f.e. by ordering all letters by 
their occurrencee count and comparing that to the know ordered distribution of letters, taking the levenshtein 
distance)
* Applying a dictionary check on the outcome 

In this case and my other test case, the first heuristic was good enough and the weather was great.

### Possible improvements
For larger problem spaces, it might quickly become necessary to prune the solutions array of definite non-answers
every X solutions to prevent an out of memory. This is trivial if the problem ever arises.

Also, heuristics can be applied to key generation. for example, frequency tables can be used to generate a number of
highly likely keys based on a 1 to 1 mapping from encrypted letter to unencrypted letter.
