import pygame
import sys

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    bg_color = (255, 255, 255)
    pygame.display.set_caption('Check Event')
    screen.fill(bg_color)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print(event.key)

        pygame.display.flip()

run_game()