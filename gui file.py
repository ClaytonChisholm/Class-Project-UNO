import pygame
import sys
from time import sleep



def main():
    pygame.init()
    # screen size, creating screen
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Uno')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 220, 30))

    font = pygame.font.Font(None, 36)
    text = font.render("Hey look its uno", True, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    background.blit(text, textpos)

    # blue 0 rectangle object
    blue0 = pygame.image.load('cards/blue_0.png')
    blue0_rect = blue0.get_rect()

    blue1 = pygame.image.load('cards/blue_1.png')


    # allows the screen to run, and allows you to quit
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Blit everything to the screen
        screen.blit(background, (0, 0))

        # red rectangle
        red = (250, 0, 0)
        pygame.draw.rect(screen, red, [75, 10, 50, 20])

        # blit blue0
        screen.blit(blue0, (500, 500))
        screen.blit(blue1, (70, 0))

        pygame.display.flip()


        screen.blit(blue0, blue0_rect)
        blue0_rect.inflate_ip(1, 1)
        blue0 = pygame.transform.scale(blue0, blue0_rect.size)

        screen.blit(blue0, blue0_rect)
        pygame.display.flip()
        sleep(.5)

if __name__ == '__main__':
    main()