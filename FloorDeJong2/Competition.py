class Poker_Competition:

    def __init__(self):
        self.player_list = []
        self.nr_games_played = 0

    def add_player(self, player):
        self.player_list.append(player)
        print("Added player", player.get_name())

    def deal_cards(self, all_cards):
        print(all_cards)
        if len(all_cards) < len(self.player_list)*5:
            print("Error: Not enough cards for ", len(self.player_list), "players")
            exit(1)

        for i in range(len(self.player_list)):
            self.player_list[i].set_hand(all_cards[i*5: (i*5)+5])

    def determine_winner(self):
        winner = self.player_list[0]
        for i in range(1, len(self.player_list)):
            first_player_hand = winner.get_hand().get_hand()
            second_player_hand = self.player_list[i].get_hand().get_hand()

            if first_player_hand < second_player_hand:
                winner = self.player_list[i]
            if first_player_hand == second_player_hand:
                winner = self.determine_winner_same_hand(winner, self.player_list[i], first_player_hand)

        winner.add_win()
        return winner

    def determine_winner_same_hand(self, player_one, player_two, hand):
        if hand == 10:
            print("Error: Two players have a Royal flush, card deck incorrect")
            exit(1)
        if hand == 9:
            return self.determine_winner_via_highest_card(player_one, player_two, 1)
        if hand == 2:
            return self.determine_winner_via_highest_card(player_one, player_two, 1)
        return player_two

    def determine_winner_via_highest_card(self, player_one, player_two, attemps):
        if player_one.get_hand().get_count_call_highest_card() == 5:
            print("Both have all the same values in cards")
            exit(1)

        print(player_one.get_name(), " highest card ", player_one.get_hand().get_highest_card(attemps))
        print(player_two.get_name(), " highest card ", player_two.get_hand().get_highest_card(attemps))
        if player_one.get_hand().get_highest_card(attemps) < player_two.get_hand().get_highest_card(attemps):
            return player_one
        elif player_one.get_hand().get_highest_card(attemps) > player_two.get_hand().get_highest_card(attemps):
            return player_two
        else:
            print("same card:", player_one.get_hand().get_highest_card(attemps))
            attemps += 1
            return self.determine_winner_via_highest_card(player_one, player_two, attemps)





