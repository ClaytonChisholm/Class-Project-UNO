import random

class CPU:
    CPU_hand = []

    def __init__(self, CPU_name, CPU_number):
        self.CPU_name = CPU_name
        self.CPU_number = CPU_number

    def set_hand(self, deck):
        global CPU_hand
        deck_length = len(deck)
        for num in range(8):
            card_num = random.randint(0,deck_length)
            card_selected = deck.pop(card_num)
            CPU_hand[num] = card_selected

    def add_card(self, deck):
        global CPU_hand
        card_added = deck.pop(0)
        CPU_hand.append(card_added)

    def get_hand(self):
        return CPU_hand

    def play_card(self, Player, CPU1, CPU2, CPU3):
        special_cards = []
        player_hand = Player.get_hand()
        player_length = len(player_hand)
        CPU1_hand = CPU1.get_hand()
        CPU2_hand = CPU2.get_hand()
        CPU3_hand = CPU3.get_hand()
        if player_length <= 3 or CPU1_hand <= 3 or CPU2_hand <= 3 or CPU3_hand <= 3:
            for card in CPU_hand:
                if card.get_number() == "Draw 4":
                    special_cards.append(card)
                elif card.get_number() == 'Reverse':
                    special_cards.append(card)
                elif card.get_number() == 'Draw 2':
                    special_cards.append(card)
                elif card.get_number() == 'Skip':
                    special_cards.append(card)

            power_card_length = len(special_cards)
            card_chosen = random.randint(0, power_card_length)
            card_selected = special_cards[card_chosen]
            return card_selected

        else:
            #finishing this part tomorrow
























