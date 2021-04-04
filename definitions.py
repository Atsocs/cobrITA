import os

import pygame

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCES_DIR = os.path.join(ROOT_DIR, 'resources')
MAPS_DIR = os.path.join(RESOURCES_DIR, 'maps')
TMX_DIR = os.path.join(MAPS_DIR, 'tmx')

PX = 32
L = 20

background_color = pygame.Color(33, 33, 33)
credits_color = pygame.Color(245, 245, 245)
