import random

import pygame

from definitions import L, PX
from components.Spritesheet import Spritesheet


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.board_width = self.board_height = L
        self.randomize_position()
        self.spritesheet = Spritesheet('Character', 4)

    def randomize_position(self, snake_body=None):
        if snake_body is None:
            snake_body = []
        # item position can't override snake's body
        while True:
            self.position = (
                random.randint(0, self.board_width - 1), random.randint(0, self.board_height - 1)
            )
            if self.position not in snake_body:
                return

    def draw(self, surface: pygame.Surface):
        sprite = self.get_sprite()
        pos = tuple((x * PX) for x in self.position)
        surface.blit(sprite, pos)

    def get_sprite(self):
        sprite = self.spritesheet.parse_sprite('down')
        return sprite
