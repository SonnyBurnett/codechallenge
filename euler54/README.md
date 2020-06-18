This script consists out of a number of parts:

Helper functions:
* valueToNumeric(val):
    '''Converts the faces of cards to numeric values'''
* sortHand(hand):
    '''Processes each card in hand and sorts it based on value of the card. Adapted implementation of bubble sort algorithm'''
* isConsecutive(hand):
    """Validates the hand on the consecutiveness of the cards. Return True if cards are consecutive and if not return False."""
 


Data structure components:

* handLToDictS(hand):
    '''Converts a poker hand {list} into a sorted dictionary based on suits as keys.'''
* handLToDictC(hand):
    '''Converts a poker hand {list} into a sorted dictionary based on card values as keys.'''


Player hands

* royalFlush(hand):
    '''
    This function accepts a list of a hand. 
    The list is converted to a dictionary with suits as keys.
    Based on it, it checks if the winning hand is a Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    '''
* straight(hand):
    """Straight: All cards are consecutive values."""


* straightFlush(hand):
    """Straight Flush: All cards are consecutive values of same suit."""
 


* flush(hand):
    """Flush: All cards of the same suit."""


* fourOfaKind(hand):
    """Four of a Kind: Four cards of the same value."""

* threeOfaKind(hand):
    """Three of a Kind: Three cards of the same value."""


* pair(hand):
    """ 
    This functions selects all pairs in a hand.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    """

* highCard(hand):
    """High Card: Highest value card."""

* scoreCalc(scList):
    """Calculates the score of a given hand."""
 

Main functions:

* whathand(hlist):
    """This is a main function that identifies the hand of the player"""
* compareHands(hand1, hand2):
    """Compare the hands of the players and decide on the winner"""

 