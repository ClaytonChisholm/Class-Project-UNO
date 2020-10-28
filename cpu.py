from player import *
from card import *


class CPU:

    def __init__(self, cpu_name, cpu_number):
        self.CPU_name = cpu_name
        self.CPU_number = cpu_number
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

    def get_number(self):
        return self.CPU_number

    def play_card(self, player: Player, cpu1, cpu2, last_played):
        special_cards = []
        valid_cards = []
        power_card_found = False
        player_length = len(player.get_hand())
        cpu1_hand = len(cpu1.get_hand())
        cpu2_hand = len(cpu2.get_hand())

        if player_length <= 3 or cpu1_hand <= 3 or cpu2_hand <= 3:

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
            for chosen_card in special_cards:
                # power_card_length = len(special_cards)
                # card_number = random.randint(0, power_card_length)
                # chosen_card = special_cards[card_number]
                if last_played.get_color() == chosen_card.get_color()\
                        or chosen_card.get_type() == last_played.get_type():
                    valid_cards.append(chosen_card)

        else:
            for chosen_card in self.CPU_hand:
                if last_played.get_color() == chosen_card.get_color()\
                        or chosen_card.get_type() == last_played.get_type():
                    valid_cards.append(chosen_card)

        if len(valid_cards) != 0:
            card_num = random.randint(0, len(valid_cards) - 1)
            chosen_card = valid_cards[card_num]
            card_hand_num = self.CPU_hand.index(chosen_card)
            played_card = self.CPU_hand.pop(card_hand_num)
            return played_card
        else:
            return False

    def cpu_wilds(self):
        color_choice = []
        count_r = 0
        count_b = 0
        count_y = 0
        count_g = 0

        for card in self.CPU_hand:
            if card.get_color() == Color.RED and count_r != 1:
                color_choice.append(Color.RED)
                count_r += 1
            elif card.get_color() == Color.BLUE and count_b != 1:
                color_choice.append(Color.BLUE)
                count_b += 1
            elif card.get_color() == Color.YELLOW and count_y != 1:
                color_choice.append(Color.YELLOW)
                count_y += 1
            elif card.get_color() == Color.GREEN and count_g != 1:
                color_choice.append(Color.GREEN)
                count_g += 1
        if len(color_choice) > 0:
            color_chosen = random.randint(0, len(color_choice) - 1)
            return color_choice[color_chosen]
        else:
            return Color.RED  # just a placeholder that doesn't matter since the CPU will win if this condition is met

    def get_name(self):
        return self.CPU_name

    def print(self):
        if not len(self.CPU_hand) == 1:
            print(self.CPU_name + ' has ' + str(len(self.CPU_hand)) + ' cards')
        else:
            print(self.CPU_name + ' has 1 card')
