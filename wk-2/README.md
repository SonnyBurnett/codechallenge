# Solving how many time player 1 wins against player 2 in poker

## Approach

Some boilerplate around reading the lines of course needs to be done. Unit test the called methods instead of an integration test for the main method (which is not needed to prove every responsibility was tested).

Then, for the algorithm we make use of the way Python compares tuples. Python compares tuples similarly to how words are ordered in a dictionary. Thus, we can use the first letter for the main category (high card = 1, pair = 2, two pair = 3, etc.), and then continue with scoring that would only be needed when there is a tie on the higher category.

E.g. comparing a pair of fives against a pair of eights, we get

    (2, 3) < (2, 6)

where 5 and 8 are 'zero-indexed' to 3 and 6 respectively, because the cards ranks range from 2. By adding a third ranking to the tuple we can also account for the follow-up high card on tie: `4D 6S 9H QH QC` and `3D 6D 7H QD QS` become

    (2, 10, 9) > (2, 10, 7)

By scoring a hand in this way, we can easily compare hands to each other.

Note that while in theory more than 3 levels may be needed to assign a winner, executing the algorithm on the exercise's 1000 lines gives the correct answer, from which we can deduce that there are no 'deep ties' in the exercise. Mathematically, for this conclusion you also need the information that our scoring on 3 levels actually works, which is why we have unit tested that thoroughly.

## Answer

`time python solve.py`
Player 1 wins **376** hands
python solve.py  0.05s user 0.01s system 85% cpu 0.062 total
