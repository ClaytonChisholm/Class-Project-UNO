import pygame
import sys
from game import *
import pygame_textinput
from time import sleep

# Global list
list_of_rect_card = []

# Global colors
white = (255, 255, 255)
grey = (180, 180, 180)
red = (245, 100, 98)
blue = (0, 195, 229)
green = (47, 226, 155)
yellow = (247, 227, 89)
black = [150, 150, 150]

# light shade of the button
button_hover_color = (170, 170, 170)

# dark shade of the button
button_color = (100, 100, 100)

# defining font
tiny_font = pygame.font.SysFont('Corbel', 25)
small_font = pygame.font.SysFont('Corbel', 35)
name_font = pygame.font.SysFont('Corbel', 25, True)

# background for game
table = pygame.image.load('NaturalOak.jpg')
table = pygame.transform.rotate(table, 90)
table = pygame.transform.scale(table, (1200, 800))


def game_engine():
    # Initialize Screen
    pygame.init()
    screen_size = (1200, 800)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('UNO!')
    screen.fill(black)

    # Rendering a text written in this font
    text_quit = small_font.render('Quit', True, white)
    text_new_game = tiny_font.render('New Game', True, white)
    text_rules = small_font.render('Rules', True, white)
    background = pygame.image.load("background.png")

    # Game booleans
    win = False
    game_over = True

    # Screen booleans
    show_menu = True
    show_rules = False
    show_results = False

    # Menu screen

    while show_menu:
        # Stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()
        width = screen.get_width()
        height = screen.get_height()
        button_width = 140
        button_height = 40
        new_game_button_x = (width * .5) - (button_width / 2)
        quit_button_x = (width * .75) - (button_width / 2)
        rules_button_x = (width * .25) - (button_width / 2)
        button_y = (height * .75) + (button_height / 2)

        # Background
        screen.fill(white)
        screen.blit(background, (screen.get_width() / 2 - 450, 100))
        # Border
        pygame.draw.rect(screen, blue, [0, 0, 20, 800])
        pygame.draw.rect(screen, green, [1180, 0, 20, 800])
        pygame.draw.rect(screen, red, [0, 0, 1200, 20])
        pygame.draw.rect(screen, yellow, [0, 780, 1200, 20])

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # mouse events
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                # Button event for quitting the game
                if quit_button_x <= mouse[0] <= quit_button_x + button_width and button_y <= mouse[
                        1] <= button_y + button_height:
                    pygame.quit()
                    sys.exit()

                # Button event for starting the game
                if new_game_button_x <= mouse[0] <= new_game_button_x + button_width and button_y <= mouse[
                        1] <= button_y + button_height:
                    game_over = False

                # Button event for showing the rules screen
                if rules_button_x <= mouse[0] <= rules_button_x + button_width and button_y <= mouse[
                        1] <= button_y + button_height:
                    show_rules = True
        # Drawing buttons

        # New game button
        if new_game_button_x <= mouse[0] <= new_game_button_x + button_width and button_y <= mouse[
                1] <= button_y + button_height:
            pygame.draw.rect(screen, button_hover_color, [new_game_button_x, button_y, 140, 40])
        else:
            pygame.draw.rect(screen, button_color, [new_game_button_x, button_y, 140, 40])

        # Quit button
        if quit_button_x <= mouse[0] <= quit_button_x + button_width and button_y <= mouse[
                1] <= button_y + button_height:
            pygame.draw.rect(screen, button_hover_color, [quit_button_x, button_y, 140, 40])
        else:
            pygame.draw.rect(screen, button_color, [quit_button_x, button_y, 140, 40])

        # Rules button
        if rules_button_x <= mouse[0] <= rules_button_x + button_width and button_y <= mouse[
                1] <= button_y + button_height:
            pygame.draw.rect(screen, button_hover_color, [rules_button_x, button_y, 140, 40])
        else:
            pygame.draw.rect(screen, button_color, [rules_button_x, button_y, 140, 40])

        # superimposing the text onto our buttons
        screen.blit(text_quit, (quit_button_x + 40, button_y + 3))
        screen.blit(text_new_game, (new_game_button_x + 15, button_y + 7))
        screen.blit(text_rules, (rules_button_x + 30, button_y + 3))

        # updates the frames of the game
        pygame.display.update()

        if show_rules or not game_over:
            show_menu = False

    # show rules screen

    if show_rules:
        print_rules(screen)

    # game screen

    if not game_over:
        # Get text input from user for name
        text_input = pygame_textinput.TextInput('', font_family='Corbel')
        text = True
        while text:
            # set background color
            screen.fill((225, 225, 225))
            text_enter = small_font.render('Enter Name', True, black)
            screen.blit(text_enter, (screen.get_width() / 2 - 70, 300))
            events = pygame.event.get()
            # Keyboard events
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    text = False
            # Feed it with events every frame
            text_input.update(events)
            # Blit its surface onto the screen
            screen.blit(text_input.get_surface(), (screen.get_width() / 2 - (len(text_input.get_text()) * 18) / 2,
                                                   screen.get_height() / 2))
            pygame.display.update()

        # Setting game screen
        screen = pygame.display.set_mode(screen_size)
        screen.fill((0, 0, 0))
        # Creating CPU objects
        cpu1 = CPU("Mark", 1)
        cpu2 = CPU("Mira", 2)
        cpu3 = CPU("Julia", 3)
        # Creating player object
        name = text_input
        player = Player(name, 0)
        # initialize game
        game = Game(cpu1, cpu2, cpu3, player)
        for player in game.players:  # creates starting hands
            game.fill_hand(player)
        screen = pygame.display.set_mode(screen_size)
        screen.fill(black)
        # Print deck
        print_top_card(game, screen)

        while not game_over:  # game engine
            # player goes first
            player = game.players[game.current_player]
            print_game(game, screen)
            pygame.display.update()
            picked_card = choose_card(screen, game)
            # Sleep if CPU's turn
            if type(player) == CPU:
                print_game(game, screen)
                pygame.display.update()
                sleep(random.random() + .25)
            if not picked_card:
                pass
            elif type(picked_card) == Card:  # handles changing the game variables when a card is played
                if game.last_played.get_type() == Type.WILD or game.last_played.get_type() == Type.DRAW4:
                    game.last_played.set_wild(Color.NONE)  # resets wilds and draw fours from the previous turn, so
                    # they don't have a color after shuffling
                game.last_played = picked_card  # updates the last played card and adds it to the discard
                game.played_deck.append(game.last_played)

                # handles wilds
                # Player wild
                if type(player) == Player and (
                        game.last_played.get_type() == Type.WILD or game.last_played.get_type() == Type.DRAW4):
                    color = set_wild(screen)
                    game.last_played.set_wild(color)
                    print_game(game, screen)
                # CPU wild
                elif type(player) == CPU and (
                        game.last_played.get_type() == Type.WILD or game.last_played.get_type() == Type.DRAW4):
                    game.last_played.set_wild(player.cpu_wilds())  # sets the color of the wild with cpu choice
                game.apply_power()
            # handles all non wild power cards
            if not player.get_hand() or (len(game.played_deck) == 0):
                game_over = True
                # If player won, set win boolean to True
                if type(player) == Player and not player.get_hand():
                    win = True
                # Show results
                show_results = True

            if type(player) == CPU:
                print_game(game, screen)
                pygame.display.update()

            elif type(player) == Player:
                print_game(game, screen)
                pygame.display.update()
            # Next turn
            game.change_turn()

    # Results screen

    if show_results:
        screen = pygame.display.set_mode(screen_size)
        # Text
        win_text = small_font.render('You Win!', True, [0, 0, 0])
        lose_text = small_font.render('You lost, better luck next round', True, white)
        if win:
            screen.fill(white)
            screen.blit(win_text, (screen.get_width() / 2 - 50, 400))
        else:
            screen.fill(black)
            screen.blit(lose_text, ((screen.get_width() / 2) - 150, 400))
        # Border
        pygame.draw.rect(screen, blue, [0, 0, 20, 800])
        pygame.draw.rect(screen, green, [1180, 0, 20, 800])
        pygame.draw.rect(screen, red, [0, 0, 1200, 20])
        pygame.draw.rect(screen, yellow, [0, 780, 1200, 20])
        # button Font
        text_back = tiny_font.render('     Menu', True, black)
        while show_results:
            # Button variables
            button_width = 140
            button_height = 40
            width = screen.get_width()
            height = screen.get_height()
            menu_back_x = (width * .1) - (button_width / 2)
            button_y = (height * .85) + (button_height / 2)
            mouse = pygame.mouse.get_pos()

            # Events
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                    # Menu Button
                    if menu_back_x <= mouse[0] <= menu_back_x + button_width and button_y <= mouse[1] <= button_y + \
                            button_height:
                        show_results = False
                        game_engine()

            # Drawing buttons
            # Menu button
            if menu_back_x <= mouse[0] <= menu_back_x + button_width and button_y <= mouse[1] <= button_y + \
                    button_height:
                pygame.draw.rect(screen, button_hover_color, [menu_back_x, button_y, 140, 40])
            else:
                pygame.draw.rect(screen, button_color, [menu_back_x, button_y, 140, 40])

            # superimposing the text onto our buttons
            screen.blit(text_back, (menu_back_x + 15, button_y + 10))

            # updates the frames of the game
            pygame.display.update()


