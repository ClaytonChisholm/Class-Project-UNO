import pygame
import sys
from game import *
import pygame_textinput

white = (255, 255, 255)
list_of_rect_card = []
red = (245, 100, 98)
blue = (0, 195, 229)
green = (47, 226, 155)
yellow = (247, 227, 89)
black = [0, 0, 0]
# light shade of the button
button_hover_color = (170, 170, 170)

# dark shade of the button
button_color = (100, 100, 100)


def game_engine():
    pygame.init()
    screen_size = (1200, 800)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('UNO!')
    screen.fill(black)

    # defining a font
    tiny_font = pygame.font.SysFont('Corbel', 25)
    small_font = pygame.font.SysFont('Corbel', 35)

    # rendering a text written in
    # this font
    text_quit = small_font.render('Quit', True, white)
    text_new_game = tiny_font.render('New Game', True, white)
    text_rules = small_font.render('Rules', True, white)

    game_over = True
    show_menu = True
    show_rules = False

    # menu screen

    while show_menu:
        # stores the (x,y) coordinates into
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

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

                # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                # if the mouse is clicked on the
                # button the game is terminated
                if quit_button_x <= mouse[0] <= quit_button_x + button_width and button_y <= mouse[
                        1] <= button_y + button_height:
                    pygame.quit()
                    sys.exit()

                if new_game_button_x <= mouse[0] <= new_game_button_x + button_width and button_y <= mouse[
                        1] <= button_y + button_height:
                    game_over = False

                if rules_button_x <= mouse[0] <= rules_button_x + button_width and button_y <= mouse[
                        1] <= button_y + button_height:
                    show_rules = True

        if new_game_button_x <= mouse[0] <= new_game_button_x + button_width and button_y <= mouse[
                1] <= button_y + button_height:
            pygame.draw.rect(screen, button_hover_color, [new_game_button_x, button_y, 140, 40])
        else:
            pygame.draw.rect(screen, button_color, [new_game_button_x, button_y, 140, 40])

        if quit_button_x <= mouse[0] <= quit_button_x + button_width and button_y <= mouse[
                1] <= button_y + button_height:
            pygame.draw.rect(screen, button_hover_color, [quit_button_x, button_y, 140, 40])
        else:
            pygame.draw.rect(screen, button_color, [quit_button_x, button_y, 140, 40])

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
        screen = pygame.display.set_mode(screen_size)
        screen.fill(white)
        text_back = tiny_font.render('Back To Menu', True, black)
        rules_text = display_rules()
        format_rules(screen, rules_text, tiny_font)
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

    # game screen
    if not game_over:

        text_input = pygame_textinput.TextInput('enter your name')
        text = True
        while text:
            screen.fill((225, 225, 225))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    text = False
            # Feed it with events every frame
            text_input.update(events)
            # Blit its surface onto the screen
            screen.blit(text_input.get_surface(), (screen.get_width() / 2, screen.get_height() / 2))
            pygame.display.update()

        screen = pygame.display.set_mode(screen_size)
        screen.fill((0, 0, 0))
        cpu1 = CPU("Mark", 1)
        cpu2 = CPU("Mira", 2)
        cpu3 = CPU("Julia", 3)
        name = text_input
        player = Player(name, 0)
        game = Game(cpu1, cpu2, cpu3, player)
        for player in game.players:  # creates starting hands
            game.fill_hand(player)
        screen = pygame.display.set_mode(screen_size)
        screen.fill((0, 0, 0))
        print_top_card(game, screen)

        while not game_over:  # game engine
            player = game.players[game.current_player]
            print_player_hand(game, screen)
            print_top_card(game, screen)
            print_cpu_hands(game, screen)
            pygame.display.update()
            picked_card = choose_card(screen, game)
            if not picked_card:
                pass
            elif type(picked_card) == Card:  # handles changing the game variables when a card is played
                if game.last_played.get_type() == Type.WILD or game.last_played.get_type() == Type.DRAW4:
                    game.last_played.set_wild(Color.NONE)  # resets wilds and draw fours from the previous turn, so
                    # they don't have a color after shuffling
                game.last_played = picked_card  # updates the last played card and adds it to the discard
                game.played_deck.append(game.last_played)

                # handles wilds
                if type(player) == Player and (
                        game.last_played.get_type() == Type.WILD or game.last_played.get_type() == Type.DRAW4):
                    color = set_wild(screen)
                    game.last_played.set_wild(color)
                elif type(player) == CPU and (
                        game.last_played.get_type() == Type.WILD or game.last_played.get_type() == Type.DRAW4):
                    game.last_played.set_wild(player.cpu_wilds())  # sets the color of the wild with cpu choice
            game.apply_power()  # handles all non wild power cards
            if not player.get_hand() or (len(game.played_deck) == 0):
                game_over = True
                print("game over")
                game_engine()
            if type(player) == CPU:
                sleep(1)
            game.change_turn()
            screen = pygame.display.set_mode(screen_size)
            pygame.display.update()


