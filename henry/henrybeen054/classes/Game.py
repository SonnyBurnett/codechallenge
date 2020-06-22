from classes.Hand import Hand


class Game:
    def __init__(self, game_descriptor):
        cards = game_descriptor.split()
        card_count = len(cards)
        hand_count = int(card_count / 5)

        self.hands = [Hand(playerId, cards[5*playerId:5+(5*playerId)]) for playerId in range(0, hand_count)]

    def get_winning_player_id(self):
        winner = max(self.hands, key=lambda h: h.get_score())
        return winner.player_id
