import sys

import pygame

from game_state_machine.GameControl import GameControl
from game_states.Menu import Menu

pygame.init()
screen = pygame.display.set_mode(screen_size := (480, 480))
fps = 60

states = [Menu()]
start_state = 'Menu'

game = GameControl(states, start_state, screen, fps)
game.run()
pygame.quit()
sys.exit()
