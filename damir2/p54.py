'''
https://projecteuler.net/problem=54

In the card game poker, a hand consists of five cards and are ranked,
from lowest to highest, in the following way:

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

If two players have the same ranked hands then the rank made up of
the highest value wins; for example, a pair of eights beats a pair
of fives (see example 1 below). But if two ranks tie, for example,
both players have a pair of queens, then highest cards in each hand
are compared (see example 4 below); if the highest cards tie
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
import os


class PlayerHand:
  '''
  Class containing a single players cards
  parses the cards and determines the values of the cards
  '''
  def __init__(self, round_of_cards):
    self._seen = None
    self._duplicates = None
    self._values = []
    self._colors = []
    self.cards_values = {}
    self.cards = self.__read_hand(round_of_cards)
    self.__evaluate_hand()

  @classmethod
  def __get_card_value(cls, card):
    if card.capitalize() not in '123456789TJQKA':
      raise ValueError('Card not recognized! Allowed values: 1,...,9,T,J,Q,K,A')

    translation = {
        '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }

    return translation.get(card.capitalize())

  def __read_hand(self, round_of_cards):
    if len(round_of_cards.split()) != 5:
      raise ValueError('Wrong input for the players hand. Expecting 5 cards!')
    cards = []
    seen = {}
    duplicates = []
    for card in round_of_cards.split():
      card_value = self.__get_card_value(card[0])
      self._values.append(card_value)
      self._colors.append(card[1].capitalize())

      if card_value not in seen:
          seen[card_value] = 1
      else:
        if seen[card_value] == 1:
          duplicates.append(card_value)
        seen[card_value] += 1

    self._seen = seen
    self._duplicates = duplicates
    return cards

  def __evaluate_hand(self):
    '''
    this should calculate the highest value of all cards with following value
    assignments. It is possible to have combinations of values.
    Function returns a dictionary with one or more keys
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
    self.cards_values[0] = max(self._values)
    # get pair, two pairs, three, four
    for duplicate in self._duplicates:
      if self._seen[duplicate] == 2:
        if 1 not in self.cards_values:
          self.cards_values[1] = [duplicate]  # One Pair
          self.cards_values[0] = max([x for x in self._values if x != duplicate])
        else:
          self.cards_values[1].append(duplicate)  # Two Pairs
          self.cards_values[0] = max([x for x in self._values if x not in self._duplicates])
      elif self._seen[duplicate] == 3:  # Three of a Kind
        self.cards_values[3] = duplicate
      elif self._seen[duplicate] == 4:  # Four of a Kind
        self.cards_values[7] == duplicate
    # two pairs?
    if 1 in self.cards_values and len(self.cards_values[1]) == 2:
      self.cards_values[2] = self.cards_values[1][0] if self.cards_values[1][0] > self.cards_values[1][1] else self.cards_values[1][1]
    # straight
    if len(self._values) == len(set(self._values)):
      if sorted(self._values) == list(range(min(self._values), max(self._values) + 1)):
        self.cards_values[4] = self.cards_values[0]
    # flush
    if len(set(self._colors)) == 1:
      self.cards_values[5] = self.cards_values[0]  # Get a value of highest card
    # Full House
    if 3 in self.cards_values and 1 in self.cards_values:
      self.cards_values[6] = self.cards_values[3]  # Get the value of Three of a Kind
    # Straight Flush
    if 4 in self.cards_values and 5 in self.cards_values:
      self.cards_values = self.cards_values[0]
      # Royal FLush
      if self.cards_values[0] == 14:
        self.cards_values[9] = 14

    self.highest_value = max(self.cards_values)

  def __gt__(self, other):
    if self.highest_value > other.highest_value:
      return True
    if self.highest_value == other.highest_value:
      if self.cards_values[self.highest_value] > other.cards_values[other.highest_value]:
        return True
      if self.cards_values[self.highest_value] == other.cards_values[other.highest_value] \
         and self.cards_values[0] > other.cards_values[0]:
          return True
    return False


class OneRound:
  def __init__(self, round_of_cards):
    self.hand1 = PlayerHand(round_of_cards[:14])
    self.hand2 = PlayerHand(round_of_cards[15:])

  def did_player1_win(self):
    return self.hand1 > self.hand2


class Poker():
  def __init__(self, filename='', poker_hands=None):
    self._location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    self.player1_wins = 0
    if len(filename) > 0:
      self.process_data_from_file(filename)
    if poker_hands is not None and len(poker_hands) > 0:
      self.process_data_from_poker_hands(poker_hands)

  def process_data_from_poker_hands(self, poker_hands):
    if not isinstance(poker_hands, (str, list)):
      raise TypeError("Wrong type for poker_hands. Expected str or list of str")
    if isinstance(poker_hands, list):
      for line in poker_hands:
        self.__evaluate_hand(line)
    else:
      for line in poker_hands.split('\n'):
        self.__evaluate_hand(line.strip())

  def process_data_from_file(self, filename):
    if not os.path.exists(os.path.join(self._location, filename)):
      raise FileNotFoundError("File specified does not exists.")

    with open(os.path.join(self._location, filename)) as poker_file:
      poker_hand = poker_file.readline()
      while poker_hand:
        self.__evaluate_hand(poker_hand)
        poker_hand = poker_file.readline()

  def __evaluate_hand(self, hand_data):
    '''
    Single hand evaluated
    '''
    hand = OneRound(hand_data)
    if hand.did_player1_win():
      self.player1_wins += 1

  def euler_solution(self):
    '''
    method to find the solution for the eulers problem
    '''
    self.process_data_from_file('p54-poker.txt')
    return self.player1_wins


def main():
  '''
  main function
  '''
  _poker = Poker()
  print('Solution for the Euler 054 problem:')
  # prints: 376
  print('Player1 wins {} times!'.format(_poker.euler_solution()))


if __name__ == "__main__":
  main()
