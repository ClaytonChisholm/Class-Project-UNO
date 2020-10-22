from cpu import *
from player import *


def choose_color():  # TODO change when graphics
    print('Red: 1')
    print('Green: 2')
    print('Blue: 3')
    print('Yellow: 4')
    while True:
        try:
            color = int(input('Enter the number corresponding to your preferred color: '))
            if not color < 1 and not color > 4:
                break
            else:
                print('That isn\'t a valid option...')
        except ValueError:
            print('Please try again, make sure to enter an integer corresponding to your choice...')
    return Color(color)


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
        self.player.set_name(player_name)
        self.fill_deck()
        self.shuffle_deck()
        self.last_played = self.draw_card()

    def validate_move(self, card: Card):
        if (card.get_color() == self.last_played.get_color() or card.get_type() == self.last_played.get_type()
                or card.get_type() == Type.WILD or card.get_type() == Type.DRAW4):
            return True
        else:
            return False

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def apply_power(self):
        card = self.last_played
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
            for j in range(1, 10):
                self.deck.append(Card(Type(j), color))
                self.deck.append(Card(Type(j), color))

    def draw_card(self):
        deck_length = len(self.deck)
        if deck_length == 0:
            self.fill_deck()
            self.shuffle_deck()
        card_num = random.randint(0, deck_length-1)
        card_selected = self.deck.pop(card_num)
        return card_selected

    def reverse(self):
        pass  # don't merge this i just put it here to test w/o error

    def set_wild(self):  # TODO, should this prompt user for color here or in game engine?
        color = choose_color()
        self.last_played.set_wild(color)

    def fill_hand(self, player):
        for i in range(0, 7):
            card = self.draw_card()
            player.add_card(card)

    def change_turn(self):
        if self.reversed:
            self.current_player -= 1
        else:
            self.current_player += 1
        if self.current_player > self.player_count-1:
            self.current_player = 0
        elif self.current_player < 0:
            self.current_player = self.player_count-1

    def pick_card(self):  # this function needs to be changed for graphics
        player = self.players[self.current_player]

        # TODO this
        card = self.last_played  # this is very temporary
        return card

    def print_top_card(self):  # change for graphic
        print('Current card is a', end=' ')
        self.last_played.print()
        print()

    def do_turns(self):
        for player in self.players:
            self.fill_hand(player)
        while not self.game_over:  # game engine of sorts
            player = self.players[self.current_player]
            self.print_top_card()
            if type(player) == Player:
                for p in self.players:
                    p.print()  # prints the hand
            else:
                print(
                    'It\'s ' + player.get_name() + '\'s turn')  # this is the only text based thing in here that i
                # couldnt find an independent place for
            self.last_played = self.pick_card()
            self.apply_power()  # we will handle wilds later TODO should draw4 and wild color choosing be handled here?

            if type(player) == Player and (
                    self.last_played.get_type() == Type.WILD or self.last_played.get_type == Type.DRAW4):
                # TODO cpu wilds
                self.set_wild()
            elif self.last_played.get_type() == Type.WILD or self.last_played.get_type == Type.DRAW4:
                # calls cpu wild function
                self.last_played.set_wild(Color.RED)  # temporary

            if not player.get_hand():  # think this checks for an empty hand but im completely guessing
                self.game_over = False
                return self.players[self.current_player]  # returns winner
            self.change_turn()  # changes turn after loop processes


if __name__ == '__main__':
    game = Game('Tester')
    print(game.do_turns())
