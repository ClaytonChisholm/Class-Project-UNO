from copy import copy
from time import sleep
from cpu import *
from card import *


# this function prompts the user for a choice of color after playing a wild or draw 4
def choose_color():  # change when graphics
    print(bg('red') + fg('white') + 'Red' + attr('reset') + ': 1')
    print(bg('green_4') + fg('white') + 'Green' + attr('reset') + ': 2')
    print(bg('dodger_blue_2') + fg('white') + 'Blue' + attr('reset') + ': 3')
    print(bg('yellow') + fg('white') + 'Yellow' + attr('reset') + ': 4')
    while True:  # loops until valid color choice is made and catches any non-integer input
        try:
            color = int(input('Enter the number corresponding to your preferred color: '))
            if not color < 1 and not color > 4:
                break
            else:
                print('That isn\'t a valid option...')
        except ValueError:
            print('Please try again, make sure to enter an integer corresponding to your choice...')
    return Color(color)


def display_rules():
    rules_text = "Welcome to the game of UNO! In this version, the goal of the game " \
                 "is to play all of the cards in your\n hand, and the first" \
                 " player to do this wins. Each player is dealt 7 cards at the start of"\
    " the game after the\n deck has been shuffled. There is a draw deck where"\
    " the players draw cards and a discard deck where the players play their\n cards."\
    " There are special and normal cards in the deck. The normal cards have a number"\
    "  from 0 to 9 and a color (red, green, blue, or yellow) and the "\
    "special cards have powers. These powers include:\n " \
    "Draw 2: where the"\
    " next person to play must draw two cards from the draw pile and lose their turn\n"\
    "Reverse: where the card reverses the direction of play (who goes next)\n"\
    "Skip card: which skips the next person in line to play\n"\
    "Wild card: where the player who played this card can change the color of the card being played\n"\
    "Draw 4 card: where the player can call the next color being played and requires the next\n"\
    " player to pick four cards from the draw pile and lose their turn\n In order to begin play,"\
    " the player must match the top card of the discard deck either by number,"\
    " color, or word and place their card to be played on top of the discard deck.\nThe player can play"\
    " a wild card or wild plus four card whenever it is their turn.\nIf the player playing does not have"\
    " a valid card to play, they must pick a card from the draw pile.\nIf you draw a card you can play,"\
    " play it.\nOtherwise, the next player starts their turn.\nIf the draw deck runs "\
    "out of cards, the discard deck will be reshuffled and become the draw deck.\nOnce the player plays"\
    " their card, play moves to the next person."\

    return rules_text


