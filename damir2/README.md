# Challenge #2

## Euler 02

A version of Fibonacci sequence.
This one uses a Python generator to generate the numbers in sequence.

## Euler 54

Evaluating a poker hands.
The main challenge was to evaluate a players hand a give it some value. Solution was to give a hand a dictionary of values that represent all possible values in poker:

```text
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
```

Represented as a dictionary in the PlayerHand class;

```json
{
  '0': 14,      # the highest value card J,Q,K,A = 11,12,13,14 with 14 the highest value card - Ace
  '1': [3],     # a pair of card with the value 3 OR
  '1': [6, 12], # two pairs and theirs values (two sixes and two queens)
  '2': 12,      # two pairs and the highest value of the pairs (two queens highest pair)
  '3': 10,      # three of a kind and the value of it (3 tens)
  '4': 9,       # straight with 9 as the highest card
  '5': 13,      # flush with king as the highest card
  '6': 10,      # full house with 3 tens as the highest value
  '7': 14,      # four of a kind in aces
  '8': 11,      # straight flush with J as an ending card
  '9': 14       # royal flush with A as an ending card
}
```

If there is no match for the value it is not going to be added to the dictionary.
Each players hand gets its own values dictionary which gets compered with the other one in the Hand class and did_player_win method.

Note: this is not checking all tie possibilities if the highest cards are the same for both players
