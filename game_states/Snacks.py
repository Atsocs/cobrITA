from definitions import background_color
import pygame
import time
from pygame.locals import *
from game_state_machine import GameState


class Snacks(GameState.GameState):
    def __init__(self, message, font, size, x_pos, y_pos, color, t):
        super().__init__()
        self.msg = message
        self.font = font
        self.size = size
        self.center = (x_pos, y_pos)
        self.col = color
        self.time = t

    def startup(self):
        self.update()

    def cleanup(self):
        pass

    def update(self):
        self.set_text()
        self.set_rect()

    def draw(self, surface):
        t = self.set_time()
        while time.time() != t:
            surface.fill(background_color)
            surface.blit(self.text, self.center)

    def set_text(self):
        self.text = self.font.render(self.msg, True, pygame.Color(self.col))

    def set_rect(self):
        self.set_text()
        self.text_cent = self.text.get_rect(center=self.center)

    def set_time(self):
        t0 = time.time()
        tf = t0 + self.time
        return tf

    def on_key_up(self, e):
        pass

    def on_mouse_up(self, e):
        pass




