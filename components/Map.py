import pygame

from utils import draw_image
from definitions import L


class Map:
    def __init__(self, name: str, tmxdata, is_free, d, w=L, h=L):
        self.w, self.h, self.d = w, h, d
        self.tmxdata = tmxdata
        self.is_free = is_free

    def draw(self, surface: pygame.Surface):
        for z in range(self.d):
            for x in range(self.w):
                for y in range(self.h):
                    image = self.tmxdata.get_tile_image(x, y, z)
                    draw_image(surface, image, x, y)
