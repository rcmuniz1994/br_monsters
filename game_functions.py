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
