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
    
    return int(val)

def sortHand(hand):
    '''Processes each card in hand and sorts it based on value of the card. Adapted implementation of bubble sort algorithm'''
    
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
    '''Converts a poker hand {list} into a sorted dictionary based on card values as keys.'''

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
        elif hand[i][0] == "Q":
            vals["Q"].append(hand[i][1])
        elif hand[i][0] == "K":
            vals["K"].append(hand[i][1])
        elif hand[i][0] == "A":
            vals["A"].append(hand[i][1])
    
    return vals




def isConsecutive(hand):
    """Validates the hand on the consecutiveness of the cards. Return True if cards are consecutive and if not return False."""
    consec = True
    for index in enumerate(hand):
        if index[0] < len(hand)-1:
            if valueToNumeric(hand[index[0]][0]) - valueToNumeric(hand[index[0]+1][0]) != -1:
                consec = False
                break
    return consec              

#1Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
def royalFlush(hand):
    '''
    This function accepts a list of a hand. 
    The list is converted to a dictionary with suits as keys.
    Based on it, it checks if the winning hand is a Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    '''
    
    hDict = handLToDictS(hand)
    status = False
    score = 0
    for suit in hDict:
        if len(hDict[suit]) == 5:
            if isConsecutive(sortHand(hand)): 
                if hDict[suit][0] == "T" and hDict[suit][4] == "A":
                    status = True
                    score = [valueToNumeric(card[0]) for card in hand]
    result = [status,score]
    return result


def straight(hand):
    """Straight: All cards are consecutive values."""
    handSorted = sortHand(hand)
    status = False
    score = 0
    if  isConsecutive(handSorted):
        status = True
        score = [valueToNumeric(card[0])+score for card in hand]
    
    result = [status,score]
    return result 


def straightFlush(hand):
    """Straight Flush: All cards are consecutive values of same suit."""
    hDict = handLToDictS(hand)
    status = False
    score = 0
    for suit in hDict:
        if len(hDict[suit]) == 5:

            if  isConsecutive(sortHand(hand)):
                status = True
                score = [valueToNumeric(card[0])+score for card in hand]
                
                        

    result = [status,score]
    return result           
    

def flush(hand):
    """Flush: All cards of the same suit."""

    hDict = handLToDictS(hand)
    status = False
    score = 0
    for suit in hDict:
        if len(hDict[suit]) == 5:
            status = True
            score = [valueToNumeric(card[0])+score for card in hand]
    result = [status,score]
    return result           


def fourOfaKind(hand):
    """Four of a Kind: Four cards of the same value."""

    hDict = handLToDictC(hand)
    status = False
    score = 0
    for cards in hDict:
        if len(hDict[cards]) == 4:
            status = True
            score = [valueToNumeric(card[0])+score for card in hand]
    
    result = [status,score]
    return result



def threeOfaKind(hand):
    """Three of a Kind: Three cards of the same value."""

    hDict = handLToDictC(hand)
    status = False
    score = 0
    for cards in hDict:
        if len(hDict[cards]) == 3:
            status = True
            score = [valueToNumeric(card[0])+score for card in hand]
    result = [status,score]
    return result


def pair(hand):
    """ 
    This functions selects all pairs in a hand.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    """
    
    cardDict = handLToDictC(hand)
    #print(cardDict)
    status = False
    score = []
    for cards in cardDict:
       #print(cards)
       #print(cardDict[cards])
       if len(cardDict[cards]) == 2:
           status = True
           score.append(valueToNumeric(cards)*2)
    result = [status,score]
    return result




def highCard(hand):
    """High Card: Highest value card."""
    handSorted = sortHand(hand)
    status = True
    score = [valueToNumeric(handSorted[4][0])]
    result = [status,score]
    return result



def scoreCalc(scList):
    """Calculates the score of a given hand."""
    score = 0
    for sc in scList:
        score += sc
    return score



def whathand(hlist):
    """This is a main function that identifies the hand of the player"""

    handres = []
    rflush = royalFlush(hlist)
    stflush = straightFlush(hlist)
    fourk = fourOfaKind(hlist)
    threek = threeOfaKind(hlist)
    pairz = pair(hlist)
    flushz = flush(hlist)
    straightz = straight(hlist)
    highc = highCard(hlist)


    if rflush[0]:
        res = []
        res.append(10) #"Royal Flush"
        res.append(scoreCalc(rflush[1]))
        handres.append(res)
    elif stflush[0]:
        res = []
        res.append(9) #"Straight Flush"
        res.append(scoreCalc(stflush[1]))
        handres.append(res)
    elif fourk[0]:
        res = []
        res.append(8) #"Four of a kind"
        res.append(scoreCalc(fourk[1]))
        handres.append(res)    
    elif threek[0] and pairz[0]:
        #4Full House: Three of a kind and a pair.
        res = []
        res.append(7) #"Full house"
        res.append(scoreCalc(threek[1]))
        res.append(scoreCalc(pairz[1]))
        handres.append(res)
    elif flushz[0]:
        res = [] 
        res.append(6) #"Flush"
        res.append(scoreCalc(flushz[1]))
        handres.append(res)
    elif straightz[0]:
        res = []
        res.append(5) #"Straight"
        res.append(scoreCalc(straightz[1]))
        handres.append(res)
    elif threek[0]:
        res = []
        res.append(4) #"Three of a kind"
        res.append(scoreCalc(threek[1]))
        handres.append(res)
    elif pairz[0]:
        res = []
        pairs = pairz[1]
        
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
        res.append(scoreCalc(highc[1]))
        handres.append(res)
    
    return handres
     
def compareHands(hand1, hand2):
    """Compare the hands of the players and decide on the winner"""

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


if __name__ == "__main__": 

    with open("euler54/p054_poker.txt") as f:

        # [0] = Player 1, 
        # [1] = Player 2, 
        # [2] = Draws, 
        # [3] = Errors. 

        gameTotals = [0,0,0,0]
        
        for line in f.readlines():

            game = line.split()
            pl1 = game[0:5]
            pl2 = game[5:10]
            outcome = compareHands(pl1, pl2)

            if outcome[0] == 1:
                gameTotals[0] +=1
            elif outcome[0] == 2:    
                gameTotals[1] +=1
            elif outcome[0] == 0:
                gameTotals[2] +=1
            elif outcome[0] == -1:
                gameTotals[3] +=1
            

    print("Player 1 won: {pl1}, Player 2 won: {pl2}, Draw matches: {draw}, Errors: {errors}".format(pl1 = gameTotals[0], pl2 = gameTotals[1], draw = gameTotals[2], errors = gameTotals[3]))