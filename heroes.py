import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """
        Inicializa a nave
        """

        self.screen = screen

        self.image = pygame.image.load("pictures/ship.bmp")
        self.rect = self.image.get_rect()

        self.screen_rect = screen.get_rect()

        self.center = float(self.screen_rect.centerx)
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.ship_speed_factor = 1.5

    def blitme(self):
        """
        Desenha a nave na posição atual
        """

        self.screen.blit(self.image, self.rect)

    def update(self):
        """
        Atualiza a posição da nave de acordo com flag
        """

        # Verifica se a borda direita do retangulo
        # chegou na borda direita da janela
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ship_speed_factor

        # Verifica se a borda esquerda do retangulo
        # chegou na borda esquerda da janela        
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ship_speed_factor

        self.rect.centerx = self.center
