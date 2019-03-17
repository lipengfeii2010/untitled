import pygame
from pygame.sprite import Sprite


class Star(Sprite):

    def __init__(self, screen):
        super(Star, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load('images/star.jpg')
        self.rect = self.image.get_rect()

        self.rect.x = self.screen_rect.x
        self.rect.y = self.screen_rect.y

        # 计算每行放多少个星星
        self.x_num = int(self.screen_rect.width / self.rect.width)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

