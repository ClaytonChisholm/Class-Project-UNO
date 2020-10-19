class Player:
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.hand = []

        # set hand
        # takes in a set, the player hand becomes the 'cards'
    def set_hand(self, cards):
        self.hand = cards

        # get identifier
        # get the identifier of the player
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

        # add_card
        # adds a card to the players hand (references deck)
    def add_card(self, deck):
        card_added = deck.pop(0)
        self.hand.append(card_added)

        # print_console
        # prints the user's hand to the console
    def print(self):
        print('Your hand:')
        # print(self.name + "'s hand")
        for i in self.hand:
            print(i + ': ' + self.hand[i])

        # print_graphics