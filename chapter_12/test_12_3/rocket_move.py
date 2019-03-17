import pygame
import sys
from rocket import Rocket

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption('Rocket Move')
    bg_color = (66, 106, 175)

    rocket = Rocket(screen)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # 按左键
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rocket.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    rocket.moving_right = True
                elif event.key == pygame.K_UP:
                    rocket.moving_up = True
                elif event.key == pygame.K_DOWN:
                    rocket.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    rocket.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    rocket.moving_right = False
                elif event.key == pygame.K_UP:
                    rocket.moving_up = False
                elif event.key == pygame.K_DOWN:
                    rocket.moving_down = False
            '''
            

            # 按右键
            if event.type == pygame.K_RIGHT:
            # 按上键
            if event.type == pygame.K_UP:
            # 按下键
            if event.type == pygame.K_DOWN:
            '''
        screen.fill(bg_color)
        rocket.update()
        rocket.blitme()
        pygame.display.flip()

run_game()



