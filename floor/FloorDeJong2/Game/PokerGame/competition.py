import sys


class PokerCompetition:

    def __init__(self, name):
        self.__name = name
        self.__player_list = []
        self.__nr_games_played = 0

    def add_player(self, player):
        self.__player_list.append(player)
        # print("Added player", player.get_name())

    def return_player_list(self):
        print(self.__player_list[0].get_name)
        return self.__player_list

    def deal_cards(self, all_cards):
        if len(all_cards) < len(self.__player_list)*5:
            print("Error: Not enough cards for ", len(self.__player_list), "players")
            exit(1)

        for i in range(len(self.__player_list)):
            self.__player_list[i].set_hand(all_cards[i * 5: (i * 5) + 5])

    def determine_winner(self):

        self.__nr_games_played += 1

        winner = self.__player_list[0]
        for i in range(1, len(self.__player_list)):
            first_player_hand = winner.get_poker_hand().get_hand()
            second_player_hand = self.__player_list[i].get_poker_hand().get_hand()

            if first_player_hand < second_player_hand:
                winner = self.__player_list[i]
            if first_player_hand == second_player_hand:
                winner = self.determine_winner_same_hand(winner, self.__player_list[i], first_player_hand)

        winner.add_win()
        return winner

    def determine_winner_same_hand(self, player_one, player_two, hand):
        if hand == 10:
            print("Error: Two players have a Royal flush, card deck incorrect")
            exit(1)

        elif hand in [1, 5, 6, 9]:
            winner = self.determine_winner_via_highest_card(player_one, player_two, 1)
        elif hand in [2, 3, 4, 7, 8]:
            winner = self.determine_winner_via_card_value(player_one, player_two, 0)
        else:
            print("Hand-type out of bounds")
            exit(1)

        return winner

    def determine_winner_via_highest_card(self, player_one, player_two, attempts):
        if attempts > 5:
            sys.exit("Tied - Both have all the same values in cards")

        highest_card_one = player_one.get_poker_hand().get_highest_card(attempts)
        highest_card_two = player_two.get_poker_hand().get_highest_card(attempts)
        if highest_card_one > highest_card_two:
            return player_one
        elif highest_card_one < highest_card_two:
            return player_two
        else:
            attempts += 1
            return self.determine_winner_via_highest_card(player_one, player_two, attempts)

    def determine_winner_via_card_value(self, player_one, player_two, element_to_compare):
        value_one = player_one.get_poker_hand().get_hand_value()
        value_two = player_two.get_poker_hand().get_hand_value()

        if len(value_one) <= element_to_compare:
            return self.determine_winner_via_highest_card(player_one, player_two, 1)

        if value_one[element_to_compare] > value_two[element_to_compare]:
            return player_one
        elif value_one[element_to_compare] < value_two[element_to_compare]:
            return player_two
        else:
            return self.determine_winner_via_card_value(player_one, player_two, element_to_compare+1)


