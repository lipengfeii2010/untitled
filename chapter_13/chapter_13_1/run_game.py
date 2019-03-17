import sys
import pygame
from star import Star
from pygame.sprite import Group


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Star')
    bg_color = (246, 246, 246)

    stars = Group()
    star = Star(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        for i in range(3):
            for j in range(star.x_num):
                new_star = Star(screen)
                new_star.rect.x += new_star.rect.width
                stars.add(new_star)
                new_star.blitme()


        pygame.display.flip()
        print(star.x_num)

run_game()
