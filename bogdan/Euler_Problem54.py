import itertools
import os.path
import time

Straight = '1234567899192939495'
test_straight = ''
player_one_wins = 0
player_two_wins = 0
cards = "poker.txt"
if os.path.exists(cards):
   f = open(cards, "r")
   for x in f:
       player_one_cards = []
       player_one_cards_suit = []
       player_two_cards = []
       player_two_cards_suit = []
       player_one_cards.extend((x[0],x[3],x[6],x[9],x[12]))
       player_one_cards = [w.replace('T','91').replace('K','94').replace('J','92').replace('Q','93').replace('A','95') for w in player_one_cards]
       player_one_cards.sort()
       player_one_cards_suit.extend((x[1],x[4],x[7],x[10],x[13]))
       player_two_cards.extend((x[15],x[18],x[21],x[24],x[27]))
       player_two_cards = [w.replace('T','91').replace('K','94').replace('J','92').replace('Q','93').replace('A','95') for w in player_two_cards]
       player_two_cards.sort()
       player_two_cards_suit.extend((x[16],x[19],x[22],x[25],x[28]))
       test_player_one = ([(x,y) for x,y in itertools.combinations(player_one_cards, 2) if x == y])
       test_player_two = ([(x,y) for x,y in itertools.combinations(player_two_cards, 2) if x == y])


       if test_straight.join(player_one_cards) in Straight and player_one_cards[0] == '91' and player_one_cards_suit[0] == player_one_cards_suit[1] == player_one_cards_suit[2] == player_one_cards_suit[3] == player_one_cards_suit[4]:
            print (" Player one hand is Royal Flush")
            player_one_hand = 10
       elif test_straight.join(player_one_cards) in Straight and player_one_cards[0] != '91' and player_one_cards_suit[0] == player_one_cards_suit[1] == player_one_cards_suit[2] == player_one_cards_suit[3] == player_one_cards_suit[4]:
            print ("Player one hand is Straight Flush")
            player_one_hand = 9
       elif len(test_player_one) == 6:
            player_one_hand = 8
            print ("Player one hand is Four of a Kind")
       elif len(test_player_one) == 4:
            print ("Player one hand is Full House")
            player_one_hand = 6
       elif player_one_cards_suit[0] == player_one_cards_suit[1] == player_one_cards_suit[2] == player_one_cards_suit[3] == player_one_cards_suit[4] and player_one_cards[0] != player_one_cards[1]:
            print ("Player one hand is Flush")
            player_one_hand = 5
       elif test_straight.join(player_one_cards) in Straight: 
            print ("Player one hand is Straight")
            player_one_hand = 4
       elif len(test_player_one) == 3:
            print ("Player one hand is Three of a Kind")
            player_one_hand = 3
       elif len(test_player_one) == 2:
            print ("Player one hand is Two pairs")
            player_one_hand = 2
       elif len(test_player_one) == 1:
            print ("Player one hand is One pair")
            player_one_hand = 1
       elif len(test_player_one) == 0:
            print ("Player one hand is High Card", max(player_one_cards))
            player_one_hand = 0

       if test_straight.join(player_two_cards) in Straight and player_two_cards[0] == '91' and player_two_cards_suit[0] == player_two_cards_suit[1] == player_two_cards_suit[2] == player_two_cards_suit[3] == player_two_cards_suit[4]:
            print (" Player two hand is Royal Flush")
            player_two_hand = 10
       elif test_straight.join(player_two_cards) in Straight and player_two_cards[0] != '91' and player_two_cards_suit[0] == player_two_cards_suit[1] == player_two_cards_suit[2] == player_two_cards_suit[3] == player_two_cards_suit[4]:
            print ("Player two hand is Straight Flush")
            player_two_hand = 9
       elif len(test_player_two) == 6:
            player_two_hand = 8
            print ("Player two hand is Four of a Kind")
       elif len(test_player_two) == 4:
            print ("Player two hand is Full House")
            player_two_hand = 6
       elif player_two_cards_suit[0] == player_two_cards_suit[1] == player_two_cards_suit[2] == player_two_cards_suit[3] == player_two_cards_suit[4] and player_two_cards[0] != player_two_cards[1]:
            print ("Player two hand is Flush")
            player_two_hand = 5
       elif test_straight.join(player_two_cards) in Straight: 
            print ("Player two hand is Straight")
            player_two_hand = 4
       elif len(test_player_two) == 3:
            print ("Player two hand is Three of a Kind")
            player_two_hand = 3
       elif len(test_player_two) == 2:
            print ("Player two hand is Two pairs")
            player_two_hand = 2
       elif len(test_player_two) == 1:
            print ("Player two hand is One pair")
            player_two_hand = 1
       elif len(test_player_two) == 0:
            print ("Player two hand is High Card", max(player_two_cards))
            player_two_hand = 0

       if player_one_hand > player_two_hand:
           print ("Player one wins")
           player_one_wins += 1
           print ("Player one victories =", player_one_wins)
       elif player_two_hand > player_one_hand:
           print ("Player two wins")
           player_two_wins += 1
           print ("Player two victories =", player_two_wins)
       elif player_one_hand == player_two_hand:
           if player_one_hand == 1:
               if test_player_one[0] > test_player_two[0]:
                   print ("Player one wins")
                   player_one_wins += 1
                   print ("Player one victories =", player_one_wins)
               elif test_player_one[0] < test_player_two[0]:
                   print ("Player two wins")
                   player_two_wins += 1
                   print ("Player two victories =", player_two_wins)
               elif test_player_one[0] == test_player_two[0]:
                       for y in range(4,0,-1):
                        if player_one_cards[y] == player_two_cards[y]:
                            print ("Equality")
                        elif player_one_cards[y] > player_two_cards[y]:
                            print ("Player one wins")
                            player_one_wins += 1
                            print ("Player one victories =", player_one_wins)
                            break
                        elif player_one_cards[y] < player_two_cards[y]:
                            print ("Player two wins")
                            player_two_wins += 1
                            print ("Player two victories =", player_two_wins)
                            break
           elif player_one_hand == 0:
               for y in range(4,0,-1):
                        if player_one_cards[y] == player_two_cards[y]:
                            print ("Equality")
                        elif player_one_cards[y] > player_two_cards[y]:
                            print ("Player one wins")
                            player_one_wins += 1
                            print ("Player one victories =", player_one_wins)
                            break
                        elif player_one_cards[y] < player_two_cards[y]:
                            print ("Player two wins")
                            player_two_wins += 1
                            print ("Player two victories =", player_two_wins)
                            break
                
           elif player_one_hand == 2:
                    if max(test_player_one) > max(test_player_two):
                           print ("Player one wins")
                           player_one_wins += 1
                           print ("Player one victories =", player_one_wins)
                    elif max(test_player_one) < max(test_player_two):
                           print ("Player two wins")
                           player_two_wins += 1
                           print ("Player two victories =", player_two_wins)
                    elif min(test_player_one) > min(test_player_two):
                           print ("Player one wins")
                           player_one_wins += 1
                           print ("Player one victories =", player_one_wins)
                    elif min(test_player_one) < min(test_player_two):
                           print ("Player two wins")
                           player_two_wins += 1
                           print ("Player two victories =", player_two_wins)
                    elif min(test_player_one) == min(test_player_two):
                       for y in range(4,0,-1):
                        if player_one_cards[y] == player_two_cards[y]:
                            print ("Equality")
                        elif player_one_cards[y] > player_two_cards[y]:
                            print ("Player one wins")
                            player_one_wins += 1
                            print ("Player one victories =", player_one_wins)
                            break
                        elif player_one_cards[y] < player_two_cards[y]:
                            print ("Player two wins")
                            player_two_wins += 1
                            print ("Player two victories =", player_two_wins)
                            break
           elif player_one_hand == 3:
                   if max(test_player_one) > max(test_player_two):
                           print ("Player one wins")
                           player_one_wins += 1
                           print ("Player one victories =", player_one_wins)
                   elif max(test_player_one) < max(test_player_two):
                           print ("Player two wins")
                           player_two_wins += 1
                           print ("Player two victories =", player_two_wins)
                   elif max(test_player_one) == max(test_player_two):
                       for y in range(4,0,-1):
                        if player_one_cards[y] == player_two_cards[y]:
                            print ("Equality")
                        elif player_one_cards[y] > player_two_cards[y]:
                            print ("Player one wins")
                            player_one_wins += 1
                            print ("Player one victories =", player_one_wins)
                            break
                        elif player_one_cards[y] < player_two_cards[y]:
                            print ("Player two wins")
                            player_two_wins += 1
                            print ("Player two victories =", player_two_wins)
                            break 
           elif player_one_hand == 6:
                   if  test_player_one[2] > test_player_two[2]:
                       print ("Player one wins")
                       player_one_wins += 1
                       print ("Player one victories =", player_one_wins)
                   else:
                       print ("Player two wins")
                       player_two_wins += 1
                       print ("Player two victories =", player_two_wins)
           elif player_one_hand == 8:
                   if test_player_one[0] > test_player_two[0]:
                           print ("Player one wins")
                           player_one_wins += 1
                           print ("Player one victories =", player_one_wins)
                   else:
                           print ("Player two wins")
                           player_two_wins += 1
                           print ("Player two victories =", player_two_wins)
       time.sleep(3)         
else:
    print("File poker.txt is missing. Please copy the file to same path as script")


