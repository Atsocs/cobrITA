import random
import os

import pygame

from definitions import L, PX, FOODS_DIR


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.board_width = self.board_height = L
        self.randomize_position()
        self.sprite_counter = 0

    def randomize_position(self, prohibited=None):
        if prohibited is None:
            prohibited = []
        # item position can't override snake's body
        while True:
            self.position = (
                random.randint(0, self.board_width - 1), random.randint(0, self.board_height - 1)
            )
            if self.position not in prohibited:
                return

    def draw(self, surface: pygame.Surface):
        if self.sprite_counter > 1:
            self.sprite_counter = 0

        sprite = self.get_sprite()
        pos = tuple((x * PX) for x in self.position)
        surface.blit(sprite, pos)

        self.sprite_counter += 1

    def get_sprite(self):
        filename = 'acai{}.png'.format(self.sprite_counter)
        sprite = pygame.image.load(os.path.join(FOODS_DIR, filename)).convert_alpha()
        return sprite
