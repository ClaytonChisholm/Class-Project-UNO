import random


class Game:
    player = Player("")
    cpu1 = CPU("Mark")
    cpu2 = CPU("Mira")
    cpu3 = CPU("Julia")
    players = [player, cpu1, cpu2, cpu3]
    deck = []
    played_deck = []
    last_played = Card()
    current_player = 1
    player_count = 4
    reversed = False
    values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Draw 2', 'Reverse', 'Wild', 'Draw 4']
    colors = ['red', 'yellow', 'blue', 'green', 'wild']

    def __init__(self, player_name):
        self.name = player_name
        self.fill_deck()
        self.shuffle_deck()
        last_played = self.draw_card()

    def validate_move(self, card):
        if (card.get_color() == self.last_played.get_color() or card.get_number() == self.last_played.get_number()
                or card.get_color == 'Wild'):
            return True
        else:
            return False

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def apply_power(self, card):
        if card.get_number() == 'Skip':
            self.current_player = self.current_player + 2
        elif card.get_number() == 'Draw 2':
            if not self.reversed:
                for i in range(2):
                    self.players[self.current_player + 1].draw_card()
            else:
                for i in range(2):
                    self.players[self.current_player - 1].draw_card()
        elif card.get_number() == 'Reverse':
            self.reverse()
        elif card.get_number() == 'Draw 4':
            if not self.reversed:
                for i in range(4):
                    self.players[self.current_player + 1].draw_card()
            else:
                for i in range(4):
                    self.players[self.current_player - 1].draw_card()

    def fill_deck(self):
        color = ""
        for i in range(4):
            self.deck.append(Card('Wild', 'Wild'))
            self.deck.append(Card('Wild', 'Draw 4'))
            if i == 0:
                color = 'Green'
            elif i == 1:
                color = 'Yellow'
            elif i == 2:
                color = 'Blue'
            elif i == 3:
                color = 'Red'
            self.deck.append(Card(color, '0'))
            for k in range(2):
                self.deck.append(Card(color, 'Skip'))
                self.deck.append(Card(color, 'Draw 2'))
                self.deck.append(Card(color, 'Reverse'))
            for j in range(1,10):
                self.deck.append(color, j)
                self.deck.append(color, j)

    def draw_card(self):

    def reverse(self):


