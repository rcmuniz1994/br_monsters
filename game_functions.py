import sys

import pygame

def check_events():
    """
    Responde à ações de mouse ou teclas realizadas
    pelos usuários.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    # Redesenhando a tela a cada iteração
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Deixa a tela mais recente visível
    pygame.display.flip()
