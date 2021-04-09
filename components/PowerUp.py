import random
import os

import pygame

from definitions import L, PX, POWERUPS_DIR, STOP_EFFECT, SNAKE_SPEED


class PowerUp:
    def __init__(self, effect_key):
        self.position = (0, 0)
        self.board_width = self.board_height = L
        self.randomize_position()
        self.sprite_counter = 0
        # key to define power-up effect
        self.effect = effect_key

    def randomize_position(self, snake_body=None):
        if snake_body is None:
            snake_body = []
        while True:
            self.position = (
                random.randint(0, self.board_width - 1), random.randint(0, self.board_height - 1)
            )
            # item position can't override snake's body
            if self.position not in snake_body:
                return

    def draw(self, surface: pygame.Surface):
        if self.sprite_counter > 1:
            self.sprite_counter = 0

        sprite = self.get_sprite()
        pos = tuple((x * PX) for x in self.position)
        surface.blit(sprite, pos)

        self.sprite_counter += 1

    def get_sprite(self):
        filename = 'pup{}{}.png'.format(self.effect, self.sprite_counter)
        sprite = pygame.image.load(os.path.join(POWERUPS_DIR, filename)).convert_alpha()
        return sprite

    def get_effect(self, snake):
        """
        Method to cause the corresponding effect on the snake
        """
        if self.effect == 0:
            # increases snake speed by a factor of 2
            snake.speed = 2*SNAKE_SPEED
            interval = 3000
            pygame.time.set_timer(STOP_EFFECT, interval)
        elif self.effect == 1:
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
        if self.effect == 0:
            snake.speed = SNAKE_SPEED
