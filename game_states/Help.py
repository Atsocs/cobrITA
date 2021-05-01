from game_state_machine.GameState import GameState
from definitions import background_color
import pygame
from pygame.locals import *


# Inherit from a game_state that does nothing
class Help(GameState):
    def __init__(self):
        super().__init__()
        self.speed_text = "1. The rookie chain (our adapted snake) has a constant a non-zero speed."
        self.direction_text = "2. For orientation use the arrow keys in your keyboard."
        self.pause_text = "3. Press 'esc' to pause (you don't lose progress)."
        self.rules_text = "4. To upgrade your score, collect more rookies (1 rookie = 1 score point)."
        self.boundary_text = "5. The map boundaries can do you harm, watch out!"
        self.final_text = "6. Press any key to go back to the Main Menu."
        self.texts = ["Help", self.speed_text, self.direction_text, self.pause_text,
                      self.rules_text, self.boundary_text, self.final_text]

    def startup(self):
        self.update()

    def cleanup(self):
        pass

    def update(self):
        self.set_texts()
        self.set_rect_centers()

    def draw(self, surface):
        surface.fill(background_color)
        surface.blit(self.title, self.title_rect)
        surface.blit(self.speed, self.speed_rect)
        surface.blit(self.direction, self.direction_rect)
        surface.blit(self.pause, self.pause_rect)
        surface.blit(self.rules, self.rules_rect)
        surface.blit(self.boundary, self.boundary_rect)
        surface.blit(self.final, self.final_rect)

    def on_key_up(self, e):
        self.next_state = "Menu"
        self.done = True


    def on_mouse_up(self, e):
        pass

    def down(self):
        pass

    def up(self):
        pass

    # noinspection DuplicatedCode
    def set_texts(self):
        f1, f2 = (self.fonts[x] for x in ('h1', 'h2'))
        self.title = f1.render(self.texts[0], True, pygame.Color("blue"))
        self.speed = f2.render(self.texts[1], True, pygame.Color("yellow"))
        self.direction = f2.render(self.texts[2], True, pygame.Color("yellow"))
        self.pause = f2.render(self.texts[3], True, pygame.Color("yellow"))
        self.rules = f2.render(self.texts[4], True, pygame.Color("yellow"))
        self.boundary = f2.render(self.texts[5], True, pygame.Color("yellow"))
        self.final = f2.render(self.texts[6], True, pygame.Color("red"))

    # noinspection DuplicatedCode
    def set_rect_centers(self):
        self.set_texts()

        self.title_center = (self.get_screen_rect().center[0], self.get_screen_rect().center[1] - 30)
        self.speed_center = (self.get_screen_rect().center[0], self.get_screen_rect().center[1])
        self.direction_center = (self.get_screen_rect().center[0], self.get_screen_rect().center[1] + 20)
        self.pause_center = (self.get_screen_rect().center[0], self.get_screen_rect().center[1] + 40)
        self.rules_center = (self.get_screen_rect().center[0], self.get_screen_rect().center[1] + 60)
        self.boundary_center = (self.get_screen_rect().center[0], self.get_screen_rect().center[1] + 80)
        self.final_center = (self.get_screen_rect().center[0], self.get_screen_rect().center[1] + 100)

        self.title_rect = self.title.get_rect(center=self.title_center)
        self.speed_rect = self.speed.get_rect(center=self.speed_center)
        self.direction_rect = self.direction.get_rect(center=self.direction_center)
        self.pause_rect = self.pause.get_rect(center=self.pause_center)
        self.rules_rect = self.rules.get_rect(center=self.rules_center)
        self.boundary_rect = self.boundary.get_rect(center=self.boundary_center)
        self.final_rect = self.final.get_rect(center=self.final_center)


