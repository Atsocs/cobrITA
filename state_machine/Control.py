class Control(object):
    def __init__(self, states, start_state):
        states = {str(x): x for x in states}
        self.done = False
        self.states = states
        self.state_name = start_state
        self.previous_state = None
        self.state = self.states[self.state_name]
        self.state.startup()

    def update(self):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self._flip_state()

    def next(self):
        self.state.done = True
        self.update()

    def _flip_state(self):
        """Switch to the next game state."""
        next_state = self.state.next_state
        assert next_state is not None
        self.state.done = False
        self.state.cleanup()
        self.state_name = next_state
        self.state = self.states[self.state_name]
        self.state.startup()
