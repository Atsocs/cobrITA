import os

import pygame

from utils import draw_image
from definitions import MAPS_DIR, L


class Map:
    def __init__(self, name: str, tmxdata, w=L, h=L):
        self.w, self.h = w, h
        self.read(name)
        self.tmxdata = tmxdata

    def read(self, filename):
        p = os.path.join(MAPS_DIR, 'txt', filename + '.txt')
        self.is_free = []
        with open(p) as f:
            for i, line in enumerate(f):
                self.is_free.append([c == '_' for c in line.strip('\n')])

    def print(self, chars='1_'):
        for ln in self.is_free:
            print(''.join([chars[i] for i in ln]))

    def draw(self, surface: pygame.Surface):
        for x in range(self.w):
            for y in range(self.h):
                image = self.tmxdata.get_tile_image(x, y, layer=0)
                draw_image(surface, image, x, y)
