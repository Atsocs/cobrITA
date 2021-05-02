import random

import pygame

from components.Spritesheet import Spritesheet
from definitions import L, PX, UPDATE_CONST


class Food:
    def __init__(self, prohibited=None):
        self.position = (0, 0)
        self.board_width = self.board_height = L
        self.randomize_position(prohibited)

        self.sprite_counter = 0
        self.num_sprites = 4
        self.spritesheet = Spritesheet('Character')

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
        if self.sprite_counter >= self.num_sprites*UPDATE_CONST:
            self.sprite_counter = 0

        sprite = self.get_sprite()
        pos = tuple((x * PX) for x in self.position)
        surface.blit(sprite, pos)

        self.sprite_counter += 1

    def get_sprite(self):
        frame_name = 'down_{}'.format(self.sprite_counter//UPDATE_CONST)
        sprite = self.spritesheet.parse_sprite(frame_name)
        return sprite