def print_cpu_hands(game, screen):
    cpus = [game.cpu1, game.cpu2, game.cpu3]
    for i in range(len(cpus)):
        cpu = cpus[i]
        hand_size = len(cpu.get_hand())
        if i == 0:
            hand_start = 0
            hand_height = screen.get_height() * (1 / 6)
            # this is if cpu is on left of screen
            if hand_size <= 3:

                card_offset = hand_height - 30 + (.5 * (3 - hand_size) * 120)
                for _ in cpu.get_hand():
                    card_face = pygame.image.load('cards/card_back.png')
                    card_face = pygame.transform.scale(card_face, (100, 140))
                    card_face = pygame.transform.rotate(card_face, -90)
                    card_rect = card_face.get_rect()
                    # transforms to default size
                    card_rect.y = hand_height + card_offset
                    card_rect.x = hand_start + 30
                    screen.blit(card_face, card_rect)

                    card_offset += 120  # card size plus space between cards

            else:
                card_offset = 30
                max_size = screen.get_height() * 2 / 3 - 120
                hand_width = 120 * hand_size
                overlap = 0
                while max_size < hand_width:
                    overlap += 1
                    hand_width = (120 - overlap) * hand_size

                for _ in cpu.get_hand():
                    card_face = pygame.image.load('cards/card_back.png')
                    card_face = pygame.transform.scale(card_face, (100, 140))  # transforms to default size
                    card_face = pygame.transform.rotate(card_face, -90)
                    card_rect = card_face.get_rect()
                    card_rect.y = hand_height + card_offset
                    card_rect.x = hand_start + 30
                    screen.blit(card_face, card_rect)
                    card_rect.width = card_rect.width - overlap
                    card_offset += 120 - overlap

        elif i == 1:
            # this is if cpu is on top of screen
            hand_height = 0
            hand_start = screen.get_width() * (1 / 6)
            if hand_size <= 6:

                card_offset = hand_start + 30 + (.5 * (6 - hand_size) * 120)
                for _ in cpu.get_hand():
                    card_face = pygame.image.load('cards/card_back.png')
                    card_face = pygame.transform.scale(card_face, (100, 140))
                    card_face = pygame.transform.rotate(card_face, 180)
                    card_rect = card_face.get_rect()
                    # transforms to default size
                    card_rect.y = hand_height + 30
                    card_rect.x = card_offset
                    screen.blit(card_face, card_rect)
                    card_offset += 120  # card size plus space between cards

            else:
                card_offset = hand_start + 30
                max_size = screen.get_width() * 2 / 3 - 60
                hand_width = 120 * hand_size
                overlap = 0
                while max_size < hand_width:
                    overlap += 1
                    hand_width = (120 - overlap) * hand_size

                for _ in cpu.get_hand():
                    card_face = pygame.image.load('cards/card_back.png')
                    card_face = pygame.transform.scale(card_face, (100, 140))  # transforms to default size
                    card_face = pygame.transform.rotate(card_face, 180)
                    card_rect = card_face.get_rect()
                    card_rect.y = hand_height + 30
                    card_rect.x = card_offset
                    screen.blit(card_face, card_rect)
                    card_rect.width = card_rect.width - overlap
                    card_offset += 120 - overlap

        else:
            hand_start = screen.get_width() - 200
            hand_height = screen.get_height() * (1 / 6)
            if hand_size <= 3:

                card_offset = hand_height - 30 + (.5 * (3 - hand_size) * 120)
                for _ in cpu.get_hand():
                    card_face = pygame.image.load('cards/card_back.png')
                    card_face = pygame.transform.scale(card_face, (100, 140))
                    card_face = pygame.transform.rotate(card_face, 90)
                    card_rect = card_face.get_rect()
                    # transforms to default size
                    card_rect.y = hand_height + card_offset
                    card_rect.x = hand_start + 30
                    screen.blit(card_face, card_rect)

                    card_offset += 120  # card size plus space between cards

            else:
                card_offset = 30
                max_size = screen.get_height() * 2 / 3 - 120
                hand_width = 120 * hand_size
                overlap = 0
                while max_size < hand_width:
                    overlap += 1
                    hand_width = (120 - overlap) * hand_size
                for _ in cpu.get_hand():
                    card_face = pygame.image.load('cards/card_back.png')
                    card_face = pygame.transform.scale(card_face, (100, 140))  # transforms to default size
                    card_face = pygame.transform.rotate(card_face, 90)
                    card_rect = card_face.get_rect()
                    card_rect.y = hand_height + card_offset
                    card_rect.x = hand_start + 30
                    screen.blit(card_face, card_rect)
                    card_rect.width = card_rect.width - overlap
                    card_offset += 120 - overlap
            # if cpu is on right side


