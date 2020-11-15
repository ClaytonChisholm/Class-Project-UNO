import pygame
import sys
from game import *

# def main():
#     pygame.init()
#     # screen size, creating screen
#     screen = pygame.display.set_mode((1200, 800))
#     pygame.display.set_caption('Uno')
#
#     background = pygame.Surface(screen.get_size())
#     background = background.convert()
#     background.fill((0, 220, 30))
#
#     font = pygame.font.Font(None, 36)
#     text = font.render("Hey look its uno", True, (10, 10, 10))
#     textpos = text.get_rect()
#     textpos.centerx = background.get_rect().centerx
#     textpos.centery = background.get_rect().centery
#     background.blit(text, textpos)
#
#     # blue 0 rectangle object
#     blue0 = pygame.image.load('cards/blue_0.png')
#     blue0_rect = blue0.get_rect()
#
#     blue1 = pygame.image.load('cards/blue_1.png')
#
#     # allows the screen to run, and allows you to quit
#     while 1:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#         # Blit everything to the screen
#         screen.blit(background, (0, 0))
#
#         # red rectangle
#         red = (250, 0, 0)
#         pygame.draw.rect(screen, red, [75, 10, 50, 20])
#
#         # blit blue0
#         screen.blit(blue0, (500, 500))
#         screen.blit(blue1, (70, 0))
#
#         pygame.display.flip()
#
#         screen.blit(blue0, blue0_rect)
#         blue0_rect.inflate_ip(1, 1)
#         blue0 = pygame.transform.scale(blue0, blue0_rect.size)
#
#         screen.blit(blue0, blue0_rect)
#         pygame.display.flip()
#         sleep(.5)
white = (255, 255, 255)

white = (255, 255, 255)
list_of_rect_card = []


def game_engine():
    pygame.init()
    screen_size = (1200, 800)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('UNO!')
    background = pygame.Surface(screen.get_size())
    black = [255, 0, 0]
    screen.fill(black)
    background = background.convert()

    # light shade of the button
    button_hover_color = (170, 170, 170)

    # dark shade of the button
    button_color = (100, 100, 100)

    # defining a font
    tinyfont = pygame.font.SysFont('Corbel', 25)
    smallfont = pygame.font.SysFont('Corbel', 35)

    # rendering a text written in
    # this font
    text_quit = smallfont.render('Quit', True, white)
    text_new_game = tinyfont.render('New Game', True, white)
    text_rules = smallfont.render('Rules', True, white)

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
        text_back = tinyfont.render('Back To Menu', True, black)
        rules_text = display_rules()
        format_rules(screen, rules_text, tinyfont)
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
        screen = pygame.display.set_mode(screen_size)
        screen.fill((0, 0, 0))
        cpu1 = CPU("Mark", 1)
        cpu2 = CPU("Mira", 2)
        cpu3 = CPU("Julia", 3)
        player = Player('', 0)
        game = Game(cpu1, cpu2, cpu3, player)
        for player in game.players:  # creates starting hands
            game.fill_hand(player)
        print_top_card(game, screen)
        # print_player_hand(game, screen)

        while not game_over:  # game engine
            player = game.players[game.current_player]
            print_player_hand(game, screen)
            print_cpu_hands(game, screen)
            mouse = pygame.mouse.get_pos()
            width = screen.get_width()
            height = screen.get_height()

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # if type(player) == Player:
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                    for card in list_of_rect_card:
                        if card.collidepoint(ev.pos):
                            print("It's clicked")
                        # else:
                        # print("not clicked")

            pygame.display.update()


#
# def print_cpu_hands(game, screen):
#     pass
#
# def print_player_hand(game, screen: pygame.Surface):
#     player = game.player
#     player_hand_size = screen.get_width() * (2 / 3)  # 1/6
#     hand_size = len(player.get_hand())
#     card_size = (player_hand_size - 60) / hand_size  # the 90 here is how far from the end of the hand object
#     hand_height = screen.get_height() - 200
#     hand_start = screen.get_width() * (1 / 6)
#     pygame.draw.rect(screen, white, [hand_start, hand_height, screen.get_width() * 2 / 3, 200])
#     # if card_size * hand_size < player_hand_size - 60:
#     #     card_size = 120  # default size
#
#     if hand_size <= 6:
#
#         card_offset = hand_start + 30 + (.5 * (hand_size - 6) * 120)
#         for card in player.get_hand():
#             card_face = pygame.image.load(card.get_path())
#             card_face = pygame.transform.scale(card_face, (100, 140))
#             card_rect = card_face.get_rect()
#             # transforms to default size
#             card_rect.y = hand_height + 30
#             card_rect.x = card_offset
#             screen.blit(card_face, card_rect)
#             list_of_rect_card.append(card_rect)
#             #card.set_x_coord(card_offset)
#             #card.set_y_coord(hand_height + 30)
#             card_offset += 120  # card size plus space between cards
#
#     else:
#         card_offset = hand_start + 30
#         max_size = screen.get_width() * 2 / 3 - 60
#         hand_width = 120 * hand_size
#         overlap = 0
#         while max_size < hand_width:
#             overlap += 1
#             hand_width = (120 - overlap) * hand_size
#
#         # card_offset = card_offset + (screen.get_width() * 2/3 - (hand_width + 45)) / 2 TODO fix this to look
#         #  pretty
#
#         for card in player.get_hand():
#             card_face = pygame.image.load(card.get_path())
#             card_face = pygame.transform.scale(card_face, (100, 140))  # transforms to default size
#             card_rect = card_face.get_rect()
#             card_rect.y = hand_height + 30
#             card_rect.x = card_offset
#             screen.blit(card_face, card_rect)
#             list_of_rect_card.append(card_rect)
#             #all_sprites_list.add(card_rect)
#             #screen.blit(card_face, (card_offset, hand_height + 30))
#             #card.set_x_coord(card_offset)
#             #card.set_y_coord(hand_height + 30)
#             card_offset += 120 - overlap

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
    textpos = text.get_rect()
    textpos.x = x
    textpos.y = y
    screen.blit(text, textpos)
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


def print_player_hand(game, screen: pygame.Surface):
    player = game.player
    hand_size = len(player.get_hand())
    hand_height = screen.get_height() - 200
    hand_start = screen.get_width() * (1 / 6)
    pygame.draw.rect(screen, white, [hand_start, hand_height, screen.get_width() * 2 / 3, 200])
    # if card_size * hand_size < player_hand_size - 60:
    #     card_size = 120  # default size

    if hand_size <= 6:

        card_offset = hand_start + 30 + (.5 * (hand_size - 6) * 120)
        for card in player.get_hand():
            card_face = pygame.image.load(card.get_path())
            card_face = pygame.transform.scale(card_face, (100, 140))  # transforms to default size
            screen.blit(card_face, (card_offset, hand_height + 30))
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
            screen.blit(card_face, (card_offset, hand_height + 30))
            card_offset += 120 - overlap


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


if __name__ == '__main__':
    game_engine()
