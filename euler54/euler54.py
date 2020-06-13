import os

#entries = os.listdir(".")
#print(entries)


#Convert non numeric values to numeric
def valueToNumeric(val):
    '''Converts the faces of cards to numeric values'''


    if val == "T":
        val = 10
    elif val == "J":
        val = 11
    elif val == "Q":
        val = 12
    elif val == "K":
        val = 13
    elif val =="A":    
        val = 14
    else:
        val
    
    return int(val)

def sortHand(hand):
    '''Processes each card in hand and sorts it based on value of the card.'''
    
    n = len(hand)
    for i in range(n):
        already_sorted = True


        #print("i: " + str(i)) 
        for j in range(n - i - 1):
            #print("j: " + str(j))
            if valueToNumeric(hand[j][0]) > valueToNumeric(hand[j + 1][0]):
                #print("Greater than")
                hand[j], hand[j + 1] = hand[j + 1], hand[j]
                already_sorted = False
        if already_sorted:
            break
    return hand
        
        
def handLToDictS(hand):
    '''Converts a poker hand {list} into a sorted dictionary based on suits as keys.'''

    hand = sortHand(hand)

    
    suits = {
        
        "h" : [], 
        "d" : [],
        "s" : [], 
        "c" : [] 
    }
    
    n = len(hand)
    for i in range(n):
        if hand[i][1] == "H":
            suits["h"].append(hand[i][0])
        elif hand[i][1] == "D":
            suits["d"].append(hand[i][0])
        elif hand[i][1] == "S":
            suits["s"].append(hand[i][0])
        elif hand[i][1] == "C":
            suits["c"].append(hand[i][0])
    
    return suits


def handLToDictC(hand):
    '''Converts a poker hand {list} into a sorted dictionary based on suits as keys.'''

    hand = sortHand(hand)

    
    vals = {
        
        "2" : [], 
        "3" : [],
        "4" : [], 
        "5" : [], 
        "6" : [],
        "7" : [],
        "8" : [],
        "9" : [],
        "T" : [],
        "J" : [],
        "Q" : [],
        "K" : [],
        "A" : [] 
    }
    
    n = len(hand)
    for i in range(n):
        if hand[i][0] == "2":
            vals["2"].append(hand[i][1])
        elif hand[i][0] == "3":
            vals["3"].append(hand[i][1])
        elif hand[i][0] == "4":
            vals["4"].append(hand[i][1])
        elif hand[i][0] == "5":
            vals["5"].append(hand[i][1])
        elif hand[i][0] == "6":
            vals["6"].append(hand[i][1])
        elif hand[i][0] == "7":
            vals["7"].append(hand[i][1])
        elif hand[i][0] == "8":
            vals["8"].append(hand[i][1])
        elif hand[i][0] == "9":
            vals["9"].append(hand[i][1])
        elif hand[i][0] == "T":
            vals["T"].append(hand[i][1])
        elif hand[i][0] == "J":
            vals["J"].append(hand[i][1])
        elif hand[i][0] == "K":
            vals["K"].append(hand[i][1])
        elif hand[i][0] == "A":
            vals["A"].append(hand[i][1])
    
    return vals



        

   #Start from highest to lowest.
        
        
        
        
        
        
        
        

    

#1Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
def royalFlush(hand):
    '''
    This function accepts a list of a hand. 
    The list is converted to a dictionary with suits as keys.
    Based on it it checks if the winning hand is a Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    '''
    
    hDict = handLToDictS(hand)
    status = False
    score = 0
    for suit in hDict:
        if len(hDict[suit]) == 5:
            if hDict[suit][0] == "T" and hDict[suit][4] == "A":
                status = True
                score = [valueToNumeric(card[0]) for card in hand]
    result = [status,score]
    return result

#6Straight: All cards are consecutive values.
def straight(hand):
    handSorted = sortHand(hand)
    status = False
    score = 0
    #print("Straight check: " + str(valueToNumeric(handSorted[0][0]) - valueToNumeric(handSorted[4][0])))
    if  valueToNumeric(handSorted[4][0]) - valueToNumeric(handSorted[0][0]) == 4:
        status = True
        score = [valueToNumeric(card[0])+score for card in hand]
    
    result = [status,score]
    return result 



#2Straight Flush: All cards are consecutive values of same suit.
def straightFlush(hand):
    
    hDict = handLToDictS(hand)
    status = False
    score = 0
    for suit in hDict:
        if len(hDict[suit]) == 5:
            if hDict[suit][0] != "T":
                if  valueToNumeric(hDict[suit][4]) - valueToNumeric(hDict[suit][0]) == 4:
                   
                    status = True
                    score = [valueToNumeric(card[0])+score for card in hand]
                    
                        

    result = [status,score]
    return result           
    

#5Flush: All cards of the same suit.
def flush(hand):
    
    hDict = handLToDictS(hand)
    status = False
    score = 0
    for suit in hDict:
        if len(hDict[suit]) == 5:
            if hDict[suit][0] != "T":
                #print(valueToNumeric(hDict[suit][4]) - valueToNumeric(hDict[suit][0]))
                if  valueToNumeric(hDict[suit][4]) - valueToNumeric(hDict[suit][0]) != 4:
                   
                   status = True
                   score = [valueToNumeric(card[0])+score for card in hand]
               
    result = [status,score]
    return result           

