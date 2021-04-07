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

    def _flip_state(self):
        if self.state_name == 'Paused':
            self.state.next_state = 'Menu' if self.state.go_to_menu else self.previous_state
        self.previous_state = self.state_name
        super()._flip_state()

