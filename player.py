from card import *
import random
class Player:
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.hand = []

        # set hand
        # takes in a set, the player hand becomes the 'cards'
    def set_hand(self, deck):
        deck_length = len(deck)
        for num in range(8):
            card_num = random.randint(0, deck_length)
            card_selected = deck.pop(card_num)
            self.hand[num] = card_selected

        # get identifier
        # get the identifier of the player

    def set_name(self, name):
        if type(name) == str:
            self.name = name

    def get_identifier(self):
        return self.identifier

        # get hand
        # returns the set of the players current hand
    def get_hand(self):
        return self.hand

        # add_card
        # adds a card to the players hand (given a card)
    def add_card(self, card):
        self.hand.append(card)

    def play_card(self, last_played, card):
        if last_played.get_color() == card.get_color() or card.get_type() == last_played.get_type() or last_played.get_type() == Type.WILD:
            return True
        else:
            return False

        # print_console
        # prints the user's hand to the console
    def print(self):
        print('It\'s now your turn!')
        print('Your hand:')
        # print(self.name + "'s hand")
        for i in self.hand:
            print(i + ': ' + self.hand[i].print())

        # print_graphics