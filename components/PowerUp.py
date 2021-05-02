#
# WARNING: SPRITES MUST BE UPDATED!!!
#

import random
import os

import pygame

from components.Spritesheet import Spritesheet
from definitions import L, STOP_EFFECT, UPDATE_CONST
from utils import draw_image


class PowerUp:
    def __init__(self, **kwargs):
        self.SPRITE_COUNTER_MAX = 4
        self.board_width = self.board_height = L
        self.randomize_position()
        self.sprite_counter = 0
        # key to define power-up effect
        self.effect_key = kwargs['key']
        self.lasting = kwargs['lasting']
        if self.lasting:
            self.duration = kwargs['interval']
        self.spritesheet = Spritesheet('Powerups')

    def randomize_position(self, prohibited=None):
        if prohibited is None:
            prohibited = []
        while True:
            self.position = (
                random.randint(0, self.board_width - 1), random.randint(0, self.board_height - 1)
            )
            # item position can't override snake's body
            if self.position not in prohibited:
                return

    def draw(self, surface: pygame.Surface):
        sprite = self.get_sprite()
        draw_image(surface, sprite, *self.position)

        self.sprite_counter += 1
        self.sprite_counter %= self.SPRITE_COUNTER_MAX

    def get_sprite(self):
        # fixme: gambi alert
        i = (not self.effect_key) * self.SPRITE_COUNTER_MAX + self.sprite_counter
        filename = f'Powerups{i}.png'
        sprite = self.spritesheet.parse_sprite(filename)
        return sprite

    def get_effect(self, snake):
        """
        Method to cause the corresponding effect on the snake
        """
        if self.effect_key == 0:
            # increases snake speed by a factor of 2
            snake.update_counter = UPDATE_CONST // 2
            pygame.time.set_timer(STOP_EFFECT, self.duration, True)
        elif self.effect_key == 1:
            snake.reverse()

    def reset_effect(self, snake):
        if self.effect_key == 0:
            snake.update_counter = UPDATE_CONST