def print_player_hand(game, screen: pygame.Surface):
    list_of_rect_card.clear()
    player = game.player
    hand_size = len(player.get_hand())
    hand_height = screen.get_height() - 200
    hand_start = screen.get_width() * (1 / 6)
    pygame.draw.rect(screen, white, [hand_start, hand_height, screen.get_width() * 2 / 3, 200])

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

        # card_offset = card_offset + (screen.get_width() * 2/3 - (hand_width + 45)) / 2 TODO fix this to look
        #  pretty

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


def format_rules(screen, rules, font):
    new_line = ""
    count = 0
    x = 20
    y = 20
    for word in rules.split():
        if count < 25:
            if word == "include:":
                word_to_append = " " + word
                new_line += word_to_append
                new_line = blit_rules(screen, new_line, font, x, y)
            if word == "Reverse:" or word == "Skip" or word == "Wild" or word == "Draw" or word == "In":
                new_line = blit_rules(screen, new_line, font, x, y)
                word_to_append = " " + word
                new_line += word_to_append
                y += 40
                count = 1
            else:
                word_to_append = " " + word
                new_line += word_to_append
                count += 1
                if count == 25:
                    new_line = blit_rules(screen, new_line, font, x, y)
                    y += 40
                    count = 0


def blit_rules(screen, new_line, font, x, y):
    text = font.render(new_line, True, (10, 10, 10))
    text_pos = text.get_rect()
    text_pos.x = x
    text_pos.y = y
    screen.blit(text, text_pos)
    pygame.display.flip()
    pygame.display.update()
    new_line = ''
    return new_line


def print_top_card(game, screen):
    top_card = print_card(game.last_played)
    deck_cover = pygame.image.load('cards/card_back.png')
    deck_cover = pygame.transform.scale(deck_cover, (100, 140))
    screen.blit(top_card, (((screen.get_width() / 2) - 120), (screen.get_height() / 2) - 100))
    screen.blit(deck_cover, (((screen.get_width() / 2) + 20), (screen.get_height() / 2) - 100))
    pygame.display.flip()