def print_player_hand(game, screen: pygame.Surface):
    list_of_rect_card.clear()
    player = game.player
    hand_size = len(player.get_hand())
    hand_height = screen.get_height() - 200
    hand_start = screen.get_width() * (1 / 6)

    if hand_size <= 6:

        card_offset = hand_start + 30 + (.5 * (6 - hand_size) * 120)
        for card in player.get_hand():
            card_face = pygame.image.load(card.get_path())
            card_face = pygame.transform.scale(card_face, (100, 140))
            card_rect = card_face.get_rect()
            # transforms to default size
            card_rect.y = hand_height + 30
            card_rect.x = card_offset
            screen.blit(card_face, card_rect)
            list_of_rect_card.append(card_rect)
            card_offset += 120  # card size plus space between cards

    else:
        card_offset = hand_start + 30
        max_size = screen.get_width() * 2 / 3 - 60
        hand_width = 120 * hand_size
        overlap = 0
        while max_size < hand_width:
            overlap += 1
            hand_width = (120 - overlap) * hand_size

        for card in player.get_hand():
            card_face = pygame.image.load(card.get_path())
            card_face = pygame.transform.scale(card_face, (100, 140))  # transforms to default size
            card_rect = card_face.get_rect()
            card_rect.y = hand_height + 30
            card_rect.x = card_offset
            screen.blit(card_face, card_rect)
            card_rect.width = card_rect.width - overlap
            list_of_rect_card.append(card_rect)
            card_offset += 120 - overlap


