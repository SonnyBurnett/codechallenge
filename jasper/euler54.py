# read all the combined hands from the file into a list
file = open("p054_poker.txt", "r")
all_hands_unsorted = file.read().splitlines()
file.close()

# to keep all the hands after sorting them
all_hands_sorted = []

for hand in all_hands_unsorted:
    # split the hand into player1 and player2
    delt_cards = hand.split(" ")
    cards_plyr1 = delt_cards[:len(delt_cards)//2]
    cards_plyr2 = delt_cards[len(delt_cards)//2:]
    cards_plyrs = [cards_plyr1,cards_plyr2]

    # for every player process the value and suit of the delt cards into the hand of the player
    for plyr in cards_plyrs:

        # list for all possible cards in the hand of a payer including a set for the suits
        hand_plyr = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], set()]

        # for every card turn the card values into integers
        for card in plyr:
            card_val = card[:-1]
            if card_val.isnumeric():
                card_val = int(card_val)
            elif card_val == 'T':
                card_val = 10
            elif card_val == 'J':
                card_val = 11
            elif card_val == 'Q':
                card_val = 12
            elif card_val == 'K':
                card_val = 13
            else:
                card_val = 14
            # add the card value to the player hand in the correct location
            hand_plyr[int(card_val)-1].append(int(card_val))
            # add card suit to the set
            card_suit = card[-1]
            hand_plyr[14].add(card_suit)
        # clean up hand_plyr by removing all the empty lists
        i = 14 # all possible cards cards and the set of suits
        while i >= 0:
            cards_in_hand = hand_plyr[i]
            if len(cards_in_hand) == 0:
                del hand_plyr[i]
            i -= 1
        # add the sorted and cleaned hand to the list
        all_hands_sorted.append(hand_plyr)

# determine value for every hand for plyr1 and plyr 2 then compare and count winner
# 1 suit:           royal flush=9000 or straight flush=8000 or flush=5000
# 2 kinds of cards: for of a kind=7000 or full house 6000
# 3 kinds of cards: three of a kind = 3000 or two pairs = 2000
# 4 kinds of cards: pair = 1000
# 5 kinds of cards: straight = 4000 or nothing = <value highest card>
# for every uneven hand (plyr2) we compare the value with the previous hand (plyr1)

# variables
cnt_plyr = 0
hand_val_prev = 0
win_plyr1 = 0
win_plyr2 = 0
draws = 0

for hand in all_hands_sorted:
    hand_val = 0    # calculated value for hand

    # 1 suit so one of the flushes
    # add value of highest card in case both players have same kind of flush
    if len(hand[len(hand)-1]) == 1:
        hand_val = 5000 + hand[4][0]
        if hand[4][0] - hand[0][0] == 4:        # consecutive order so straight flush
            hand_val += 3000 + hand_val[4][0]
            if hand[4][0] == 14:                # highest card is ace so royal flush
                hand_val += 1000                # !! not specified what to do in case of draw !!

    # 2 kinds of cards so full house or four of a kind
    # add card value in case both players have full house or four of a kind
    elif len(hand)-1 == 2:
        if len(hand[0]) > 2:
            if len(hand[0]) == 4:
                hand_val = 7000 + hand[0][0]
            else:
                hand_val = 6000 + hand[0][0]
        elif len(hand[1]) == 3:
            hand_val = 6000 + hand[1][0]
        else:
            hand_val = 7000 + hand[1][0]

    # 3 kinds of cards so three of a kind or 2 pairs
    # for three of a kind add card value in case both players have three of a kind
    # for two pairs add card value*10 AND the value of the single card in case both players have the same pairs
    # !! not specified what to do in case of a draw !!
    elif len(hand)-1 == 3:
        if len(hand[0]) == 3:
            hand_val += 3000 + hand[0][0]
        elif len(hand[1]) == 3:
            hand_val += 3000 + hand[1][0]
        elif len(hand[2]) == 3:
            hand_val += 3000 + hand[2][0]
        elif len(hand[2]) == 2:
            hand_val += 2000 + (hand[2][0]*10)
            if len(hand[1]) == 2:
                hand_val += (hand[1][0]*10) + hand[0][0]
            else:
                hand_val += (hand[0][0]*10) + hand[1][0]
        else:
            hand_val += 2000 + (hand[1][0]*10) + (hand[0][0]*10) + hand[2][0]

    # 4 kinds of cards so a pair
    # add card value*10 AND the value of the highest single card in case both players have the smae pair.
    # !! not specified what to do on case of a draw !!
    elif len(hand)-1 == 4:
        if len(hand[3]) == 2:
            hand_val += 1000 + (hand[3][0]*10) + hand[2][0]
        elif len(hand[2]) == 2:
            hand_val += 1000 + (hand[2][0]*10) + hand[3][0]
        elif len(hand[1]) == 2:
            hand_val += 1000 + (hand[1][0]*10) + hand[3][0]
        else:
            hand_val += 1000 + (hand[0][0]*10) + hand[3][0]
    # 5 kinds of cards so nothing or a straight
    # add value of highest card in case both players have nothing or a straight
    else:
        if hand[4][0] - hand[0][0] == 4:  # YES a straight
            hand_val += 4000 + hand[4][0]
        else: # take value of highest card
            hand_val += hand[4][0]

    # compare the value of every second hand (plyr2) with the previous hand (plyr1)
    if cnt_plyr % 2 != 0:
        if hand_val == hand_val_prev:
            draws += 1
        elif hand_val < hand_val_prev:
            win_plyr1 += 1
        else:
            win_plyr2 += 1

    # save the value for this hand and up cnt_plyr by one
    hand_val_prev = hand_val
    cnt_plyr += 1

print('wins player 1: ' + str(win_plyr1) + ' wins player 2: ' + str(win_plyr2) + ' draws: ' + str(draws) + ' played_hands: ' + str(int(cnt_plyr/2)))


