import random
from card import *


class CPU:

    def __init__(self, CPU_name, CPU_number):
        self.CPU_name = CPU_name
        self.CPU_number = CPU_number
        self.CPU_hand = []

    def set_hand(self, deck):
        deck_length = len(deck)
        for num in range(7):
            card_num = random.randint(0,deck_length)
            card_selected = deck.pop(card_num)
            self.CPU_hand[num] = card_selected

    def add_card(self, card):
        self.CPU_hand.append(card)

    def get_hand(self):
        return self.CPU_hand

    def play_card(self, Player, CPU1, CPU2, CPU3, last_played):
        special_cards = []
        power_card_found = False
        player_hand = Player.get_hand()
        player_length = len(player_hand)
        CPU1_hand = CPU1.get_hand()
        CPU2_hand = CPU2.get_hand()
        CPU3_hand = CPU3.get_hand()

        if player_length <= 3 or CPU1_hand <= 3 or CPU2_hand <= 3 or CPU3_hand <= 3:

            for card in self.CPU_hand:
                if card.get_type() == Type.DRAW4:
                    power_card_found = True
                    special_cards.append(card)
                elif card.get_type() == Type.REVERSE:
                    power_card_found = True
                    special_cards.append(card)
                elif card.get_type() == Type.DRAW2:
                    power_card_found = True
                    special_cards.append(card)
                elif card.get_type() == Type.SKIP:
                    power_card_found = True
                    special_cards.append(card)

            if power_card_found:
                power_card_length = len(special_cards)
                card_chosen = random.randint(0, power_card_length)
                card_selected = special_cards[card_chosen]
                return card_selected
            else:

                num_left = len(self.CPU_hand)
                card_num = random.randint(0, num_left)
                played_card = self.CPU_hand.pop(card_num)
                return played_card
        else:
            num_left = len(self.CPU_hand)
            card_num = random.randint(0, num_left)
            played_card = self.CPU_hand.pop(card_num)
            return played_card

