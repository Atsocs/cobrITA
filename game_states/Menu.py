import pygame
from pygame.locals import *

from definitions import background_color, credits_color, achiev_color
from game_state_machine.GameState import GameState


class Menu(GameState):
    def __init__(self):
        super().__init__()
        self.menus = ["Main Menu", "Map Selection", "Help", "Credits", "Achievements"]

    def startup(self):
        self.selected = 1
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
        surface.blit(self.mapselec, self.mapselec_rect)
        surface.blit(self.help, self.help_rect)
        surface.blit(self.credits, self.credits_rect)
        surface.blit(self.achiev, self.achiev_rect)

    def on_key_up(self, e):
        if e.key in [K_DOWN, K_RIGHT]:
            self.down()
        elif e.key in [K_UP, K_LEFT]:
            self.up()
        elif e.key in [K_RETURN, K_KP_ENTER, K_SPACE]:
            self.next_state = self.to_class(self.menus[self.selected])
            self.done = True

    def on_mouse_up(self, e):
        pass

    def down(self):
        self.unselect(self.selected)
        self.selected = 1 + (self.selected % (len(self.menus) - 1))
        self.select(self.selected)

    def up(self):
        self.unselect(self.selected)
        self.selected = (self.selected - 2) % (len(self.menus) - 1) + 1
        self.select(self.selected)

    def set_texts(self):
        f1, f2 = (self.fonts[x] for x in ('h1', 'h2'))
        self.title = f1.render(self.menus[0], True, pygame.Color("blue"))
        self.mapselec = f2.render(self.menus[1], True, pygame.Color("red"))
        self.help = f2.render(self.menus[2], True, pygame.Color("yellow"))
        self.credits = f2.render(self.menus[3], True, credits_color)
        self.achiev = f2.render(self.menus[4], True, achiev_color)

    def set_rect_centers(self):
        self.set_texts()
        self.title_center = (self.get_screen_rect().center[0], self.get_screen_rect().center[1] - 30)
        self.credits_center = (self.get_screen_rect().center[0], self.get_screen_rect().center[1] + 20)
        self.help_center = (self.get_screen_rect().center[0], self.get_screen_rect().center[1] + 40)
        self.mapselec_center = (self.get_screen_rect().center[0], self.get_screen_rect().center[1])
        self.achiev_center = (self.get_screen_rect().center[0], self.get_screen_rect().center[1] + 60)
        self.title_rect = self.title.get_rect(center=self.title_center)
        self.help_rect = self.help.get_rect(center=self.help_center)
        self.credits_rect = self.credits.get_rect(center=self.credits_center)
        self.mapselec_rect = self.mapselec.get_rect(center=self.mapselec_center)
        self.achiev_rect = self.achiev.get_rect(center=self.achiev_center)

    def select(self, idx):
        self.menus[idx] = '< ' + self.menus[idx] + ' >'

    def unselect(self, idx):
        self.menus[idx] = self.menus[idx][2:-2]

    @staticmethod
    def to_class(string):
        return string.title().replace('<', '').replace('>', '').replace(' ', '')