#3Four of a Kind: Four cards of the same value.
def fourOfaKind(hand):
    
    hDict = handLToDictC(hand)
    status = False
    score = 0
    for cards in hDict:
        if len(hDict[cards]) == 4:
            status = True
            score = [valueToNumeric(card[0])+score for card in hand]
    
    result = [status,score]
    return result


#7Three of a Kind: Three cards of the same value.
def threeOfaKind(hand):
    
    hDict = handLToDictC(hand)
    status = False
    score = 0
    for cards in hDict:
        if len(hDict[cards]) == 3:
            status = True
            score = [valueToNumeric(card[0])+score for card in hand]
    result = [status,score]
    return result


#4Full House: Three of a kind and a pair.





#8Two Pairs: Two different pairs.
#9One Pair: Two cards of the same value.
def pair(hand):
    
    cardDict = handLToDictC(hand)
    status = False
    score = []
    pairs = []
    for cards in cardDict:
       #print(cards)
       if len(cardDict[cards]) == 2:
           status = True
           score.append(valueToNumeric(cards)*2)
    result = [status,score]
    return result



#10High Card: Highest value card.
def highCard(hand):
    handSorted = sortHand(hand)
    status = True
    score = [valueToNumeric(handSorted[4][0])]
    result = [status,score]
    return result



def scoreCalc(scList):
    score = 0
    for sc in scList:
        score += sc
    return score


#Function to identify the hand of the player
def whathand(hlist):
    
    score = 0
    handres = []

    if royalFlush(hlist)[0]:
        res = []
        res.append(10) #"Royal Flush"
        res.append(scoreCalc(royalFlush(hlist)[1]))
        handres.append(res)
    elif straightFlush(hlist)[0]:
        res = []
        res.append(9) #"Straight Flush"
        res.append(scoreCalc(straightFlush(hlist)[1]))
        handres.append(res)
    elif fourOfaKind(hlist)[0]:
        res = []
        res.append(8) #"Four of a kind"
        res.append(scoreCalc(fourOfaKind(hlist)[1]))
        handres.append(res)    
    elif threeOfaKind(hlist)[0] and pair(hlist)[0]:
        #4Full House: Three of a kind and a pair.
        res = []
        res.append(7) #"Full house"
        res.append(scoreCalc(threeOfaKind(hlist)[1]))
        res.append(scoreCalc(pair(hlist)[1]))
        handres.append(res)
    
    
    elif flush(hlist)[0]:
        res = [] 
        res.append(6) #"Flush"
        res.append(scoreCalc(flush(hlist)[1]))
        handres.append(res)
    elif straight(hlist)[0]:
        res = []
        res.append(5) #"Straight"
        res.append(scoreCalc(straight(hlist)[1]))
        handres.append(res)
    
    
    elif threeOfaKind(hlist)[0]:
        res = []
        res.append(4) #"Three of a kind"
        res.append(scoreCalc(threeOfaKind(hlist)[1]))
        handres.append(res)
    
    
    elif pair(hlist)[0]:
        res = []
        pairs = pair(hlist)[1]
        
        if len(pairs) == 2:
            res.append(3) #"Two Pairs"
            res.append(scoreCalc(pairs))
        else:
            res.append(2) #"Pair"
            res.append(scoreCalc(pairs))

        handres.append(res)
    
    
    else:
        res = []
        res.append(1) #"High card"
        res.append(scoreCalc(highCard(hlist)[1]))
        handres.append(res)
    return handres
     
        
    


#Compare the hands of the player and decide on the winner
def compareHands(hand1, hand2):
    
    player1 = whathand(hand1)
    player2 = whathand(hand2)

    res = []

    if player1[0][0] > player2[0][0]:
        res.append(1) #"Player 1 won!"
    elif player1[0][0] < player2[0][0]:
        res.append(2)  #"Player 2 won!"
    elif player1[0][0] == player2[0][0]:
        if player1[0][1] > player2[0][1]:
            res.append(1) #"Player 1 won!"
        elif player1[0][1] < player2[0][1]:
            res.append(2)  #"Player 2 won!"
        else:
            res.append(0) #"It is a draw"
    
    else:
        res.append(-1) #Something is wrong

    return res




with open("euler54/p054_poker.txt") as f:


    cntpl1 = 0
    cntpl2 = 0
    drw = 0
    er = 0

    for line in f.readlines():
        game = line.split()
        
        pl1 = game[0:5]
        pl2 = game[5:10]

        #print("Player 1: " + str(pl1))
        #print(whathand(pl1))
        #print(highCard(pl1))
        
        #print("Player 2: " + str(pl2))
        #print(whathand(pl2))

        outcome = compareHands(pl1, pl2)
        #print(outcome)

        if outcome[0] == 1:
            cntpl1 +=1
        elif outcome[0] == 2:
            cntpl2 +=1
        elif outcome[0] == 0:
            drw +=1
        elif outcome[0] == -1:
            er +=1
        

print("Player 1 won: {pl1}, Player 2 won: {pl2}, Draw matches: {draw}, Errors: {errors}".format(pl1 = cntpl1, pl2 = cntpl2, draw = drw, errors = er))

    





