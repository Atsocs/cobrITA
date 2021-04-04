from abc import ABC

import pygame

from state_machine.State import State


class GameState(State, ABC):
    """
    Parent class for individual game states to inherit from.
    """

    def __init__(self, next_state=None):
        super().__init__(next_state)

    def update(self):
        raise NotImplementedError

    def draw(self, surface):
        raise NotImplementedError

    def on_key_up(self, e):
        raise NotImplementedError

    def on_mouse_up(self, e):
        raise NotImplementedError

    def get_event(self, event):
        """
        Handle a single event passed by the Game object.

        :return: True if some event was catched, False otherwise.
        """
        if event.type == pygame.QUIT:
            self.quit = True
            return True
        elif event.type == pygame.KEYUP:
            self.on_key_up(event)
            return True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.on_mouse_up(event)
            return True
        return False

    @staticmethod
    def get_screen_rect():
        return pygame.display.get_surface().get_rect()