class Game:
    # player = Player(' ', 0)
    # cpu1 = CPU("Mark", 1)
    # cpu2 = CPU("Mira", 2)
    # cpu3 = CPU("Julia", 3)
    # players = [player, cpu1, cpu2, cpu3]
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
        # self.name = player_name
        # self.player.set_name(player_name)
        self.fill_deck()
        self.shuffle_deck()
        self.last_played = self.draw_first_card()  # special draw function that makes sure first card doesn't
        # have a special power

    def get_top_card(self):  # TODO, call this each cycle for printing.
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
        print('reshuffling deck')
        sleep(2)  # for ~~aesthetics~~
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
                print(self.players[self.current_player].get_name(), 'has lost their turn!\n')
            else:
                # assign the current player to the beginning of the turn order if it is currently player 4s turn
                self.current_player = 0
                # output who lost their turn so the player can see
                print('You have lost your turn!\n')
        # if it is currently reversed, do the opposite of above
        else:
            if self.current_player != 0:
                self.current_player = self.current_player - 1
                # output who lost their turn so the player can see
                print(self.players[self.current_player].get_name(), 'has lost their turn!\n')
            else:
                self.current_player = self.player_count - 1
                # output who lost their turn so the player can see
                print(self.players[self.current_player].get_name(), 'has lost their turn!\n')

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

    def set_wild(self):
        # call choose color to set the color of a wild card
        color = choose_color()
        self.last_played.set_wild(color)

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

    def choose_card(self, current_player):  # change with graphics
        # get user input whether they wish to draw or play
        card_choice = input('Enter D to draw a new card or enter P to play a card: ').upper()
        # validate user input
        while not card_choice == 'P' and not card_choice == 'D':
            card_choice = input(
                'Invalid choice please try again...\nEnter D to draw a new card or enter P to play a card: ').upper()
        # if user input was play card them get the user to choose a card
        if card_choice == 'P':
            card_num = current_player.choose_card()
            card = current_player.get_hand()[card_num]
        # if they drew, then draw a new card and tell the user what they drew
        else:
            new_card = self.draw_card()
            print('You picked up a ', end='')
            new_card.print()
            sleep(.5)
            print()
            # if the new card can be played, allow the player to play it
            if self.validate_move(new_card):  # checks to see if drawn card is a valid move
                # validate input
                while not card_choice == 'Y' and not card_choice == 'N':
                    print('Would you like to play it?', end='')
                    print(end=' ')
                    card_choice = input('Y or N?').upper()
                # if they choose yes then play the card
                if card_choice == 'Y':
                    return new_card
                # if they choose no then add the card to the hand
                elif card_choice == 'N':
                    current_player.add_card(new_card)
            current_player.add_card(new_card)  # adds to players hand if its not valid
            return False

        # while the chosen card is not valid, make them try again
        while not self.validate_move(card):
            print('Sorry that card is not valid...')
            sleep(.25)
            card_choice = input('Enter D to Draw a new card or enter P to play a card').upper()
            if card_choice == 'P':
                card_num = current_player.choose_card()
                card = current_player.get_hand()[card_num]
            elif card_choice == 'D':
                new_card = self.draw_card()
                if self.validate_move(new_card):  # checks to see if drawn card is a valid move
                    while not card_choice == 'Y' and not card_choice == 'N':
                        print('Would you like to play the', end=' ')
                        new_card.print()
                        print(end='; ')
                        card_choice = input('Y or N?').upper()
                    if card_choice == 'Y':
                        return new_card
                    else:
                        current_player.add_card(new_card)
                current_player.add_card(new_card)  # adds to players hand if its not valid
                return False
            else:
                print('Try again...')
        return current_player.get_hand().pop(card_num)

    # picks a card through calling the method corresponding to whichever player calls it
    def pick_card(self):
        current_player = self.players[self.current_player]
        if type(current_player) == Player:
            return self.choose_card(current_player)  # i separated this so it can be easily isolated for graphics
        else:  # CPU card picking
            if current_player.get_number() == 1:
                card = current_player.play_card(self.player, self.cpu3, self.cpu2, self.last_played)
            elif current_player.get_number() == 2:
                card = current_player.play_card(self.player, self.cpu1, self.cpu3, self.last_played)
            else:
                card = current_player.play_card(self.player, self.cpu1, self.cpu2, self.last_played)
            if not card:
                current_player.add_card(self.draw_card())
                if self.validate_move(current_player.get_hand()[len(current_player.get_hand()) - 1]):
                    return current_player.get_hand().pop(len(current_player.get_hand()) - 1)
                else:
                    return False  # returns false if no valid card is found
            else:
                return card  # returns card if one is found

    # prints the most recently played card and states who played it
    def print_played_card(self):  # change for graphic
        print(self.players[self.current_player].get_name(), 'played a', end=' ')
        self.last_played.print()
        print(end='\n\n')

    # prints the top card (only used for the first card since every other card is played by a player
    def print_top_card(self):
        print('Current card is a ', end='')
        self.last_played.print()
        print()

    # do_turns cycles each hand and changes the game states according to what card is played and by whom
    def do_turns(self):
        for player in self.players:  # creates starting hands
            self.fill_hand(player)
        self.print_top_card()  # shows first card

        while not self.game_over:  # game engine
            player = self.players[self.current_player]

            if type(player) == Player:
                for p in self.players:
                    p.print()  # prints the hand
            else:
                print('It\'s ' + player.get_name() + '\'s turn')
                sleep(1)
            picked_card = self.pick_card()

            if not picked_card:  # if no card could be played, next turn
                print(self.players[self.current_player].get_name(), 'drew a card.\n')
            elif type(picked_card) == Card:  # handles changing the game variables when a card is played
                if self.last_played.get_type() == Type.WILD or self.last_played.get_type() == Type.DRAW4:
                    self.last_played.set_wild(Color.NONE)  # resets wilds and draw fours from the previous turn, so
                    # they don't have a color after shuffling
                self.last_played = picked_card  # updates the last played card and adds it to the discard
                self.played_deck.append(self.last_played)

                # handles wilds
                if type(player) == Player and (
                        self.last_played.get_type() == Type.WILD or self.last_played.get_type() == Type.DRAW4):
                    self.set_wild()
                elif type(player) == CPU and (
                        self.last_played.get_type() == Type.WILD or self.last_played.get_type() == Type.DRAW4):
                    self.last_played.set_wild(player.cpu_wilds())  # sets the color of the wild with cpu choice

                # prints who played card
                self.print_played_card()
                self.apply_power()  # handles all non wild power cards

            # checks for game ending conditions and returns the winner
            if not player.get_hand() or (len(self.played_deck) == 0 and len(self.deck) == 0):
                self.game_over = True
                self.print_top_card()
                if type(player) == CPU:
                    return self.players[self.current_player].get_name() + ' wins.'  # returns winner CPU
                else:
                    return 'You Win!!!'

            self.change_turn()  # changes turn after loop processes


if __name__ == '__main__':
    while True:  # loops until program is quit
        print('Welcome to Uno! Enter \'S\' to start a new game? Enter \'R\' to see the rules. Or enter \'Q\' to quit.')
        choice = input('').upper()
        if choice == 'Q' or choice == 'R' or choice == 'H' or choice == 'S':
            if choice == 'Q':  # quits the program
                print('Thanks for playing!')
                break
            elif choice == 'R' or choice == 'H':  # gets the rules
                display_rules()
                print()
            else:  # if its not the other two, the game is run
                # game = Game(input('What\'s your name?'))
                # print(game.do_turns())
                new_game = Game()
                print(new_game.do_turns())
        else:  # handles invalid strings
            print('Not a valid choice...')
