class Poker_Competition:

    def __init__(self):
        player_list = []
        nr_games_played = 0

    def add_player(self, player):
        self.player_list.append(player)
        print("Added player", player.get_name())
