'''
https://projecteuler.net/problem=54

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins;
for example, a pair of eights beats a pair of fives (see example 1 below). 
But if two ranks tie, for example, both players have a pair of queens, then highest cards 
in each hand are compared (see example 4 below); if the highest cards tie 
then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand    Player 1      Player 2            Winner
1   5H 5C 6S 7S KD    2C 3S 8S 8D TD
    Pair of Fives     Pair of Eights 	    Player 2
2   5D 8C 9S JS AC    2C 5C 7D 8S QH
    Highest card Ace  Highest card Queen  Player 1
3   2D 9C AS AH AC    3D 6D 7D TD QD
    Three Aces        Flush with Diamonds Player 2
4	 	4D 6S 9H QH QC    3D 6D 7H QD QS
    Pair of Queens    Pair of Queens
    Highest card Nine Highest card Seven  Player 1
5   2H 2D 4C 4D 4S    3C 3D 3S 9S 9D
    Full House        Full House
    With Three Fours  with Three Threes   Player 1
 	
The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space):
the first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid (no invalid characters or repeated
cards), each player's hand is in no specific order, and in each hand
there is a clear winner.

How many hands does Player 1 win?
'''
class PlayerHand:
  def __init__(self, round_of_cards):
    self._seen = None
    self._dupes = None
    self._values = []
    self._colors = []
    self.cards_values = {}
    self.cards = self.read_hand(round_of_cards)
    self.calculate_highest_value()

  def get_card_value(self, card):
    try:
      return int(card)
    except:
      translation = {
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
      }
      return translation.get(card)

  def read_hand(self, round_of_cards):
    cards = []
    seen = {}
    dupes = []
    for c in round_of_cards.split():
      v = self.get_card_value(c[0])
      self._values.append(v)
      self._colors.append(c[1])

      #calc - do we have a pair?
      if v not in seen:
          seen[v] = 1
      else:
        if seen[v] == 1:
          dupes.append(v)
        seen[v] += 1
    
    self._seen = seen
    self._dupes = dupes
    return cards
  
  def get_highest_card(self):
    return max(self._values)
  
  def calculate_highest_value(self):
    '''
    this should calculate the highest value of all cards
    0 - High Card: Highest value card.
    1 - One Pair: Two cards of the same value.
    2 - Two Pairs: Two different pairs.
    3 - Three of a Kind: Three cards of the same value.
    4 - Straight: All cards are consecutive values.
    5 - Flush: All cards of the same suit.
    6 - Full House: Three of a kind and a pair.
    7 - Four of a Kind: Four cards of the same value.
    8 - Straight Flush: All cards are consecutive values of same suit.
    9 - Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    '''
    self.cards_values[0] = self.get_highest_card()
    #get pairs, three, four
    for dupe in self._dupes:
      if self._seen[dupe] == 2:
        if 1 not in self.cards_values:
          self.cards_values[1] = [dupe] #One Pair
        else:
          self.cards_values[1].append(dupe) #Two Pairs
      elif self._seen[dupe] == 3: #Three of a Kind
        self.cards_values[3] = dupe
      elif self._seen[dupe] == 4: #Four of a Kind
        self.cards_values[7] == dupe
    #two pairs?
    if 1 in self.cards_values and len(self.cards_values[1]) == 2:
      self.cards_values[2] = self.cards_values[1][0] if self.cards_values[1][0] > self.cards_values[1][1] else self.cards_values[1][1]
    #straight
    if len(self._values) == len(set(self._values)):
      if sorted(self._values) == list(range(min(self._values), max(self._values) + 1)):
        self.cards_values[4] = self.cards_values[0]
    #flush
    if len(set(self._colors)) == 1:
      self.cards_values[5] = self.cards_values[0] #Get a value of highest card
    #Full House
    if 3 in self.cards_values and 1 in self.cards_values:
      self.cards_values[6] = self.cards_values[3] #Get the value of Three of a Kind
    #Straight Flush
    if 4 in self.cards_values and 5 in self.cards_values:
      self.cards_values = self.cards_values[0]
      #Do we have a Royal FLush???
      if self.cards_values[0] == 14:
        self.cards_values[9] = 14

    self.highest_value = max(self.cards_values)

class Hand:
  def __init__(self, round_of_cards):
    self.hand1 = PlayerHand(round_of_cards[:14])
    self.hand2 = PlayerHand(round_of_cards[15:])

  def did_player1_win(self):
    if self.hand1.highest_value > self.hand2.highest_value:
      return True
    elif self.hand1.highest_value == self.hand2.highest_value:
      if self.hand1.cards_values[self.hand1.highest_value] > self.hand2.cards_values[self.hand2.highest_value]:
        return True
    return False


f = open('54-poker.txt')
line = f.readline()
p1_wins = 0

while line:
  print(line)
  hand = Hand(line)
  if hand.did_player1_win():
    p1_wins += 1
    print('Player1 wins this round')
  
  #read next line
  line = f.readline()

print('Player1 wins {} times!'.format(p1_wins))

f.close()
