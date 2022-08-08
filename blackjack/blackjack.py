import random
class Card:

    def __init__(self, value, suit) -> None:
        self.value = value
        self.suit = suit

    @classmethod
    def create_deck(self) -> list:
        deck = []
        suits = {'hearts', 'spades', 'clovers', 'diamonds'}
        for suit in suits:
            for num in range(1, 14):
                deck.append(
                    Card(num, suit)
                )
        return deck

    @classmethod
    def shuffle_deck(self, deck) -> list:
        random.shuffle(deck)

    def __str__(self) -> str:
        cards = {
            1: 'Ace',
            11: 'Jack',
            12: 'Queen',
            13: 'King'
            }
        return f'{cards.get(self.value, self.value)} of {self.suit}'

class Blackjack:
    
    def __init__(self) -> None:
        self.deck = Card.create_deck()
        self.player_hand = []
        self.cpu_hand = []
        self.turn = True
        self.winner = ''

    def shuffle(self) -> None:
        Card.shuffle_deck(self.deck)

    def draw(self, player) -> None:
        player = self.player_hand if player == 'player' else self.cpu_hand
        player.append(self.deck.pop())
    
    def show_hand(self) -> None:
        print(', '.join(
            [str(x) for x in self.player_hand]
            ))
        print(self.get_count(self.player_hand))

    def get_count(self, hand) -> int:
        aces, count = 0, 0
        for card in hand:
            card = card.value

            if card == 1:
                aces += 1
            elif card >= 10:
                count += 10
            else:
                count += card

        for _ in range(aces):
            if 11 + count <= 21:
                count += 11
            else:
                count += 1
                
        return count

        
    def action(self) -> None:
        print('Hit or Stay?')
        answer = input('-> ')
        if answer in ['hit', 'h', 'Hit']:
            self.draw('player')
            if self.get_count(self.player_hand) > 21:
                self.turn = not self.turn
        else:
            self.turn = not self.turn

    def cpu_move(self) -> None:
        while True:
            if self.get_count(self.cpu_hand) > 17: break
            self.draw('cpu')

    def check_winner(self) -> None:
        player, cpu = self.get_count(self.player_hand), self.get_count(self.cpu_hand)
        # if player > 21 or cpu > 21:
        #     pass
        if player <= 21 and cpu > 21:
            self.winner = 'player'
        elif player > 21 and cpu <= 21:
            self.winner = 'CPU'
        else:
            self.winner = 'player' if player > cpu else 'CPU'


    def play(self) -> None:
        print('BlackJack Begin.')
        self.deck = Card.create_deck()
        self.shuffle()
        while self.turn:
            self.show_hand()
            self.action()
        self.cpu_move()
        self.show_hand()
        self.check_winner()
        print(f'Game Over.\nWinner is {self.winner}\n{self.get_count(self.player_hand)} vs {self.get_count(self.cpu_hand)}')

game = Blackjack()
game.play()
# game.shuffle()
# game.draw('player')
# game.draw('player')
# game.draw('cpu')
# game.draw('cpu')
# game.show_hand()
# game.check_winner()
# game.draw('player')
# game.draw('player')
# game.draw('player')
# game.draw('player')
# game.show_hand()
# print(game.get_count(game.player_hand))