def print_top_card(game, screen):
    top_card = print_card(game.last_played)
    deck_cover = pygame.image.load('cards/card_back.png')
    deck_cover = pygame.transform.scale(deck_cover, (100, 140))
    screen.blit(top_card, (((screen.get_width() / 2) - 120), (screen.get_height() / 2) - 70))
    screen.blit(deck_cover, (((screen.get_width() / 2) + 20), (screen.get_height() / 2) - 70))


def print_card(card):
    graphics_card = pygame.image.load(card.get_path())
    graphics_card = pygame.transform.scale(graphics_card, (100, 140))
    return graphics_card


def choose_card(screen, game):
    current_player = game.players[game.current_player]
    deck_cover = pygame.image.load('cards/card_back.png')
    deck_cover = pygame.transform.scale(deck_cover, (100, 140))
    deck_rect = deck_cover.get_rect()
    deck_rect.x = (screen.get_width() / 2) + 20
    deck_rect.y = (screen.get_height() / 2) - 70
    screen.blit(deck_cover, deck_rect)
    user_answer = False

    # while user has not played or drawn a card from the deck
    while user_answer is False and type(game.players[game.current_player]) == Player:

        while True:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:

                    if deck_rect.collidepoint(ev.pos):
                        card = game.draw_card()
                        deck_cover = pygame.image.load('cards/card_back.png')
                        deck_cover = pygame.transform.scale(deck_cover, (100, 140))
                        deck_cover_rect = deck_cover.get_rect()
                        deck_cover_rect.x = (screen.get_width() / 2) + 20
                        deck_cover_rect.y = (screen.get_height() / 2) - 70
                        for x in range(20):
                            # re-update screen every time card moves up # of pixels
                            print_game(game, screen)
                            # move card object up 10 pixels at a time
                            deck_cover_rect = deck_cover_rect.move(0, 10)
                            screen.blit(deck_cover, deck_cover_rect)  # blit it to the new position
                            pygame.display.update()
                            pygame.time.delay(10)

                        # re-update screen once card animation is over
                        print_game(game, screen)

                        if game.validate_move(card):
                            card_face = pygame.image.load(card.get_path())
                            card_face = pygame.transform.scale(card_face, (100, 140))
                            card_rect = card_face.get_rect()

                            # confirm if user wants to play drawn card
                            result = confirm_user_card(card, card_rect, screen)

                            # update screen after user confirmation
                            print_game(game, screen)

                            # if the user wants to play it, play card
                            if result:
                                card_rect.x = (screen.get_width() / 2) - 50
                                card_rect.y = screen.get_height() - 170
                                for x in range(20):
                                    # re-update screen every time card moves up # of pixels
                                    print_game(game, screen)

                                    # move card object up 10 pixels at a time
                                    card_rect = card_rect.move(0, -10)
                                    screen.blit(card_face, card_rect)  # blit it to the new position
                                    pygame.time.delay(10)  # add time delay so it doesn't happen all at once
                                    pygame.display.update()
                                return card

                            # otherwise add to user hand
                            else:
                                current_player.add_card(card)
                                return False
                        else:
                            current_player.add_card(card)
                            return False

                    # checks to see which card user clicked on
                    for i in range(len(list_of_rect_card)):
                        if list_of_rect_card[i].collidepoint(ev.pos):
                            rect_position = list_of_rect_card[i]  # gets rectangle card object user clicked on

                            # calls to confirm card to confirm user selection of card played
                            user_answer = confirm_user_card(current_player.get_hand()[i], rect_position, screen)

                            # if user wants to play their card, update screen and play card
                            if user_answer:

                                # updates screen
                                print_game(game, screen)

                                if game.validate_move(current_player.get_hand()[i]):
                                    position = list_of_rect_card.pop(i)
                                    pygame.display.update()
                                    card_played = pygame.image.load(current_player.get_hand()[i].get_path())
                                    card_selected = current_player.get_hand().pop(i)
                                    # re-update screen once card animation is over

                                    # animation part: kinda of buggy but works?
                                    for x in range(20):
                                        # re-update screen every time card moves up # of pixels
                                        print_game(game, screen)

                                        # move card object up 10 pixels at a time
                                        position = position.move(0, -10)
                                        screen.blit(card_played, position)  # blit it to the new position
                                        pygame.time.delay(10)  # add time delay so it doesn't happen all at once
                                        pygame.display.update()

                                    # re-update screen once card animation is over
                                    print_game(game, screen)
                                    return card_selected
                                pygame.display.update()
                            # if the user does not want to play the selected card, re-update screen
                            # and let them select again
                            elif user_answer is False:

                                print_game(game, screen)
                                pygame.display.update()

                    # else:
                    # print("not clicked")

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    card_face = pygame.image.load('cards/card_back.png')
    card_face = pygame.transform.scale(card_face, (100, 140))

    if current_player.get_number() == 1:
        card_face = pygame.transform.rotate(card_face, -90)
        card_rect = card_face.get_rect()
        card_rect.x = 30
        card_rect.y = (screen.get_height() / 2) - 50
        direction = (10, 0)
        card = current_player.play_card(game.player, game.cpu3, game.cpu2, game.last_played)
        pygame.display.update()

    elif current_player.get_number() == 2:
        card_face = pygame.transform.rotate(card_face, 180)
        card_rect = card_face.get_rect()
        card_rect.x = (screen.get_width() / 2) - 50
        card_rect.y = 30
        direction = (0, 10)
        card = current_player.play_card(game.player, game.cpu1, game.cpu3, game.last_played)
        pygame.display.update()

    else:  # right
        card_face = pygame.transform.rotate(card_face, 90)
        card_rect = card_face.get_rect()
        card_rect.x = screen.get_width() - 170
        card_rect.y = (screen.get_height() / 2) - 50
        direction = (-10, 0)
        card = current_player.play_card(game.player, game.cpu1, game.cpu2, game.last_played)
        pygame.display.update()

    if not card:
        current_player.add_card(game.draw_card())
        if game.validate_move(current_player.get_hand()[len(current_player.get_hand()) - 1]):
            print_game(game, screen)
            # move card object up 10 pixels at a time
            for x in range(20):
                print_game(game, screen)
                deck_rect = deck_rect.move(-5, 0)
                screen.blit(card_face, deck_rect)  # blit it to the new position
                pygame.time.delay(10)
                pygame.display.update()
            print_game(game, screen)
            return current_player.get_hand().pop(len(current_player.get_hand()) - 1)

        else:
            for x in range(20):
                # re-update screen every time card moves up # of pixels
                print_game(game, screen)

                # move card object up 10 pixels at a time
                deck_rect = deck_rect.move(-(direction[0]), -(direction[1]))
                screen.blit(card_face, deck_rect)  # blit it to the new position
                pygame.time.delay(10)  # add time delay so it doesn't happen all at once
                pygame.display.update()
            print_game(game, screen)
            return False  # returns false if no valid card is found
    else:

        for x in range(20):
            # re-update screen every time card moves up # of pixels
            # screen.fill(black)
            print_game(game, screen)

            # move card object up 10 pixels at a time
            card_rect = card_rect.move(direction)
            screen.blit(card_face, card_rect)  # blit it to the new position
            pygame.time.delay(10)  # add time delay so it doesn't happen all at once
            pygame.display.update()
        print_game(game, screen)

        return card  # returns card if one is found


