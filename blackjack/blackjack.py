import random
class Card:

    def __init__(self, value, suit) -> None:
        self.value = value
        self.suit = suit

    @classmethod
    def create_deck(self):
        deck = []
        suits = {'hearts', 'spades', 'clovers', 'diamonds'}
        for suit in suits:
            for num in range(1, 13):
                deck.append(
                    Card(num, suit)
                )
        return deck

    @classmethod
    def shuffle_desk(self, deck):
        return random.shuffle(deck)

class Blackjack:
    
    def __init__(self) -> None:
        self.deck = Card.create_deck()
        self.player_hand = []
        self.cpu_hand = []

    def __shuffle(self):
        self.deck = Card.shuffle_desk(self.deck)

    def draw(self, player) -> None:
        player = self.player_hand if player == 'player' else self.cpu_hand
        player.append(self.deck.pop())
    