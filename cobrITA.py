import sys

import pygame

from definitions import PX, L
from game_state_machine.GameControl import GameControl
from game_states.Achievements import Achievements
from game_states.Credits import Credits
from game_states.Help import Help
from game_states.MapSelection import MapSelection
from game_states.Menu import Menu
from game_states.Paused import Paused
from game_states.Playing import PlayingFeijao, PlayingQuadra, PlayingApart, PlayingHall

pygame.init()
screen = pygame.display.set_mode(screen_size := (PX * L, PX * L))
fps = 5

states = [Menu(),
          Credits('Menu'), Help('Menu'), Achievements('Menu'),
          MapSelection(), Paused(),
          PlayingFeijao(), PlayingQuadra(), PlayingApart(), PlayingHall()]
start_state = 'Menu'

game = GameControl(states, start_state, screen, fps)
game.run()
pygame.quit()
sys.exit()
