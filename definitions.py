import os

import pygame

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCES_DIR = os.path.join(ROOT_DIR, 'resources')
MAPS_DIR = os.path.join(RESOURCES_DIR, 'maps')
TMX_DIR = os.path.join(MAPS_DIR, 'tmx')
SPRITES_DIR = os.path.join(RESOURCES_DIR, 'sprites')
FOODS_DIR = os.path.join(SPRITES_DIR, 'food')
BODY_DIR = os.path.join(SPRITES_DIR, 'body')
POWERUPS_DIR = os.path.join(SPRITES_DIR, 'powerup')

PX = 32
L = 20

# factor that multiplies the fps while playing
SNAKE_SPEED = 1

# pygame event for power-up creation
CREATE_PWUP = pygame.event.custom_type()
# pygame event to stop power-up effect
STOP_EFFECT = pygame.event.custom_type()

# available power-ups
PWUP_DICT = {
    'Accelerate': 0,
    'Reverse': 1
}

background_color = pygame.Color(33, 33, 33)
credits_color = pygame.Color(245, 245, 245)
