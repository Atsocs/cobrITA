import os

import pygame

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCES_DIR = os.path.join(ROOT_DIR, 'resources')
MAPS_DIR = os.path.join(RESOURCES_DIR, 'maps')
TMX_DIR = os.path.join(MAPS_DIR, 'tmx')
SPRITES_DIR = os.path.join(RESOURCES_DIR, 'sprites')
SOUND_DIR = os.path.join(RESOURCES_DIR, "sound")
POWERUPS_DIR = os.path.join(SPRITES_DIR, 'powerup')

PX = 32
L = 16

# don't know how to define this!!!
UPDATE_CONST = 15

# pygame event for power-up creation
CREATE_PWUP = pygame.event.custom_type()
# pygame event to stop power-up effect
STOP_EFFECT = pygame.event.custom_type()

# available power-ups
PWUP_DICT = {
    'Accelerate': {'key': 0, 'lasting': True, 'interval': 3000},
    'Reverse': {'key': 1, 'lasting': False}
}

GRADES = {
    'XLL': 1.10,  # by Prof. Alonso
    'XL': 1.00,  # by Prof. Alonso
    'L': 0.95,
    'MB': 0.85,
    'B': 0.75,
    'R': 0.65,
    'I': 0.5,
    'D': 0.0
}

background_color = pygame.Color(33, 33, 33)
credits_color = pygame.Color(245, 245, 245)
achiev_color = pygame.Color(246, 246, 246)
