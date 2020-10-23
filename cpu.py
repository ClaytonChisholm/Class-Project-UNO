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
            card_num = random.randint(0, deck_length)
            card_selected = deck.pop(card_num)
            self.CPU_hand[num] = card_selected

    def add_card(self, card):
        self.CPU_hand.append(card)

    def get_hand(self):
        return self.CPU_hand

    def play_card(self, Player, CPU1, CPU2, CPU3, last_played):
        special_cards = []
        power_card_found = False
        valid = False
        player_length = len(Player.get_hand())
        num_left = len(self.CPU_hand)
        CPU1_hand = len(CPU1.get_hand())
        CPU2_hand = len(CPU2.get_hand())
        CPU3_hand = len(CPU3.get_hand())

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

        while not valid:
            if power_card_found:
                power_card_length = len(special_cards)
                card_number = random.randint(0, power_card_length)
                chosen_card = special_cards[card_number]
                if last_played.get_color() == chosen_card.get_color() or chosen_card.get_type() == last_played.get_type() \
                        or last_played.get_type() == Type.WILD:
                    valid = True
                    self.CPU_hand.remove(chosen_card)
                    return chosen_card
            # add a bool to card object to confirm its been checked for validation?  else:

            else:
                card_num = random.randint(0, num_left)
                chosen_card = self.CPU_hand[card_num]
                if last_played.get_color() == chosen_card.get_color() or chosen_card.get_type() == last_played.get_type() \
                        or last_played.get_type() == Type.WILD:
                    valid = True
                    played_card = self.CPU_hand.pop(card_num)
                    return played_card
                # add a bool to card object to confirm its been checked for validation?  else:

    def get_name(self):
        return self.CPU_name

    def print(self):
        print(self.CPU_name + ' has ' + str(len(self.CPU_hand)) + ' cards')
