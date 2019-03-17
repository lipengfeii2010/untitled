import pygame


class Rocket():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/rocket.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 让火箭居中
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # 持续移动标识
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_left == True and self.rect.x > 0:
            self.rect.centerx -= 1
        elif self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        elif self.moving_up == True and self.rect.top > 0:
            self.rect.centery -= 1
        elif self.moving_down == True and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1

