import pygame


class Ship():

    def __init__(self, screen):
        """
        Inicializa a nave
        """

        self.screen = screen

        self.image = pygame.image.load("pictures/ship.bmp")
        self.rect = self.image.get_rect()

        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """
        Desenha a nave na posição atual
        """

        self.screen.blit(self.image, self.rect)

    def update(self):
        """
        Atualiza a posição da nave de acordo com flag
        """
        if self.moving_right:
            self.rect.centerx += 1
        elif self.moving_left:
            self.rect.centerx -= 1
