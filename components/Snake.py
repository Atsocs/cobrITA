import random
import pygame

from definitions import L, PX, UPDATE_CONST
from components.Spritesheet import Spritesheet
from utils import sound_path


class Snake:
    def __init__(self, prohibited=None, head=None, hd=None):
        self.width = self.height = L
        self.length = 1
        self.update_counter = UPDATE_CONST

        head = self.initial_head(prohibited) if head is None else head
        self.body = [head]

        self.up = (0, -1)
        self.down = (0, 1)
        self.left = (-1, 0)
        self.right = (1, 0)
        d = (self.up, self.down, self.left, self.right)
        self.head_direction = random.choice(d) if hd is None else hd
        self.directions = [self.head_direction]

        self.sprite_counter = 0
        self.num_sprites = 4
        self.spritesheet = Spritesheet('Character')
        self.lost_sound = pygame.mixer.Sound(sound_path('perdeu.ogg'))

        self.last_turn_command = self.head_direction
        self.turns_to_apply = []

    def get_head_position(self):
        return self.body[0]

    def add_turn_command(self, to):
        if (to[0] * -1, to[1] * -1) == self.last_turn_command:
            return
        self.last_turn_command = to
        self.turns_to_apply.append(to)

    def move(self, map_prohibited=None):
        """
        :return: has collided?
        """

        if map_prohibited is None:
            map_prohibited = []

        def lose():
            self.lost_sound.play()
            return True

        cur = self.get_head_position()

        # turn
        if self.turns_to_apply:
            self.head_direction = self.turns_to_apply.pop(0)

        x, y = self.head_direction
        new_x, new_y = new = (cur[0] + x, cur[1] + y)

        # checks if snake collided with something inside the map
        if new in map_prohibited:
            return lose()

        # checks if the snake collided with map borders
        if new_x < 0 or new_x >= self.width or new_y >= self.height or new_y < 0:
            return lose()

        # checks if the snake collided with itself
        if new in self.body[3:]:
            return lose()
        else:
            self.body.insert(0, new)
            self.directions.insert(0, self.head_direction)
            if len(self.body) > self.length:
                self.body.pop()
            if len(self.directions) > self.length:
                self.directions.pop()
            return False

    def draw(self, surface: pygame.Surface):
        if self.sprite_counter >= self.num_sprites * self.update_counter:
            self.sprite_counter = 0  # fixme

        for pos, direction in zip(self.body, self.directions):
            pos = tuple((PX * x) for x in pos)  # fixme
            sprite = self.get_sprite(direction)
            surface.blit(sprite, pos)

        self.sprite_counter += 1

    def get_sprite(self, d):
        possible_directions = [{'dir': self.__dict__[x], 'name': x} for x in ('up', 'down', 'left', 'right')]
        direction = next(x['name'] for x in possible_directions if x['dir'] == d)
        frame_name = f'{direction}_{self.sprite_counter // self.update_counter}'
        sprite = self.spritesheet.parse_sprite(frame_name)
        return sprite

    def reverse(self):
        tmp = []
        for i, d in enumerate(self.directions):
            if d == self.up:
                tmp.insert(0, self.down)
            elif d == self.left:
                tmp.insert(0, self.right)
            elif d == self.right:
                tmp.insert(0, self.left)
            elif d == self.down:
                tmp.insert(0, self.up)
        self.directions = tmp
        self.head_direction = tmp[0]
        self.body.reverse()

    def initial_head(self, prohibited=None):
        if prohibited is None:
            prohibited = []
        while True:
            head = (
                random.randint(0, self.width - 1),
                random.randint(0, self.height - 1)
            )
            if head not in prohibited:
                return head
