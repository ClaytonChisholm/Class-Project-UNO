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
    background = background.convert()
    background.fill((0, 0, 0))

    # white color
    white = (255, 255, 255)

    # light shade of the button
    color_light = (170, 170, 170)

    # dark shade of the button
    color_dark = (100, 100, 100)

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
            pygame.draw.rect(screen, color_light, [new_game_button_x, button_y, 140, 40])
        else:
            pygame.draw.rect(screen, color_dark, [new_game_button_x, button_y, 140, 40])

        if quit_button_x <= mouse[0] <= quit_button_x+button_width and button_y <= mouse[1] <= button_y+button_height:
            pygame.draw.rect(screen, color_light, [quit_button_x, button_y, 140, 40])
        else:
            pygame.draw.rect(screen, color_dark, [quit_button_x, button_y, 140, 40])

        if rules_button_x <= mouse[0] <= rules_button_x+button_width and button_y <= mouse[1] <= button_y+button_height:
            pygame.draw.rect(screen, color_light, [rules_button_x, button_y, 140, 40])
        else:
            pygame.draw.rect(screen, color_dark, [rules_button_x, button_y, 140, 40])

        # superimposing the text onto our buttons
        screen.blit(text_quit, (quit_button_x + 40, button_y+3))
        screen.blit(text_new_game, (new_game_button_x+15, button_y+7))
        screen.blit(text_rules, (rules_button_x+30, button_y+3))

        # updates the frames of the game
        pygame.display.update()

        if show_rules or not game_over:
            show_menu = False

    # if show_rules:
       # while:

    # if not game_over:
       # while:


        # cpu1 = CPU("Mark", 1)
        # cpu2 = CPU("Mira", 2)
        # cpu3 = CPU("Julia", 3)
        # player = Player('', 0)
        # game = Game(cpu1, cpu2, cpu3, player)
        # game_over = False

    # TODO get name input
    # name = ''
    # player.set_name(name)


if __name__ == '__main__':
    game_engine()
