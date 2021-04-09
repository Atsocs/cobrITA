from definitions import background_color
import pygame
import time
from pygame.locals import *
from game_state_machine import GameState
from tkinter import *
from tkinter import messagebox


class Snacks(GameState.GameState):
    def __init__(self, message, size, x_pos, y_pos, color, t):
        super().__init__()
        self.msg = message
        self.font = self.fonts['h1']
        self.size = size
        self.center = (x_pos, y_pos)
        self.col = color
        self.time = t
        self.surface = pygame.display.get_surface()
        self.startup()

    def startup(self):
        self.update()

    def cleanup(self):
        pass

    def update(self):
        self.set_text()
        self.set_rect()
        self.draw(self.surface)

    def draw(self, surface):
        t = self.time + time.time()
        while t > time.time():
            surface.fill('white')
            surface.blit(self.title, self.msg_cent)

    def set_text(self):
        f = self.font
        self.title = f.render(self.msg, True, pygame.Color(self.col))

    def set_rect(self):
        self.set_text()
        self.msg_cent = self.title.get_rect(center=self.center)

    def set_time(self):
        t0 = time.time()
        tf = t0 + self.time
        return tf

    def on_key_up(self, e):
        pass

    def on_mouse_up(self, e):
        pass




