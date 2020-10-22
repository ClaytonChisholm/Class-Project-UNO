from cpu import *
from player import *

class Game:
    player = Player(' ', 0)
    cpu1 = CPU("Mark", 1)
    cpu2 = CPU("Mira", 2)
    cpu3 = CPU("Julia", 3)
    players = [player, cpu1, cpu2, cpu3]
    deck = []
    played_deck = []
    last_played = Card(Type.WILD)
    current_player = 0
    player_count = 4
    reversed = False
    game_over = False
    # values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Draw 2', 'Reverse', 'Wild', 'Draw 4']
    # colors = ['red', 'yellow', 'blue', 'green', 'wild']

    def __init__(self, player_name):
        self.name = player_name
        self.fill_deck()
        self.shuffle_deck()
        last_played = self.draw_card()

    def validate_move(self, card: Card):
        if (card.get_color() == self.last_played.get_color() or card.get_type() == self.last_played.get_type()
                or card.get_type() == Type.WILD):
            return True
        else:
            return False

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def apply_power(self, card: Card):
        if card.get_type() == Type.SKIP:
            self.current_player = self.current_player + 2
        elif card.get_type() == Type.DRAW2:
            if not self.reversed:
                for i in range(2):
                    self.players[self.current_player + 1].add_card(self.draw_card())
            else:
                for i in range(2):
                    self.players[self.current_player - 1].add_card(self.draw_card())
        elif card.get_type() == Type.REVERSE:
            self.reverse()
        elif card.get_type() == Type.DRAW4:
            if not self.reversed:
                for i in range(4):
                    self.players[self.current_player + 1].add_card(self.draw_card())
            else:
                for i in range(4):
                    self.players[self.current_player - 1].add_card(self.draw_card())

    def fill_deck(self):
        color = Color.NONE
        for i in range(4):
            self.deck.append(Card(Type.WILD))
            self.deck.append(Card(Type.DRAW4))
            if i == 0:
                color = Color.YELLOW
            elif i == 1:
                color = Color.RED
            elif i == 2:
                color = Color.GREEN
            elif i == 3:
                color = Color.BLUE
            self.deck.append(Card(Type.ZERO, color))
            for k in range(2):
                self.deck.append(Card(Type.SKIP, color))
                self.deck.append(Card(Type.DRAW2, color))
                self.deck.append(Card(Type.REVERSE, color))
            for j in range(1,10):
                self.deck.append(Card(Type(j), color))
                self.deck.append(Card(Type(j), color))

    def draw_card(self):
        deck_length = len(self.deck)
        card_num = random.randint(0, deck_length)
        card_selected = self.deck.pop(card_num)
        return card_selected

    def reverse(self):

    def fill_hand(self, player):
        for i in range(0,7):
            card = self.draw_card()
            player.add_card(card)

    def change_turn(self):
        if self.reversed:
            self.current_player -=1
        else:
            self.current_player +=1

    def do_turns(self):
        self.player.set_name(input('How would you like to be called?'))
        for player in self.players:
            self.fill_hand(player)
        while not self.game_over:  # game engine of sorts

            for player in self.players:
                player.print() # prints the hand





            self.change_turn()
            if not self.players[self.current_player].get_hand():  # think this checks for an empty hand but im completely guessing
                self.game_over = False
                return self.players[self.current_player]  # returns winner










