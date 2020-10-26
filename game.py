from cpu import *
from player import *


def choose_color():  # change when graphics
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

    def __init__(self, player_name):
        self.name = player_name
        self.player.set_name(player_name)
        self.fill_deck()
        self.shuffle_deck()
        self.last_played = self.draw_first_card()

    def validate_move(self, card: Card):
        if (card.get_color() == self.last_played.get_color() or card.get_type() == self.last_played.get_type()
                or card.get_type() == Type.WILD or card.get_type() == Type.DRAW4):
            return True
        else:
            return False

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def shuffle_discard(self):
        random.shuffle(self.played_deck)
        self.deck = self.played_deck

    def apply_power(self):
        card = self.last_played
        if card.get_type() == Type.SKIP:
            if not self.reversed:
                if self.current_player != self.players[4]:
                    self.current_player = self.current_player + 1
                else:
                    self.current_player = self.players[0]
            else:
                if self.current_player != self.players[0]:
                    self.current_player = self.current_player - 1
                else:
                    self.current_player = self.players[4]
        elif card.get_type() == Type.DRAW2:
            if not self.reversed:
                if self.current_player != self.players[4]:
                    for i in range(2):
                        self.players[self.current_player + 1].add_card(self.draw_card())
                else:
                    for i in range(2):
                        self.players[0].add_card(self.draw_card())
            else:
                if self.current_player != self.players[0]:
                    for i in range(2):
                        self.players[self.current_player - 1].add_card(self.draw_card())
                else:
                    for i in range(2):
                        self.players[4].add_card(self.draw_card())
        elif card.get_type() == Type.REVERSE:
            self.reverse()
        elif card.get_type() == Type.DRAW4:
            if not self.reversed:
                if self.current_player != self.players[4]:
                    for i in range(4):
                        self.players[self.current_player + 1].add_card(self.draw_card())
                else:
                    for i in range(4):
                        self.players[0].add_card(self.draw_card())
            else:
                if self.current_player != self.players[0]:
                    for i in range(4):
                        self.players[self.current_player - 1].add_card(self.draw_card())
                else:
                    for i in range(4):
                        self.players[4].add_card(self.draw_card())

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
            self.shuffle_discard()
            deck_length = len(self.deck)
        card_num = random.randint(0, deck_length-1)
        card_selected = self.deck.pop(card_num)
        return card_selected

    def draw_first_card(self):
        while True:
            card = self.draw_card()
            card_type = card.get_type()
            if card_type == Type.DRAW4 or card_type == Type.WILD or card_type == Type.SKIP or card_type == Type.DRAW2 or card_type == Type.REVERSE:
                self.played_deck.append(card)
                continue
            else:
                self.played_deck.append(card)
                break
        return card

    def reverse(self):
        if not self.reversed:
            self.reversed = True
        else:
            self.reversed = False

    def set_wild(self):
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
    
    def display_rules(self):
        print("Welcome to the game of UNO! In this version, the goal of the \n"
              "game is to play all of the cards in your hand, and the first player\n"
              "to do this wins. Each player is dealt 7 cards at the start of\n"
              "the game after the deck has been shuffled. There is a draw deck where\n"
              "the players draw cards and a discard deck where the players play their cards.\n"
              "There are special and normal cards in the deck. The normal cards have a number\n"
              "ranging from 0 to 9 and a color (red, green, blue, or yellow) and the\n"
              "special cards have powers. These powers include:")

        print("Draw 2: where the next person to play must draw two cards from the draw pile and lose their turn\n"
              "Reverse: where the card reverses the direction of play (who goes next)\n"
              "Skip card: which skips the next person in line to play\n"
              "Wild card: where the player who played this card can change the color of the card being played\n"
              "Draw 4 Wild card: where the player can call the next color being played and requires the next\n"
              "player to pick four cards from the draw pile and lose their turn")

        print("In order to begin play, the player must match the top card of the discard deck either by number,\n"
              "color, or word and place their card to be played on top of the discard deck. The player can play\n"
              "a wild card or wild plus four card whenever it is their turn. If the player playing does not have\n"
              "a valid card to play, they must pick a card from the draw pile. If you draw a card you can play,\n"
              "play it. Otherwise, continue picking until you have found a card to play. If the draw deck runs\n"
              "out of cards, the discard deck will be reshuffled and become the draw deck. Once the player plays\n"
              "their card, play moves to the next person. Before playing your last card, you must click the button\n"
              "which says “UNO”. If the next player to go plays their card before you say UNO, you must draw four\n"
              "cards from the discard deck. Once a player plays their last card, play is over!")
        
   

        # TODO this
        card = self.draw_card()  # this is very temporary
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
                print('It\'s ' + player.get_name() + '\'s turn')  # this is the only text based thing in here that i
                # couldnt find a better place for
            self.last_played = self.pick_card()
            self.played_deck.append(self.last_played)
            self.apply_power()  # we will handle wilds later TODO should draw4 and wild color choosing be handled here?

            if type(player) == Player and (
                    self.last_played.get_type() == Type.WILD or self.last_played.get_type == Type.DRAW4):
                self.set_wild()
            elif self.last_played.get_type() == Type.WILD or self.last_played.get_type == Type.DRAW4:
                # Not sure if entirely works, I think I can call the player variable (which in this elif statement is actually a CPU?)
                color = player.CPU_wilds() # calls cpu wild function
                self.last_played.set_wild(color)

            if not player.get_hand():  # think this checks for an empty hand but im completely guessing
                self.game_over = False
                return self.players[self.current_player]  # returns winner
            self.change_turn()  # changes turn after loop processes


if __name__ == '__main__':
    game = Game(input('What\'s your name?'))
    print(game.do_turns(), ' wins!')
