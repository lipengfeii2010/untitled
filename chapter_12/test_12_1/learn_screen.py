import pygame
import sys
from butterfly import Butterfly

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    bg_color = (255, 255, 255)
    pygame.display.set_caption("Learn Screen")

    butterfly = Butterfly(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        butterfly.blitme()
        pygame.display.flip()

run_game()
