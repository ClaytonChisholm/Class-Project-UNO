from player import *
from card import *


# CPU Class, creates and plays each CPU player
class CPU:

    def __init__(self, cpu_name, cpu_number):
        self.CPU_name = cpu_name
        self.CPU_number = cpu_number
        self.CPU_hand = []

    # Creates the hand of CPU initially from deck of cards
    def set_hand(self, deck):
        deck_length = len(deck)
        for num in range(7):
            # randomly generates a card from deck to append to CPU_hand
            card_num = random.randint(0, deck_length)
            card_selected = deck.pop(card_num)
            self.CPU_hand[num] = card_selected

    # Adds card to CPU_hand
    def add_card(self, card):
        self.CPU_hand.append(card)

    # returns the CPU hand
    def get_hand(self):
        return self.CPU_hand

    # returns the identification number of the CPU
    def get_number(self):
        return self.CPU_number

    # Selects which card CPU will play
    def play_card(self, player: Player, cpu1, cpu2, last_played):
        special_cards = []
        valid_cards = []
        power_card_found = False
        player_length = len(player.get_hand())
        cpu1_hand = len(cpu1.get_hand())
        cpu2_hand = len(cpu2.get_hand())

        # if the other players have less than three cards left, play special powered cards
        if player_length <= 3 or cpu1_hand <= 3 or cpu2_hand <= 3:
            for card in self.CPU_hand:
                if card.get_type() == Type.DRAW4:
                    power_card_found = True
                    special_cards.append(card)  # appends power cards to special_cards list
                elif card.get_type() == Type.REVERSE:
                    power_card_found = True
                    special_cards.append(card)
                elif card.get_type() == Type.DRAW2:
                    power_card_found = True
                    special_cards.append(card)
                elif card.get_type() == Type.SKIP:
                    power_card_found = True
                    special_cards.append(card)

        # If the CPU is playing power cards, check what cards are valid to be played and add to
        # valid_cards list
        if power_card_found:
            for chosen_card in special_cards:
                if last_played.get_color() == chosen_card.get_color() \
                        or chosen_card.get_type() == last_played.get_type():
                    valid_cards.append(chosen_card)

        # Otherwise, check entire hand for valid cards and add to valid_cards list
        else:
            for chosen_card in self.CPU_hand:
                if last_played.get_color() == chosen_card.get_color() \
                        or chosen_card.get_type() == last_played.get_type():
                    valid_cards.append(chosen_card)

        # If the CPU has a valid card to play, randomly select a card and return it
        if len(valid_cards) != 0:
            card_num = random.randint(0, len(valid_cards) - 1)
            chosen_card = valid_cards[card_num]
            card_hand_num = self.CPU_hand.index(chosen_card)
            played_card = self.CPU_hand.pop(card_hand_num)
            return played_card

        # otherwise CPU must draw a card and return false
        else:
            return False

    # Randomly generates a wild card color based on color of cards in CPU hand
    # returns color chosen
    def cpu_wilds(self):
        color_choice = []
        count_r = 0
        count_b = 0
        count_y = 0
        count_g = 0

        for card in self.CPU_hand:
            # if the card in CPU hand is red, add to count and append to
            # color choice list
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

        # if the list has colors in it, randomly select a color and return choice
        if len(color_choice) > 0:
            color_chosen = random.randint(0, len(color_choice) - 1)
            return color_choice[color_chosen]
        else:
            return Color.RED  # just a placeholder that doesn't matter since the CPU will win if this condition is met

    # returns CPU name
    def get_name(self):
        return self.CPU_name
