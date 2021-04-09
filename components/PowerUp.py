import random
import os

import pygame

from definitions import L, PX, POWERUPS_DIR, STOP_EFFECT, SNAKE_SPEED


class PowerUp:
    def __init__(self, dic):
        self.position = (0, 0)
        self.board_width = self.board_height = L
        self.randomize_position()
        self.sprite_counter = 0
        # key to define power-up effect
        self.effect_key = dic['key']
        self.lasting = dic['lasting']
        if self.lasting:
            self.duration = dic['interval']

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
        if self.sprite_counter > 1:
            self.sprite_counter = 0

        sprite = self.get_sprite()
        pos = tuple((x * PX) for x in self.position)
        surface.blit(sprite, pos)

        self.sprite_counter += 1

    def get_sprite(self):
        filename = 'pup{}{}.png'.format(self.effect_key, self.sprite_counter)
        sprite = pygame.image.load(os.path.join(POWERUPS_DIR, filename)).convert_alpha()
        return sprite

    def get_effect(self, snake):
        """
        Method to cause the corresponding effect on the snake
        """
        if self.effect_key == 0:
            # increases snake speed by a factor of 2
            snake.speed = 2*SNAKE_SPEED
            pygame.time.set_timer(STOP_EFFECT, self.duration, 1)
        elif self.effect_key == 1:
            # reverses the snake
            tmp = []
            for i, d in enumerate(snake.directions):
                if d == snake.up:
                    tmp.insert(0, snake.down)
                elif d == snake.left:
                    tmp.insert(0, snake.right)
                elif d == snake.right:
                    tmp.insert(0, snake.left)
                elif d == snake.down:
                    tmp.insert(0, snake.up)
            snake.directions = tmp
            snake.head_direction = tmp[0]
            snake.body.reverse()

    def reset_effect(self, snake):
        if self.effect_key == 0:
            snake.speed = SNAKE_SPEED
