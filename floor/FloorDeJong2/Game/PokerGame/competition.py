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
        winner = self.__player_list[0]
        for player in self.__player_list[1:]:
            if player.get_poker_hand() > winner.get_poker_hand():
                winner = player

        winner.add_win()
