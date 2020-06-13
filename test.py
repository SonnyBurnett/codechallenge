#creat a prime factorizor

def primeFactorizer(n):
    primesFactList = [2]

    remainder = 1
    for prime in primesFactList:
        if n % prime
        



for card in hand:
            # Continue untill there are no cards in hand.
            if cnt != 4:
                print("Comparing " + str(card) + " and " + str(hand[cnt+1]))
                if valueToNumeric(card[0]) > valueToNumeric(hand[cnt+1][0]):
                    print(str(valueToNumeric(card[0])) + " > " + str(valueToNumeric(hand[cnt+1][0])))
                    tmp = hand[cnt+1]
                    print(tmp)
                    hand[cnt+1] = hand[cnt]
                    print(hand[cnt+1])
                    hand[cnt] = tmp
                    print(hand[cnt])
                else:
                    print("Not greater")
                #print(card[0] + ": " + str(type(valueToNumeric(card[0]))))
                #print(hand[cnt+1][0] + ": " + str(type(valueToNumeric(hand[cnt+1][0]))))
            else:
                print("Out of cards to compare")
            cnt +=1
        print(hand)    


for j in range(n - i - 1):
            if valueToNumeric(hand[j]) > valueToNumeric(hand[j + 1]):
                hand[j], hand[j + 1] = hand[j + 1], hand[j]
                already_sorted = False
            if already_sorted:
                break
        return hand