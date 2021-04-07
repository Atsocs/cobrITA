import pygame
from pygame.locals import *

from definitions import background_color
from game_state_machine.GameState import GameState


class Paused (GameState):
    def __init__(self):
        super().__init__()
        self.options = ["Paused", "Resume", "Exit"]

    def startup(self):
        self.selected = 1
        self.go_to_menu = False
        self.select(self.selected)
        self.update()

    def cleanup(self):
        self.unselect(self.selected)

    def update(self):
        self.set_texts()
        self.set_rect_centers()

    def draw(self, surface):
        surface.fill(background_color)
        surface.blit(self.title, self.title_rect)
        surface.blit(self.resume, self.resume_rect)
        surface.blit(self.exit, self.exit_rect)

    def on_key_up(self, e):
        if e.key in [K_DOWN, K_RIGHT]:
            self.down()
        elif e.key in [K_UP, K_LEFT]:
            self.up()
        elif e.key in [K_RETURN, K_KP_ENTER, K_SPACE]:
            selected_text = self.options[self.selected]
            self.done = True

    def on_mouse_up(self, e):
        pass

    def down(self):
        self.unselect(self.selected)
        self.selected += 1
        print(self.selected)
        if self.selected >= len(self.options):
            self.selected = 1
        self.select(self.selected)

    def up(self):
        self.unselect(self.selected)
        self.selected -= 1
        print(self.selected)
        if self.selected <= 0:
            self.selected = len(self.options) - 1
        self.select(self.selected)

    def set_texts(self):
        f1, f2 = (self.fonts[x] for x in ('h1', 'h2'))
        self.title = f1.render(self.options[0], True, pygame.Color("blue"))
        self.resume = f2.render(self.options[1], True, pygame.Color("red"))
        self.exit = f2.render(self.options[2], True, pygame.Color("green"))

    def set_rect_centers(self):
        self.set_texts()
        self.title_center = (self.get_screen_rect().center[0], self.get_screen_rect().center[1] - 30)
        self.resume_center = (self.get_screen_rect().center[0], self.get_screen_rect().center[1])
        self.exit_center = (self.get_screen_rect().center[0], self.get_screen_rect().center[1] + 20)
        self.title_rect = self.title.get_rect(center=self.title_center)
        self.resume_rect = self.resume.get_rect(center=self.resume_center)
        self.exit_rect = self.exit.get_rect(center=self.exit_center)

    def select(self, idx):
        self.options[idx] = '< ' + self.options[idx] + ' >'

    def unselect(self, idx):
        self.options[idx] = self.options[idx][2:-2]

    @staticmethod
    def to_gamestate(string):
        return string.title().replace('<', '').replace('>', '').replace(' ', '')