def confirm_user_card(card_selected, rectangle, screen):
    screen.fill(black)  # clear the screen
    button_height = 100
    button_width = 150

    pygame.display.update()
    card_played = pygame.image.load(card_selected.get_path())
    rectangle.x = screen.get_width() / 2 - 75
    rectangle.y = screen.get_height() / 2 - 75

    # blit the card selected by user to screen
    screen.blit(card_played, rectangle)

    # yes or no buttons for user selection
    yes_button = pygame.draw.rect(screen, blue,
                                  [screen.get_width() / 2 - 165, screen.get_height() / 2 + 200, button_width,
                                   button_height])
    no_button = pygame.draw.rect(screen, red,
                                 [screen.get_width() / 2 - 165 + 160, screen.get_height() / 2 + 200, button_width,
                                  button_height])
    yes = small_font.render('Yes', True, black)
    no = small_font.render('No', True, black)

    # blit buttons and text description to screen
    description = small_font.render("Would you like to play this card?", True, white)
    screen.blit(yes, (screen.get_width() / 2 - 110, screen.get_height() / 2 + 235))
    screen.blit(no, (screen.get_width() / 2 - 110 + 160, screen.get_height() / 2 + 235))
    screen.blit(description, (screen.get_width() / 2 - 200, screen.get_height() / 2 - 150))
    pygame.display.update()

    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                mouse = pygame.mouse.get_pos()
                # if yes button is clicked on
                if yes_button.x <= mouse[0] <= yes_button.x + button_width and yes_button.y <= mouse[
                        1] <= yes_button.y + button_height:
                    return True
                # if no button is clicked on
                if no_button.x <= mouse[0] <= no_button.x + button_width and no_button.y <= mouse[
                        1] <= no_button.y + button_height:
                    return False


