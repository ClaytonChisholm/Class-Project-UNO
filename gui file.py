import pygame
import sys



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
        pygame.display.flip()

if __name__ == '__main__':
    main()