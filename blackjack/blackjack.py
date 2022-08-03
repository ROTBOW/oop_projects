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
            for num in range(1, 14):
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
        self.turn = True
        self.winner = ''

    def __shuffle(self):
        self.deck = Card.shuffle_desk(self.deck)

    def draw(self, player) -> None:
        player = self.player_hand if player == 'player' else self.cpu_hand
        player.append(self.deck.pop())
    
    def show_hand(self):
        cards = {
            1: 'Ace',
            11: 'Jack',
            12: 'Queen',
            13: 'King'
        }
        print(', '.join(
            [str(cards.get(x.value, x.value)) for x in self.player_hand]
            ))
        

    def play(self):
        print('BlackJack Begin.')
        self.deck = Card.create_deck()
        self.__shuffle()
        while self.turn:
            self.show_hand()
            self.action() # needs to be made
        self.cpu_move() # needs to be made
        self.check_winner() # needs to be made
        print(f'Game Over.\nWinner is {self.winner}')

# game = Blackjack()
# game.draw('player')
# game.draw('player')
# game.draw('player')
# game.draw('player')
# game.show_hand()