def set_wild(screen):
    button_size = 150
    blue_button = pygame.draw.rect(screen, blue,
                                   [(screen.get_width() / 2) - button_size - 75, (screen.get_height() / 2) - 75,
                                    button_size, button_size])
    yellow_button = pygame.draw.rect(screen, yellow,
                                     [(screen.get_width() / 2) + button_size - 75, (screen.get_height() / 2) - 75,
                                      button_size, button_size])
    red_button = pygame.draw.rect(screen, red,
                                  [(screen.get_width() / 2) - 75, (screen.get_height() / 2) - button_size - 75,
                                   button_size, button_size])
    green_button = pygame.draw.rect(screen, green,
                                    [(screen.get_width() / 2) - 75, (screen.get_height() / 2) + button_size - 75,
                                     button_size, button_size])

    pygame.display.update()

    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

                # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                mouse = pygame.mouse.get_pos()
                # if the mouse is clicked on the
                # button the game is terminated
                if blue_button.x <= mouse[0] <= blue_button.x + button_size and blue_button.y <= mouse[
                        1] <= blue_button.y + button_size:
                    return Color.BLUE
                elif red_button.x <= mouse[0] <= red_button.x + button_size and red_button.y <= mouse[
                        1] <= red_button.y + button_size:
                    return Color.RED
                elif green_button.x <= mouse[0] <= green_button.x + button_size and green_button.y <= mouse[
                        1] <= green_button.y + button_size:
                    return Color.GREEN
                elif yellow_button.x <= mouse[0] <= yellow_button.x + button_size and yellow_button.y <= mouse[
                        1] <= yellow_button.y + button_size:
                    return Color.YELLOW


