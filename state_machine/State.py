class State(object):
    """
    Parent class for individual states to inherit from.
    """

    def __init__(self, next_state=None):
        self.done = False
        self.quit = False
        self.prev_state = None
        self.next_state = next_state

    def __str__(self):
        return self.__class__.__name__

    def startup(self):
        """
        Called when a state resumes being active.
        """
        raise NotImplementedError

    def cleanup(self):
        """
        Called when a state stops being active.
        """
        raise NotImplementedError
