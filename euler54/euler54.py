import os

#entries = os.listdir(".")
#print(entries)


#Convert non numeric values to numeric
def valueToNumeric(val):
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
    
    #Process each card in hand and sort it based on value of the card.
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
        
        
def handLToDict(hand):
    
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


        



    

#1Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
def royalFlush(hDict):
    status = False
    for suit in hDict:
        if len(hDict[suit]) == 5:
            if hDict[suit][0] == "T" and hDict[suit][4] == "A":
                status = True
    return status
        



#Function to identify the hand of the player
def whathand(hlist):
    for hand in hlist:
        value = valueToNumeric(hand[0])
        print("Value: " + str(value))
        suit = hand[1]
        

        #Start from highest to lowest.



        #10High Card: Highest value card.
        #9One Pair: Two cards of the same value.
        #8Two Pairs: Two different pairs.
        #7Three of a Kind: Three cards of the same value.
        #6Straight: All cards are consecutive values.
        #5Flush: All cards of the same suit.
        #4Full House: Three of a kind and a pair.
        #3Four of a Kind: Four cards of the same value.
        #2Straight Flush: All cards are consecutive values of same suit.
        
    


#Compare the hands of the player and decide on the winner
def compareHands():
    return


with open("euler54/p054_pokerShort.txt") as f:

    for line in f.readlines():
        game = line.split()
        
        pl1 = game[0:5]
        pl2 = game[5:10]

        print("Player 1: " + str(pl1))
        print(royalFlush(handLToDict(pl1)))

        print("Player 2: " + str(pl2))
       
        print("-------------------------")


        
    





