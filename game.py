from copy import copy
from cpu import *
from card import *


def display_rules():
    rules_text = "Welcome to the game of UNO! In this version, the goal of the game " \
                 "is to play all of the cards in your\n hand, and the first" \
                 " player to do this wins. Each player is dealt 7 cards at the start of" \
                 " the game after the\n deck has been shuffled. There is a draw deck where" \
                 " the players draw cards and a discard deck where the players play their\n cards." \
                 " There are special and normal cards in the deck. The normal\n cards have a number" \
                 "  from 0 to 9 and a color (red, green, blue, or yellow) and the " \
                 "special cards have powers. These powers include:\n " \
                 "Draw 2: where the" \
                 " next person to play must draw two cards from the draw pile and lose their turn\n" \
                 "Reverse: where the card reverses the direction of play (who goes next)\n" \
                 "Skip card: which skips the next person in line to play\n" \
                 "Wild card: where the player who played this card can change the color of the card being played\n" \
                 "Draw 4 card: where the player can call the next color being played and requires the next\n" \
                 " player to pick four cards from the draw pile and lose their turn\n In order to begin play," \
                 " the player must match the top card of the discard deck either by number," \
                 " color, or word and place their card to be played on top of the discard deck.\nThe player can play"\
                 "a wild card or wild plus four card whenever it is their turn.\nIf the player playing does not have"\
                 " a valid card to play, they must pick a card from the draw pile.\nIf you draw a card you can play,"\
                 " play it.\nOtherwise, the next player starts their turn.\nIf the draw deck runs " \
                 "out of cards, the discard deck will be reshuffled and become the draw deck.\nOnce the player plays"\
                 " their card, play moves to the next person."

    return rules_text


