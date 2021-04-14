import os
from abc import ABC

import pygame
from pytmx import load_pygame

from pygame.locals import *

from components.Snake import Snake
from components.Food import Food
from components.Map import Map
from definitions import MAPS_DIR
from game_state_machine.GameState import GameState


class Playing(GameState, ABC):
    def __init__(self, next_state):
        super().__init__(next_state)
        self.paused = False

    def get_map(self, map_name):
        tmxpath = os.path.join(MAPS_DIR, 'tmx', map_name + '.tmx')
        tmxdata = load_pygame(tmxpath)
        self.map = Map(map_name, tmxdata)

    def startup(self):
        if self.paused:  # came from Paused state
            return
        self.snake = Snake()
        self.food = Food()
        self.update_score()

    def cleanup(self):
        if self.paused:  # called by Paused state
            return
        del self.snake
        del self.food

    def update(self):
        collided = self.snake.move()
        if collided:
            self.on_collision()
            return

        if self.snake.get_head_position() == self.food.position:
            self.snake.length += 1
            self.food.randomize_position(self.snake.body)

        self.update_score()

    def update_score(self):
        score = self.snake.length - 1
        score_text = "Score: {}".format(score)
        f = self.fonts['h2']
        self.score_surf = f.render(score_text, True, pygame.Color("yellow"))
        self.score_rect = self.score_surf.get_rect(left=self.get_screen_rect().left)
        self.score_rect.move_ip(10, 10)

    def draw(self, surface):
        self.map.draw(surface)
        self.snake.draw(surface)
        self.food.draw(surface)
        surface.blit(self.score_surf, self.score_rect)

    def on_key_up(self, e):
        d = {
            K_LEFT: self.snake.left,
            K_RIGHT: self.snake.right,
            K_UP: self.snake.up,
            K_DOWN: self.snake.down,
        }
        if e.key in d:
            self.snake.turn(d[e.key])
        elif e.key in [K_ESCAPE, K_p]:
            self.next_state = "Paused"
            self.paused = True
            self.done = True

    def on_mouse_up(self, e):
        pass

    def on_collision(self):
        self.done = True


class PlayingFeijao(Playing):
    def __init__(self, next_state=None):
        super().__init__(next_state)
        self.get_map(map_name='feijao')


class PlayingHall(Playing):
    def __init__(self, next_state=None):
        super().__init__(next_state)
        self.get_map(map_name='hall')


class PlayingQuadra(Playing):
    def __init__(self, next_state=None):
        super().__init__(next_state)
        self.get_map(map_name='quadra')


class PlayingApart(Playing):
    def __init__(self, next_state=None):
        super().__init__(next_state)
        self.get_map(map_name='apart')
