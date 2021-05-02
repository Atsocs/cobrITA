import os
import pygame
from pygame.locals import *

from definitions import background_color, UPDATE_CONST, SPRITES_DIR
from game_state_machine.GameState import GameState
from components.Spritesheet import Spritesheet


class Menu(GameState):
    def __init__(self):
        super().__init__()
        self.menus = ["Main Menu", "Map Selection", "Help"]
        self.spritesheet = Spritesheet('Character')
        self.num_sprites = 4
        self.sprite_counter = 0
        hat_path = os.path.join(SPRITES_DIR, 'chapeu_magicos.png')
        self.hat = pygame.image.load(hat_path).convert_alpha()

    def startup(self):
        self.selected = 1
        self.select(self.selected)
        self.update()

    def cleanup(self):
        self.unselect(self.selected)

    def update(self):
        self.set_texts()
        self.set_rects()

    def draw(self, surface: pygame.Surface):
        surface.fill(background_color)

        surface.blit(self.title, self.title_rect)
        surface.blit(self.mapselec, self.mapselec_rect)
        surface.blit(self.help, self.help_rect)
        surface.blit(self.hat, self.hat_rect)

        if self.sprite_counter >= self.num_sprites*UPDATE_CONST:
            self.sprite_counter = 0

        sprite = self.get_sprite()
        surface.blit(sprite, self.animation_rect_right)
        surface.blit(sprite, self.animation_rect_left)

        self.sprite_counter += 1

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
    def set_rects(self):
        self.set_texts()

        self.title_center = (self.get_screen_rect().center[0], self.get_screen_rect().center[1] - 30)
        self.mapselec_center = (self.get_screen_rect().center[0], self.get_screen_rect().center[1])
        self.help_center = (self.get_screen_rect().center[0], self.get_screen_rect().center[1] + 20)

        self.title_rect = self.title.get_rect(center=self.title_center)
        self.mapselec_rect = self.mapselec.get_rect(center=self.mapselec_center)
        self.help_rect = self.help.get_rect(center=self.help_center)

        self.hat_topleft = (self.get_screen_rect().bottomright[0] - 150, self.get_screen_rect().bottomright[1] - 150)
        self.animation_right = (self.title_rect.right + 20, self.title_rect.y)
        self.animation_left = (self.title_rect.left - 52, self.title_rect.y)

        self.hat_rect = pygame.Rect(self.hat_topleft, (128, 128))
        self.animation_rect_right = pygame.Rect(self.animation_right, (32, 32))
        self.animation_rect_left = pygame.Rect(self.animation_left, (32, 32))

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

    def get_sprite(self):
        frame_name = 'down_{}'.format(self.sprite_counter//UPDATE_CONST)
        sprite = self.spritesheet.parse_sprite(frame_name)
        return sprite