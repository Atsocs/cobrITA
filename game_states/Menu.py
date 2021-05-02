import pygame
from pygame.locals import *

from definitions import background_color
from game_state_machine.GameState import GameState


class Menu(GameState):
    def __init__(self):
        super().__init__()
        self.menus = ["Main Menu", "Map Selection", "Help"]

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

    def on_key_up(self, e):
        if e.key in [K_DOWN, K_RIGHT]:
            self.down()
        elif e.key in [K_UP, K_LEFT]:
            self.up()
        elif e.key in [K_RETURN, K_KP_ENTER, K_SPACE]:
            self.next_state = self.unselect(self.selected, inplace=False).replace(' ', '')
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

    # noinspection DuplicatedCode
    def set_texts(self):
        f1, f2 = (self.fonts[x] for x in ('h1', 'h2'))
        self.title = f1.render(self.menus[0], True, pygame.Color("blue"))
        self.mapselec = f2.render(self.menus[1], True, pygame.Color("red"))
        self.help = f2.render(self.menus[2], True, pygame.Color("yellow"))

    # noinspection DuplicatedCode
    def set_rect_centers(self):
        self.set_texts()

        self.title_center = (self.get_screen_rect().center[0], self.get_screen_rect().center[1] - 30)
        self.mapselec_center = (self.get_screen_rect().center[0], self.get_screen_rect().center[1])
        self.help_center = (self.get_screen_rect().center[0], self.get_screen_rect().center[1] + 20)

        self.title_rect = self.title.get_rect(center=self.title_center)
        self.mapselec_rect = self.mapselec.get_rect(center=self.mapselec_center)
        self.help_rect = self.help.get_rect(center=self.help_center)

    def select(self, idx, inplace=True):
        selected = '< ' + self.menus[idx] + ' >'
        if inplace:
            self.menus[idx] = selected
        return selected

    def unselect(self, idx, inplace=True):
        unselected = self.menus[idx][2:-2]
        if inplace:
            self.menus[idx] = unselected
        return unselected
