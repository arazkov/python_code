import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.image = pygame.image.load('/home/ara/python/game/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.ai_settings = ai_settings
        self.center = float(self.rect.centerx)

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.center < 1160:
            self.center += self.ai_settings.ship_speed_factor
            # return self.center
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center
