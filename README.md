# bogdan_manolache
Euler 54 / Poker problem :
Euler problem 54. 
File poker.txt must be copied to same path from where the script is executed. 
I'm reading lines one by one and I’m using 4 lists for players hand evaluation.
For easier evaluation I’m replacing letters to numbers.
For hands evaluation I’m using itertools.combinations to find how many similar cards has each player.
Then I’m using 2 ‘if’ statements to translate each player hand to poker game ranks and assign a value:
Royal Flush = 10
Straight Flush = 9
Four of a Kind = 8
Four of a Kind = 6
Flush = 5
Straight = 4
Three of a Kind = 3
Two pairs = 2
One pair = 1
High Card = 0
  
 Next is a final if statement to compare player hands and count victories. If player hands are equal then I’m testing next highest cards. 
‘Sleep’ was added specially for my testing part to make sure hands rank is evaluated correctly. 