def print_arrows(game, screen):
    arrow_player_x = (screen.get_width() / 2) - 75
    arrow_player_y = (screen.get_height() / 2) + 100
    arrow_highlight_player = pygame.image.load('arrows/light_arrow_player.png')
    arrow_highlight_reverse_player = pygame.image.load('arrows/light_arrow_reverse_player.png')
    arrow_dark_player = pygame.image.load('arrows/dark_arrow_player.png')
    arrow_dark_reverse_player = pygame.image.load('arrows/dark_arrow_reverse_player.png')
    if not game.reversed and game.current_player == 0:
        arrow_player_rect = arrow_highlight_player.get_rect()
        arrow_player_rect.x = arrow_player_x
        arrow_player_rect.y = arrow_player_y
        screen.blit(arrow_highlight_player, arrow_player_rect)
    elif not game.reversed and game.current_player != 0:
        arrow_player_rect = arrow_dark_player.get_rect()
        arrow_player_rect.x = arrow_player_x
        arrow_player_rect.y = arrow_player_y
        screen.blit(arrow_dark_player, arrow_player_rect)
    elif game.reversed and game.current_player == 0:
        arrow_player_rect = arrow_highlight_reverse_player.get_rect()
        arrow_player_rect.x = arrow_player_x
        arrow_player_rect.y = arrow_player_y
        screen.blit(arrow_highlight_reverse_player, arrow_player_rect)
    elif game.reversed and game.current_player != 0:
        arrow_player_rect = arrow_dark_reverse_player.get_rect()
        arrow_player_rect.x = arrow_player_x
        arrow_player_rect.y = arrow_player_y
        screen.blit(arrow_dark_reverse_player, arrow_player_rect)
    arrow_cpu1_x = (screen.get_width() / 2) - 200
    arrow_cpu1_y = (screen.get_height() / 2) - 75
    arrow_highlight_cpu1 = pygame.image.load('arrows/light_arrow_cpu1.png')
    arrow_highlight_reverse_cpu1 = pygame.image.load('arrows/light_arrow_reverse_cpu1.png')
    arrow_dark_cpu1 = pygame.image.load('arrows/dark_arrow_cpu1.png')
    arrow_dark_reverse_cpu1 = pygame.image.load('arrows/dark_arrow_reverse_cpu1.png')
    if not game.reversed and game.current_player == 1:
        arrow_cpu1_rect = arrow_highlight_cpu1.get_rect()
        arrow_cpu1_rect.x = arrow_cpu1_x
        arrow_cpu1_rect.y = arrow_cpu1_y
        screen.blit(arrow_highlight_cpu1, arrow_cpu1_rect)
    elif not game.reversed and game.current_player != 1:
        arrow_cpu1_rect = arrow_dark_cpu1.get_rect()
        arrow_cpu1_rect.x = arrow_cpu1_x
        arrow_cpu1_rect.y = arrow_cpu1_y
        screen.blit(arrow_dark_cpu1, arrow_cpu1_rect)
    elif game.reversed and game.current_player == 1:
        arrow_cpu1_rect = arrow_highlight_reverse_cpu1.get_rect()
        arrow_cpu1_rect.x = arrow_cpu1_x
        arrow_cpu1_rect.y = arrow_cpu1_y
        screen.blit(arrow_highlight_reverse_cpu1, arrow_cpu1_rect)
    elif game.reversed and game.current_player != 1:
        arrow_cpu1_rect = arrow_dark_reverse_cpu1.get_rect()
        arrow_cpu1_rect.x = arrow_cpu1_x
        arrow_cpu1_rect.y = arrow_cpu1_y
        screen.blit(arrow_dark_reverse_cpu1, arrow_cpu1_rect)
    arrow_cpu2_x = (screen.get_width() / 2) - 75
    arrow_cpu2_y = (screen.get_height() / 2) - 160
    arrow_highlight_cpu2 = pygame.image.load('arrows/light_arrow_cpu2.png')
    arrow_highlight_reverse_cpu2 = pygame.image.load('arrows/light_arrow_reverse_cpu2.png')
    arrow_dark_cpu2 = pygame.image.load('arrows/dark_arrow_cpu2.png')
    arrow_dark_reverse_cpu2 = pygame.image.load('arrows/dark_arrow_reverse_cpu2.png')
    if not game.reversed and game.current_player == 2:
        arrow_cpu2_rect = arrow_highlight_cpu2.get_rect()
        arrow_cpu2_rect.x = arrow_cpu2_x
        arrow_cpu2_rect.y = arrow_cpu2_y
        screen.blit(arrow_highlight_cpu2, arrow_cpu2_rect)
    elif not game.reversed and game.current_player != 2:
        arrow_cpu2_rect = arrow_dark_cpu2.get_rect()
        arrow_cpu2_rect.x = arrow_cpu2_x
        arrow_cpu2_rect.y = arrow_cpu2_y
        screen.blit(arrow_dark_cpu2, arrow_cpu2_rect)
    elif game.reversed and game.current_player == 2:
        arrow_cpu2_rect = arrow_highlight_reverse_cpu2.get_rect()
        arrow_cpu2_rect.x = arrow_cpu2_x
        arrow_cpu2_rect.y = arrow_cpu2_y
        screen.blit(arrow_highlight_reverse_cpu2, arrow_cpu2_rect)
    elif game.reversed and game.current_player != 2:
        arrow_cpu2_rect = arrow_dark_reverse_cpu2.get_rect()
        arrow_cpu2_rect.x = arrow_cpu2_x
        arrow_cpu2_rect.y = arrow_cpu2_y
        screen.blit(arrow_dark_reverse_cpu2, arrow_cpu2_rect)
    arrow_cpu3_x = (screen.get_width() / 2) + 140
    arrow_cpu3_y = (screen.get_height() / 2) - 75
    arrow_highlight_cpu3 = pygame.image.load('arrows/light_arrow_cpu3.png')
    arrow_highlight_reverse_cpu3 = pygame.image.load('arrows/light_arrow_reverse_cpu3.png')
    arrow_dark_cpu3 = pygame.image.load('arrows/dark_arrow_cpu3.png')
    arrow_dark_reverse_cpu3 = pygame.image.load('arrows/dark_arrow_reverse_cpu3.png')
    if not game.reversed and game.current_player == 3:
        arrow_cpu3_rect = arrow_highlight_cpu3.get_rect()
        arrow_cpu3_rect.x = arrow_cpu3_x
        arrow_cpu3_rect.y = arrow_cpu3_y
        screen.blit(arrow_highlight_cpu3, arrow_cpu3_rect)
    elif not game.reversed and game.current_player != 3:
        arrow_cpu3_rect = arrow_dark_cpu3.get_rect()
        arrow_cpu3_rect.x = arrow_cpu3_x
        arrow_cpu3_rect.y = arrow_cpu3_y
        screen.blit(arrow_dark_cpu3, arrow_cpu3_rect)
    elif game.reversed and game.current_player == 3:
        arrow_cpu3_rect = arrow_highlight_reverse_cpu3.get_rect()
        arrow_cpu3_rect.x = arrow_cpu3_x
        arrow_cpu3_rect.y = arrow_cpu3_y
        screen.blit(arrow_highlight_reverse_cpu3, arrow_cpu3_rect)
    elif game.reversed and game.current_player != 3:
        arrow_cpu3_rect = arrow_dark_reverse_cpu3.get_rect()
        arrow_cpu3_rect.x = arrow_cpu3_x
        arrow_cpu3_rect.y = arrow_cpu3_y
        screen.blit(arrow_dark_reverse_cpu3, arrow_cpu3_rect)


