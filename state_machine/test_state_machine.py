from state_machine.Control import Control
from state_machine.State import State


class A(State):
    def startup(self):
        pass

    def cleanup(self):
        pass


class B(State):
    def startup(self):
        pass

    def cleanup(self):
        pass


class C(State):
    def startup(self):
        pass

    def cleanup(self):
        pass


def test_cyclic_state_machine():
    states = [A('B'), B('C'), C('A')]
    start_state = 'A'
    c = Control(states, start_state)
    for s in states:
        assert str(c.state) == str(s)
        c.next()


if __name__ == '__main__':
    test_cyclic_state_machine()
