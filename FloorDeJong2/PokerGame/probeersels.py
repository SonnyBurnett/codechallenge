from unittest import mock

import PokerGame.simple
import PokerGame.pokerhand as ph
import PokerGame.pokerhand
from PokerGame.player import Player


def use_simple_function():
    result = PokerGame.simple.simple_function()
    print(result)


@mock.patch("PokerGame.simple.simple_function")
def mock_simpler_function(mock_simpler_function):
    mock_simpler_function.return_value = "Bla bla"
    result = PokerGame.simple.simple_function()
    print(result)

@mock.patch('PokerGame.pokerhand.is_flush')
def test_is_flush(mock_is_flush):
    mock_is_flush.return_value = True
    result = PokerGame.pokerhand.is_flush()
    print(result)

@mock.patch("PokerGame.player.Player.get_poker_hand")
def test_get_poker_hand(mock_get_poker_hand):
    mock_get_poker_hand.return_value = 5
    result = PokerGame.player.Player.get_poker_hand()
    print(result)


@mock.patch("PokerGame.player.Player.get_poker_hand")
def test_get_poker_hand2(mock_get_poker_hand):
    mock_get_poker_hand.side_effect = [5, 6]
    result = PokerGame.player.Player.get_poker_hand()
    result2 = PokerGame.player.Player.get_poker_hand()
    print(result, result2)


@mock.patch("PokerGame.simple.SimpleClass")
def mock_simple_class(mock_class):
    mock_class.return_value.explode.return_value = "BOO!"
    inst = PokerGame.simple.SimpleClass()
    result = inst.explode()
    print(result)


@mock.patch("PokerGame.player.Player")
@mock.patch("PokerGame.pokerhand.PokerHand")
def mock_player_class(mock_player, mock_hand):
    mock_player.return_value.get_poker_hand.side_effect = [5, 6]
    mock_hand.return_value.get_highest_card.return_value = [2, 14]

    player_one = PokerGame.player.Player()
    player_two = PokerGame.player.Player()
    hand_one = PokerGame.pokerhand.PokerHand()

    result = player_one.get_poker_hand()
    result2 = player_two.get_poker_hand()
    result3 = hand_one.get_highest_card()
    print(result, result2, result3)

if __name__ == '__main__':
    use_simple_function()
    mock_simpler_function()
    test_is_flush()
    test_get_poker_hand()
    test_get_poker_hand2()
    test_get_poker_hand2()
    mock_simple_class()
    mock_player_class()
