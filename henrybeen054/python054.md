This exercise has cost me a good amount of time. Learning all new kinds of Python thingies and some stuff about poker
that I never knew.

### Approach
I did not want to approach this problem by finding an algorithm only for comparing hands, as that would be a very 
narrow solution that would be very hard to use in other situations. And as for all comparisons, their implementation is
trivial if you have a way to value all elements in the comparison individually. Conclusion: I wanted to build a way for
scoring the individual hands into an integer, from which the comparison would be trivial.

### Scoring hands
For scoring the hands, it was quickly clear that I had to find a way for scoring each hand on two levels: the type of
the hand (flush, straight, pair, etc) and the score of the individual cards. This would yield an array of six integers,
all with a value smaller than sixteen. Shifting those 5..0 times by two bytes ( or multiplying by the powers 5 .. 0 of 
16 ) would yield a single integer value where the part of the scoring that needs to be the most important is shifted
into the most significant bits, allowing for a simple integer representing the score of that hand. 

### Scoring the hand types
For scoring the hand types, I wrote out all the combinations possible for an hand type, like this:
* 1, 1, 1, 1, 1 (High card)
* 2, 1, 1, 1 (Pair)
* 2, 2, 1 (2 Pair)
* etc

Looking at this list, it can be seen that the first two values for every combination, uniquely qualify the hand pair.
Applying shifting by three bits ( multiplication by powers of eight), this can also score the hand types for all hands
that are not a straight or a flush.

To incorporate the straight and the flush, I concluded that I would take the three left-most columns of the table above
so that the scores for three of a kind become (3,1,1) and full house (3,2) - allowing me to hard code the values (3,1,3)
and (3,1,4) for the straight and the flush. Also, the value (4,2) can be used for the straight flush.
 

### Tweaking the scoring of individual cards
For scoring the individual cards, I just sorted all the values and applied the multiplication. During testing I found a
bug in this implementation. Given a hand 2C 2S 3H 6C 9C, this would give precedence to the nine as it is higher, while
it should give precedence to the two, as this is the highest value in the 'hand type' I worked around this by sorting
all cards in a dictionary, first by the number of occurrences, then by their actual value. 


### Wrapping up
To complete the solution, I factored the parsing and running of the game out in a seperate class, so that I could write
a good test for the whole solution.

Next, I wrote this file 