def print_names(game, screen):
    player_name = name_font.render(game.players[0].get_name().get_text(), True, white)
    cpu1_name = name_font.render(game.players[1].get_name(), True, white)
    cpu2_name = name_font.render(game.players[2].get_name(), True, white)
    cpu3_name = name_font.render(game.players[3].get_name(), True, white)
    screen.blit(player_name, ((screen.get_width() / 2) - len(game.players[0].get_name().get_text()) * 6, 570))
    screen.blit(cpu2_name, ((screen.get_width() / 2) - len(game.players[1].get_name()) * 6, 205))
    screen.blit(cpu1_name, (205, (screen.get_height() / 2) - 10))
    screen.blit(cpu3_name, (1000 - len(game.players[1].get_name()) * 12, (screen.get_height() / 2) - 10))


def draw_uno(screen):
    uno = pygame.image.load('background.png')
    uno = pygame.transform.scale(uno, (135, 95))
    screen.blit(uno, (screen.get_width() - 165, screen.get_height() - 138))


def print_rules(screen):
    rules_png = pygame.image.load('rules.PNG')
    screen = pygame.display.set_mode(screen.get_size())
    text_back = tiny_font.render('     Menu', True, black)
    screen.fill(white)
    screen.blit(rules_png, (20, 20))
    pygame.draw.rect(screen, blue, [0, 0, 20, 800])
    pygame.draw.rect(screen, green, [1180, 0, 20, 800])
    pygame.draw.rect(screen, red, [0, 0, 1200, 20])
    pygame.draw.rect(screen, yellow, [0, 780, 1200, 20])
    show_rules = True
    while show_rules:
        button_width = 140
        button_height = 40
        width = screen.get_width()
        height = screen.get_height()
        menu_back_x = (width * .1) - (button_width / 2)
        button_y = (height * .85) + (button_height / 2)
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:

                if menu_back_x <= mouse[0] <= menu_back_x + button_width and button_y <= mouse[
                        1] <= button_y + button_height:
                    show_rules = False
                    game_engine()
                elif menu_back_x <= mouse[0] <= menu_back_x + button_width and button_y <= mouse[
                        1] <= button_y + button_height:
                    show_rules = False

        # if the mouse is clicked on the
        # button the game is terminated
        if menu_back_x <= mouse[0] <= menu_back_x + button_width and button_y <= mouse[
                1] <= button_y + button_height:
            pygame.draw.rect(screen, button_hover_color, [menu_back_x, button_y, 140, 40])
        else:
            pygame.draw.rect(screen, button_color, [menu_back_x, button_y, 140, 40])
        screen.blit(text_back, (menu_back_x + 15, button_y + 10))

        # updates the frames of the game
        pygame.display.update()


def print_game(game, screen):
    screen.blit(table, (0, 0))
    print_arrows(game, screen)
    print_cpu_hands(game, screen)
    print_top_card(game, screen)
    print_player_hand(game, screen)
    print_names(game, screen)
    draw_uno(screen)


if __name__ == '__main__':
    game_engine()