def print_cpu_hands(game, screen):
    cpus = [game.cpu1, game.cpu2, game.cpu3]
    for i in range(len(cpus)):
        cpu = cpus[i - 1]
        hand_size = len(cpu.get_hand())
        if i == 1:  # TODO pygame.transform.rotate(surface, 90)
            pass  # this is if cpu is on left of screen
        elif i == 2:
            pass  # this is if cpu is on top of screen
        else:  # TODO pygame.transform.rotate(surface, 270)
            pass  # if cpu is on right side


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
    deck_rect.y = (screen.get_height() / 2) - 100
    screen.blit(deck_cover, deck_rect)
    user_answer = False
    while user_answer is False and type(game.players[game.current_player]) == Player:
        if type(game.players[game.current_player]) == Player:
            while True:
                for ev in pygame.event.get():
                    if ev.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    # if type(player) == Player:
                    if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:

                        if deck_rect.collidepoint(ev.pos):
                            print('draw card')
                            card = game.draw_card()
                            if game.validate_move(card):
                                # TODO is this the right card shit
                                return card
                            else:
                                current_player.add_card(card)
                                return False

                        for i in range(len(list_of_rect_card)):
                            print(i, " index")
                            print(len(list_of_rect_card), " card length")
                            #if (i)
                            if list_of_rect_card[i].collidepoint(ev.pos):
                                print("It's clicked")
                                print(i)
                                current_player.get_hand()[i].print()
                                rect_position = list_of_rect_card[i]
                                user_answer = confirm_user_card(current_player.get_hand()[i], rect_position, screen)
                                if user_answer:
                                    print_player_hand(game, screen)
                                    print_top_card(game, screen)
                                    if game.validate_move(current_player.get_hand()[i]):
                                        position = list_of_rect_card.pop(i)
                                        pygame.display.update()
                                        card_played = pygame.image.load(current_player.get_hand()[i].get_path())
                                        card_selected = current_player.get_hand().pop(i)
                                        # position = card_played.get_rect()
                                        for x in range(20):
                                            screen.fill(black)
                                            print_player_hand(game, screen)
                                            print_top_card(game, screen)
                                            #pygame.draw.rect(screen, black, [position.x, position.y, position.width, position.height])
                                            position = position.move(0, -10)
                                            screen.blit(card_played, position)
                                            pygame.display.update()
                                            pygame.time.delay(25)
                                        #pygame.display.update()
                                        #position = card_played.get_rect()

                                        #while position.x != (screen.get_width() / 2) - 120:
                                        #for x in range(50):
                                                #if position.x > (screen.get_width() / 2) - 120:
                                                #screen.fill(black)
                                                #print_player_hand(game, screen)
                                                #print_top_card(game, screen)
                                                #pygame.display.update()
                                                #position = position.move(-1, 0)
                                            #elif position.x < (screen.get_width() / 2) - 120:
                                             #   screen.fill(black)
                                              #  print_player_hand(game, screen)
                                               # print_top_card(game, screen)
                                                #pygame.display.update()
                                                #position = position.move(1, 0)
                                            #screen.blit(card_played, position)
                                            #pygame.display.update()
                                            #pygame.time.delay(30)
                                        #position = card_played.get_rect()
                                        #while position.y != (screen.get_height() / 2) - 100:
                                        #for x in range(50):
                                            #screen.fill(black)
                                            #print_player_hand(game, screen)
                                            #print_top_card(game, screen)
                                            #position = position.move(0, -1)
                                            #screen.blit(card_played, position)
                                            #pygame.display.update()
                                            #pygame.time.delay(30)
                                        #postion.x = screen.get_width()/2 - 100
                                        #postion.y = screen.get_height() - 250
                                        #screen.blit(card_played, postion)
                                        screen.fill(black)
                                        print_player_hand(game, screen)
                                        print_top_card(game, screen)
                                        pygame.display.update()
                                        return card_selected
                                    else:
                                        print('invalid')
                                elif user_answer is False:
                                    screen.fill(black)
                                    print_player_hand(game, screen)
                                    print_top_card(game, screen)


                        # else:
                        # print("not clicked")
    # TODO choose cpu
    else:
        if current_player.get_number() == 1:
            card = current_player.play_card(game.player, game.cpu3, game.cpu2, game.last_played)
        elif current_player.get_number() == 2:
            card = current_player.play_card(game.player, game.cpu1, game.cpu3, game.last_played)
        else:
            card = current_player.play_card(game.player, game.cpu1, game.cpu2, game.last_played)
        if not card:
            current_player.add_card(game.draw_card())
            if game.validate_move(current_player.get_hand()[len(current_player.get_hand()) - 1]):
                return current_player.get_hand().pop(len(current_player.get_hand()) - 1)
            else:
                return False  # returns false if no valid card is found
        else:
            return card  # returns card if one is found

def confirm_user_card(card_selected, rectangle, screen):
    screen.fill(black)
    button_height = 100
    button_width = 150
    small_font = pygame.font.SysFont('Corbel', 35)

    pygame.display.update()
    card_played = pygame.image.load(card_selected.get_path())
    rectangle.x = screen.get_width()/2 - 75
    rectangle.y = screen.get_height()/2 - 75
    screen.blit(card_played, rectangle)
    yes_button = pygame.draw.rect(screen, blue, [screen.get_width()/2 - 165, screen.get_height()/2 + 200, button_width, button_height])
    no_button = pygame.draw.rect(screen, red,[screen.get_width()/2 - 165 + 160, screen.get_height()/2 + 200, button_width, button_height])
    yes = small_font.render('Yes',True, black)
    no = small_font.render('No',True, black)
    screen.blit(yes, (screen.get_width()/2 - 100, screen.get_height()/2 + 200))
    screen.blit(no, (screen.get_width()/2 - 100 + 160, screen.get_height()/2 + 200))
    pygame.display.update()

    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                mouse = pygame.mouse.get_pos()
                # if the mouse is clicked on the
                # button the game is terminated
                if yes_button.x <= mouse[0] <= yes_button.x + button_width and yes_button.y <= mouse[
                        1] <= yes_button.y + button_height:
                    return True
                if no_button.x <= mouse[0] <= no_button.x + button_width and no_button.y <= mouse[
                        1] <= no_button.y + button_height:
                    return False

def set_wild(screen):
    screen_size = screen.get_size()
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


if __name__ == '__main__':
    game_engine()
