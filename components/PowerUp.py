#
# WARNING: SPRITES MUST BE UPDATED!!!
#

import random
import os

import pygame

from definitions import L, PX, POWERUPS_DIR, STOP_EFFECT, UPDATE_CONST


class PowerUp:
    def __init__(self, **kwargs):
        self.board_width = self.board_height = L
        self.randomize_position()
        self.sprite_counter = 0
        # key to define power-up effect
        self.effect_key = kwargs['key']
        self.lasting = kwargs['lasting']
        if self.lasting:
            self.duration = kwargs['interval']

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
        if self.sprite_counter >= 2*UPDATE_CONST:
            self.sprite_counter = 0

        sprite = self.get_sprite()
        pos = tuple((x * PX) for x in self.position)
        surface.blit(sprite, pos)

        self.sprite_counter += 1

    def get_sprite(self):
        filename = 'pup{}{}.png'.format(self.effect_key, (1 if self.sprite_counter >= UPDATE_CONST else 0))
        sprite = pygame.image.load(os.path.join(POWERUPS_DIR, filename)).convert_alpha()
        return sprite

    def get_effect(self, snake):
        """
        Method to cause the corresponding effect on the snake
        """
        if self.effect_key == 0:
            # increases snake speed by a factor of 2
            snake.update_counter = UPDATE_CONST//2
            pygame.time.set_timer(STOP_EFFECT, self.duration, True)
        elif self.effect_key == 1:
            snake.reverse()

    def reset_effect(self, snake):
        if self.effect_key == 0:
            snake.update_counter = UPDATE_CONST
