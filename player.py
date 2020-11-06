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

    # gets the name of the player
    def get_name(self):
        return self.name

    # returns the identifier of a player
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

    # prompts the player to choose a card and returns its index
    def choose_card(self):
        while True:
            try:
                card_num = int(input('Choose your card by entering the number associated with it: '))
                if not card_num < 1 and not card_num > len(self.hand):
                    break
                else:
                    print('That isn\'t a valid option...')
            except ValueError:
                print('Please try again, make sure to enter a number corresponding to your choice...')
        return card_num - 1

    # prints the player turn
    def print(self):
        print('It\'s now your turn, ' + self.name + '!')
        print('Your hand:')
        j = 1
        for i in self.hand:
            print(j, end=': ')
            i.print()
            if j < len(self.hand):
                print(end=', ')  # could be prettier
            j += 1
        print()
