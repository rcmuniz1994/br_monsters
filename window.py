import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from heroes import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
                (ai_settings.screen_width,
                 ai_settings.screen_height))
    pygame.display.set_caption("BR Monsters")
    ship = Ship(ai_settings, screen)
    bullets = Group()

    while True:   
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
