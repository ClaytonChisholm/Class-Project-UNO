import random


# Class Player:
# Takes in Name and Identifier
class Player:
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.hand = []

    # Sets the players hand given the deck
    def set_hand(self, deck):
        deck_length = len(deck)
        for num in range(8):
            card_num = random.randint(0, deck_length)
            card_selected = deck.pop(card_num)
            self.hand[num] = card_selected
    
    # Set name
    # sets the player name
    def set_name(self, name):
        if type(name) == str:
            self.name = name

    # Returns name
    def get_name(self):
        return self.name

    # Returns the identifier
    def get_identifier(self):
        return self.identifier

    # Returns the players hand
    def get_hand(self):
        return self.hand

    # Adds card to hand
    def add_card(self, card):
        self.hand.append(card)
