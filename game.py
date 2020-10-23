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

    def turn(self):
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
              "cards from the discard deck. Once the player plays their last card, play is over!")
        
   



