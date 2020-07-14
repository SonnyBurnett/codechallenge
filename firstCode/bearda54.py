pokerhands = open("p054_poker.txt","r")

#    High Card: Highest value card.                             
#    One Pair: Two cards of the same value.                     
#    Two Pairs: Two different pairs.
#    Three of a Kind: Three cards of the same value.
#    Straight: All cards are consecutive values.
#    Flush: All cards of the same suit.
#    Full House: Three of a kind and a pair.
#    Four of a Kind: Four cards of the same value.
#    Straight Flush: All cards are consecutive values of same suit.
#    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

# scoring as follows:
# One Pair:                       30 points + Card Rank Pair (2-14)
# Two Pairs:                      50 points + 10 * Card Rank Highest Pair + Card Rank Lowest Pair
# Three of a kind:		 300 points + Card Rank
# Straight:                     2000 points + Card Rank
# Flush:                        3000 points + Card Rank
# Full House:                   3500 points + 10 * Card Rank Three + Card Rank Pair
# Four of a Kind:               4000 points + Card Rank
# Straights and Flushes are cumulative, so score 5000 + Card Rank (which makes Royal Flush by definition the largest score)

def flush(hand):  	#determine if the hand is a flush
        if hand.count("C")== 5:
                return True
        if hand.count("D")== 5:
                return True
        if hand.count("H")== 5:
                return True
        if hand.count("S")== 5:
                return True
        return False

def count(hand):        #determine the score due to the rank of the cards
        ToaK = False
        Pairs = 0
        PairLow = 0
        cardranks = "23456789TJQKA"
        
        for i in range(13):
                if hand.count(cardranks[i])== 4:	# Four of a Kind
                        return 4002 + i			# We're done here, no more possibilities to check
                if hand.count(cardranks[i])== 3:	# Three of a Kind, possible Full House	
                        High3 = i + 2
                        ToaK = True
                if hand.count(cardranks[i])== 2:	# Determine number of Pairs
                        Pairs += 1
                        if PairLow == 0:
                                PairLow = 14-i
                        else:
                                PairHigh = 14 - i	# maximum 2 Pairs in 5 Cards
        if ToaK and (Pairs == 1):  			# Full House
                return 3000 + High3 * 10 + PairLow	
        if ToaK:					# Three of a Kind
                return 300 + High3
        if Pairs == 2:					# Two Pairs
                return 50 + PairHigh * 10 + PairLow
        if Pairs == 1:					# One Pair
                return 30 + PairLow

        straight = True					# No combinations, check for straight
        i = 12						# start with the highest possible card
        while cardranks[i] not in hand:
                i -= 1
        for j in range(1,5):
                if cardranks[i-j] not in hand:
                        straight = False
                        break
        if straight:
                return 2002+i
        else:
                return i+2
        
wins1 = 0

for line in pokerhands:
        score1 = 0
        score2 = 0

        suits = []						# initialize for check on flush
        suits2 = []
        for i in range(5):
                suits.append(line[3*i+1])
                suits2.append(line[3*i+16])

        ranks = []						# initialize for check on Four of a Kind, Full House, Three of a Kind, Pairs, High Card
        ranks2 = []
        for i in range(5):
                ranks.append(line[3*i])
                ranks2.append(line[3*i+15])

        score1 = count(ranks)					# Calculate score for hand 1
        if flush(suits):
                score1 += 3000   			

        score2 = count(ranks2)					# Calculate score for hand 2
        if flush(suits2):
                score2 += 3000   

        cardranks = "AKQJT98765432"				# Score can still be equal, need to check for difference, no draw allowed
	i = 0
        while score1 == score2:  				# This can only happen with 1 or 2 pairs or High Card, find the remaining high card
                if ranks.count(cardranks[i])== 1:
                        score1 += (14-i)
                if ranks2.count(cardranks[i])== 1:
                        score2 += (14-i)
		i +=1

        if score1 > score2:
                wins1 += 1

print(wins1)
      
pokerhands.close()
