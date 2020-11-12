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


def game_engine():

    pygame.init()
    screen_size = (1200, 800)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('UNO!')
    background = pygame.Surface(screen.get_size())
    black = [255, 0, 0]
    screen.fill(black)
    background = background.convert()

    # white color
    white = (255, 255, 255)

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
        new_game_button_x = (width*.5)-(button_width/2)
        quit_button_x = (width*.75)-(button_width/2)
        rules_button_x = (width*.25)-(button_width/2)
        button_y = (height*.75)+(button_height/2)

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

                # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                # if the mouse is clicked on the
                # button the game is terminated
                if quit_button_x <= mouse[0] <= quit_button_x+button_width and button_y <= mouse[1] <= button_y+button_height:
                    pygame.quit()
                    sys.exit()

                if new_game_button_x <= mouse[0] <= new_game_button_x+button_width and button_y <= mouse[1] <= button_y+button_height:
                    game_over = False

                if rules_button_x <= mouse[0] <= rules_button_x+button_width and button_y <= mouse[1] <= button_y+button_height:
                    show_rules = True

        if new_game_button_x <= mouse[0] <= new_game_button_x+button_width and button_y <= mouse[1] <= button_y+button_height:
            pygame.draw.rect(screen, button_hover_color, [new_game_button_x, button_y, 140, 40])
        else:
            pygame.draw.rect(screen, button_color, [new_game_button_x, button_y, 140, 40])

        if quit_button_x <= mouse[0] <= quit_button_x+button_width and button_y <= mouse[1] <= button_y+button_height:
            pygame.draw.rect(screen, button_hover_color, [quit_button_x, button_y, 140, 40])
        else:
            pygame.draw.rect(screen, button_color, [quit_button_x, button_y, 140, 40])

        if rules_button_x <= mouse[0] <= rules_button_x+button_width and button_y <= mouse[1] <= button_y+button_height:
            pygame.draw.rect(screen, button_hover_color, [rules_button_x, button_y, 140, 40])
        else:
            pygame.draw.rect(screen, button_color, [rules_button_x, button_y, 140, 40])

        # superimposing the text onto our buttons
        screen.blit(text_quit, (quit_button_x + 40, button_y+3))
        screen.blit(text_new_game, (new_game_button_x+15, button_y+7))
        screen.blit(text_rules, (rules_button_x+30, button_y+3))

        # updates the frames of the game
        pygame.display.update()

        if show_rules or not game_over:
            show_menu = False

    # show rules screen
    if show_rules:
        screen = pygame.display.set_mode(screen_size)
        while show_rules:
            mouse = pygame.mouse.get_pos()
            width = screen.get_width()
            height = screen.get_height()

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    # game screen
    if not game_over:
        screen = pygame.display.set_mode(screen_size)
        #screen.fill(red)
        cpu1 = CPU("Mark", 1)
        cpu2 = CPU("Mira", 2)
        cpu3 = CPU("Julia", 3)
        player = Player('', 0)
        game = Game(cpu1, cpu2, cpu3, player)
        for player in game.players:  # creates starting hands
            game.fill_hand(player)
        print_top_card(game, screen)

        while not game_over:
            mouse = pygame.mouse.get_pos()
            width = screen.get_width()
            height = screen.get_height()

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


def print_top_card(game, screen):
    top_card = print_card(game.last_played)
    deck_cover = pygame.image.load('cards/card_back.png')
    deck_cover = pygame.transform.scale(deck_cover, (100, 140))
    screen.blit(top_card, (((screen.get_width()/2)-120), (screen.get_height()/2)-100))
    screen.blit(deck_cover, (((screen.get_width() / 2) + 20), (screen.get_height() / 2) - 100))
    pygame.display.flip()

#def print_player_hand(game, screen):
    #stuff

#def print_cpu_hands(game, screen):
    #


def print_card(card):
    graphics_card = pygame.image.load(card.get_path())
    graphics_card = pygame.transform.scale(graphics_card, (100, 140))
    return graphics_card


if __name__ == '__main__':
    game_engine()
