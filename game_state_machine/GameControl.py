import pygame
from state_machine.Control import Control


class GameControl(Control):
    def __init__(self, states, start_state, screen, fps):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.fps = fps
        super().__init__(states, start_state)

    def run(self):
        """
        Pretty much the entirety of the game's runtime will be
        spent inside this while loop.
        """
        while not self.done:
            if self.state.__str__()[:7] == 'Playing':
                # fps for Playing states
                c = self.state.snake.speed
                self.clock.tick(c*self.fps)
            else:
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
        self.state.update()

    def draw(self):
        """Pass display surface to active state for drawing."""
        self.state.draw(self.screen)
