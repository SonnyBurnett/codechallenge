import os

#entries = os.listdir(".")
#print(entries)

with open("euler54/p054_poker.txt") as f:

    for line in f.readlines():
        game = line.split()
        
        pl1 = game[0:5]
        pl2 = game[5:10]

        print("Player 1: " + str(pl1))
        print("Player 2: " + str(pl2))
        print("-------------------------")

    





