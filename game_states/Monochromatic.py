import pygame

from game_state_machine.GameState import GameState


class Monochromatic(GameState):
    def __init__(self, next_state, color="black"):
        super().__init__(next_state=next_state)
        self.color = color

    def startup(self):
        pass

    def cleanup(self):
        pass

    def update(self):
        pass

    def draw(self, surface):
        surface.fill(pygame.Color(self.color))

    # Anything quits this state
    def on_key_up(self, e):
        self.done = True

    # Anything quits this state
    def on_mouse_up(self, e):
        self.done = True