class Game:
    deck = []
    played_deck = []
    last_played = Card(Type.WILD)
    current_player = 0
    player_count = 4
    reversed = False
    game_over = False

    def __init__(self, cpu1, cpu2, cpu3, player):
        self.player = player
        self.cpu1 = cpu1
        self.cpu2 = cpu2
        self.cpu3 = cpu3
        self.players = [self.player, self.cpu1, self.cpu2, self.cpu3]
        self.fill_deck()
        self.shuffle_deck()
        self.last_played = self.draw_first_card()  # special draw function that makes sure first card doesn't
        # have a special power

    def get_top_card(self):
        return self.last_played

    def validate_move(self, card: Card):
        # if the selected card has the same color, number (type) or is a wild it can be played
        if (card.get_color() == self.last_played.get_color() or card.get_type() == self.last_played.get_type()
                or card.get_type() == Type.WILD or card.get_type() == Type.DRAW4):
            return True
        else:
            return False

    # shuffle the entire deck
    def shuffle_deck(self):
        random.shuffle(self.deck)

    def shuffle_discard(self):
        random.shuffle(self.played_deck)
        self.deck = copy(self.played_deck)
        # reset the played deck to empty
        self.played_deck = []

    def skip(self):
        # Order of skip is different depending on the reverse status
        if not self.reversed:
            # if the current player is not the last player in the turn order it is safe to
            # skip the next player
            if self.current_player != self.player_count - 1:
                self.current_player = self.current_player + 1
                # output who lost their turn so the player can see
            else:
                # assign the current player to the beginning of the turn order if it is currently player 4s turn
                self.current_player = 0
                # output who lost their turn so the player can see

        # if it is currently reversed, do the opposite of above
        else:
            if self.current_player != 0:
                self.current_player = self.current_player - 1
                # output who lost their turn so the player can see
            else:
                self.current_player = self.player_count - 1
                # output who lost their turn so the player can see

    def apply_power(self):
        # assign card to the last played card then check for a power
        card = self.last_played
        if card.get_type() == Type.SKIP:
            self.skip()
        elif card.get_type() == Type.DRAW2:
            if not self.reversed:
                # if the current player is not the last player in the turn order it is safe to
                # make the next player draw two cards
                if self.current_player != self.player_count - 1:
                    for i in range(2):
                        self.players[self.current_player + 1].add_card(self.draw_card())
                    # when you are required to draw your turn is also skipped
                    self.skip()
                # if the current player is player 4 then assign the draw 2 to player 0 to avoid indexing out of bounds
                else:
                    for i in range(2):
                        self.players[0].add_card(self.draw_card())
                    # when you are required to draw your turn is also skipped
                    self.skip()
            # if it is currently reversed, do the opposite of above
            else:
                if self.current_player != 0:
                    for i in range(2):
                        self.players[self.current_player - 1].add_card(self.draw_card())
                    self.skip()
                # if the current player is player 0 then assign the draw 2 to player 4 to avoid indexing out of bounds
                else:
                    for i in range(2):
                        self.players[self.player_count - 1].add_card(self.draw_card())
                    self.skip()
        # if the power of the card is reverse, call the reverse function
        elif card.get_type() == Type.REVERSE:
            self.reverse()
        elif card.get_type() == Type.DRAW4:
            if not self.reversed:
                # if the current player is not the last player in the turn order it is safe to
                # make the next player draw four cards
                if self.current_player != self.player_count - 1:
                    for i in range(4):
                        self.players[self.current_player + 1].add_card(self.draw_card())
                    # when you are required to draw your turn is also skipped
                    self.skip()
                # if the current player is player 4, make player 0 draw four cards
                else:
                    for i in range(4):
                        self.players[0].add_card(self.draw_card())
                    # when you are required to draw your turn is also skipped
                    self.skip()
            # if it is currently reversed, do the opposite of above
            else:
                if self.current_player != 0:
                    for i in range(4):
                        self.players[self.current_player - 1].add_card(self.draw_card())
                    # when you are required to draw your turn is also skipped
                    self.skip()
                else:
                    for i in range(4):
                        self.players[self.player_count - 1].add_card(self.draw_card())
                    # when you are required to draw your turn is also skipped
                    self.skip()

    def fill_deck(self):
        color = Color.NONE
        # for loop with range 4 since there are 4 colors
        for i in range(4):
            # create 4 of each: wild and wild draw 4, 1 each time the loop passes
            self.deck.append(Card(Type.WILD))
            self.deck.append(Card(Type.DRAW4))
            # assign a color depending on i
            if i == 0:
                color = Color.YELLOW
            elif i == 1:
                color = Color.RED
            elif i == 2:
                color = Color.GREEN
            elif i == 3:
                color = Color.BLUE
            # there are only 1 zero card of each color
            self.deck.append(Card(Type.ZERO, color))
            # create 2 of each power card for each color
            for k in range(2):
                self.deck.append(Card(Type.SKIP, color))
                self.deck.append(Card(Type.DRAW2, color))
                self.deck.append(Card(Type.REVERSE, color))
            # create 2 of each number card from 1 to 9
            for j in range(1, 10):
                self.deck.append(Card(Type(j), color))
                self.deck.append(Card(Type(j), color))

    def draw_card(self):
        deck_length = len(self.deck)
        # if the deck is empty, shuffle the discard pile back in
        if deck_length == 0:
            self.shuffle_discard()
            deck_length = len(self.deck)
        # choose a random card
        card_num = random.randint(0, deck_length - 1)
        # remove the card from the deck
        card_selected = self.deck.pop(card_num)
        return card_selected

    def draw_first_card(self):
        while True:
            card = self.draw_card()
            card_type = card.get_type()
            # if the card drawn is a power card then discard it and draw again
            if card_type == Type.DRAW4 or card_type == Type.WILD or card_type == Type.SKIP or card_type == Type.DRAW2 \
                    or card_type == Type.REVERSE:
                self.played_deck.append(card)
                continue
            # continue until a value card is drawn
            else:
                self.played_deck.append(card)
                break
        return card

    def reverse(self):
        # if the game is not already reversed then set reverse to true
        if not self.reversed:
            self.reversed = True
        # if the game is currently reverse then set it to false
        else:
            self.reversed = False

    def fill_hand(self, player):
        # the game begins with each player having seven cards
        for i in range(0, 7):
            card = self.draw_card()
            player.add_card(card)

    # changes the current player variable according to reverse boolean and who last played
    def change_turn(self):
        if self.reversed:
            self.current_player -= 1
        else:
            self.current_player += 1
        if self.current_player > self.player_count - 1:
            self.current_player = 0
        elif self.current_player < 0:
            self.current_player = self.player_count - 1
