#!/usr/bin/python3

import pygame
from settings import Settings
from ship import Ship
from game_function import check_events, update_screen

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invation')
    # bg_color = ai_settings.bg_color
    ship = Ship(ai_settings, screen)

    while True:
        check_events(ship)
        ship.update()
        # print(ship.center)
        update_screen(ai_settings, screen, ship)

run_game()
