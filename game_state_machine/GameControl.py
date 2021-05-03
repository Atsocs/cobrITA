import pygame
from state_machine.Control import Control
from game_states.Playing import Playing
from utils import sound_path


class GameControl(Control):
    def __init__(self, states, start_state, screen, fps):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.clock_counter = 0
        super().__init__(states, start_state)

    def run(self):
        """
        Pretty much the entirety of the game's runtime will be
        spent inside this while loop.
        """
        pygame.mixer.music.load(sound_path("na_cova_dela.ogg"))
        pygame.mixer.music.play(-1)
        while not self.done:
            self.clock_counter += 1
            self.clock.tick(self.fps)
            self.event_loop()
            self.update()
            self.draw()
            pygame.display.update()

    def event_loop(self):
        """Events are passed for handling to the current state."""
        for event in pygame.event.get():
            self.state.get_event(event)

    def update(self):
        """
        Check for state flip and update active state.
        """
        super().update()
        if issubclass(self.state.__class__, Playing):
            if self.clock_counter >= self.state.snake.update_counter:
                self.clock_counter = 0
                self.state.update(self.screen)
        else:
            self.state.update()

    def draw(self):
        """Pass display surface to active state for drawing."""
        self.state.draw(self.screen)
