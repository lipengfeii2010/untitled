import pygame
import sys
from rocket import Rocket


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption('Rocket Fire!!!')
    bg_color = (66, 106, 175)
    screen.fill(bg_color)

    rocket = Rocket(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    rocket.moving_up = True
                elif event.key == pygame.K_DOWN:
                    rocket.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    rocket.moving_up = False
                elif event.key == pygame.K_DOWN:
                    rocket.moving_down = False

        rocket.update()
        rocket.blitme()
        pygame.display.flip()

run_game()