import random
import os

import pygame

from definitions import L, PX


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.board_width = self.board_height = L
        self.randomize_position()
        self.sprite_path = os.path.join(os.getcwd(), 'resources', 'sprites', 'food')  # fixme
        self.sprite_counter = 0

    def randomize_position(self, snake_body=None):
        if snake_body is None:
            snake_body = []
        # item position can't override snake's body
        while True:
            self.position = (
                random.randint(0, self.board_width - 1), random.randint(0, self.board_height - 1)
            )
            if self.position not in snake_body:
                print(self.position)
                return

    def draw(self, surface: pygame.Surface):
        if self.sprite_counter > 1:
            self.sprite_counter = 0

        sprite = self.get_sprite()
        pos = tuple((x * PX) for x in self.position)
        surface.blit(sprite, pos)

        self.sprite_counter += 1

    def get_sprite(self):
        sprite = pygame.image.load(
            os.path.join(
                self.sprite_path, 'acai' + str(self.sprite_counter) + '.png'
            )
        )
        sprite = sprite.convert_alpha()
        return sprite
