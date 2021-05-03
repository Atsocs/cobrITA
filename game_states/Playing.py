import os
from abc import ABC

import pygame
from pytmx import load_pygame

from pygame.locals import *

from components.Snake import Snake
from components.Food import Food
from components.Map import Map
from components.PowerUpFactory import PowerUpFactory
from definitions import MAPS_DIR, STOP_EFFECT, CREATE_PWUP, PWUP_DICT, MAX_SCORES, GRADES
from game_state_machine.GameState import GameState
from utils import sound_path

# interval time to CREATE_PWUP event
PWUP_INTERVAL = 5000


class Playing(GameState, ABC):
    def __init__(self, next_state):
        super().__init__(next_state)
        self.paused = False

    def startup(self):
        if self.paused:  # came from Paused state
            return
        prohibited = self.map.get_prohibited_list()
        self.snake = Snake(prohibited=prohibited)
        self.food = Food(prohibited=prohibited)
        self.factory = PowerUpFactory(PWUP_DICT)  # available pwups can be changed here
        self.gain_sound = pygame.mixer.Sound(sound_path('aumentou.ogg'))
        self.powerup_sound = pygame.mixer.Sound(sound_path('powerup.ogg'))
        self.enter_sound = pygame.mixer.Sound(sound_path('enter.ogg'))
        self.interval = PWUP_INTERVAL
        pygame.time.set_timer(CREATE_PWUP, self.interval)
        self.active_powerups = []
        self.update_score()

    def cleanup(self):
        if self.paused:  # called by Paused state
            return
        del self.snake
        del self.food
        del self.factory

    def update(self):
        map_prohibited = self.map.get_prohibited_list()
        collided = self.snake.move(map_prohibited)
        if collided:
            self.on_collision()
            return

        if self.snake.get_head_position() == self.food.position:
            self.gain_sound.play()
            self.snake.length += 1
            prohibited = self.snake.body + self.factory.get_positions()
            prohibited += self.map.get_prohibited_list()
            self.food.randomize_position(prohibited)

        for p in self.factory.collectable_powerups:
            if self.snake.get_head_position() == p.position:
                self.powerup_sound.play()
                p.get_effect(self.snake)
                if p.lasting:
                    self.active_powerups.append(p)
                self.factory.collectable_powerups.remove(p)
                break

        self.update_score()

    def update_score(self):
        maxsc = MAX_SCORES[self.__str__()[7:]]
        sc = (self.snake.length - 1) / maxsc
        # fail -> belle epoque or little hell
        # legend -> cancer area
        fail = legend = False

        score = list(GRADES)[-1]
        for k, v in GRADES.items():
            if sc >= v:
                score = k
                break

        if score in ['L', 'XL', 'XLL']:
            legend = True

        if score in ['I', 'D']:
            fail = True

        score_text = "Score: {}".format(score)
        f = self.fonts['h2']
        self.score_surf = f.render(score_text, True, pygame.Color("yellow"))
        self.score_rect = self.score_surf.get_rect(left=self.get_screen_rect().left)
        self.score_rect.move_ip(10, 10)
        # change color based on the concepts
        if fail:
            color = pygame.Color("red")
        elif legend:
            color = pygame.Color("green")
        else:
            color = pygame.Color("yellow")
        self.score_surf = f.render(score_text, True, color)

    def draw(self, surface, draw_snake=True):
        self.map.draw(surface)
        if draw_snake:
            self.snake.draw(surface)
        self.food.draw(surface)
        for p in self.factory.collectable_powerups:
            p.draw(surface)
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
            self.enter_sound.play()
            self.paused = True
            self.done = True

    def on_mouse_up(self, e):
        pass

    def on_collision(self):
        self.next_state = 'Menu'
        self.done = True

    def get_event(self, event):
        if event.type == CREATE_PWUP:
            prohibited = self.snake.body + self.factory.get_positions() + [self.food.position]
            prohibited += self.map.get_prohibited_list()
            self.factory.maybe_create_powerup(prohibited)
            return True
        if event.type == STOP_EFFECT:  # todo: fixme, i'm BRONCO!
            if self.active_powerups:
                self.active_powerups.pop(0).reset_effect(self.snake)
                return True
        return super().get_event(event)

    def get_map(self, map_name):
        tmxpath = os.path.join(MAPS_DIR, 'tmx', map_name + '.tmx')
        tmxdata = load_pygame(tmxpath)
        self.map = Map(map_name, tmxdata, d=3)


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
