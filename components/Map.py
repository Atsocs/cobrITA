import pygame

from utils import draw_image
from definitions import L


class Map:
    def __init__(self, name: str, tmxdata, d, w=L, h=L):
        self.w, self.h, self.d = w, h, d
        self.tmxdata = tmxdata
        self.is_free = self.prohibited = None
        self.get_is_free()
        self.get_prohibited_list()

    def draw(self, surface: pygame.Surface):
        for z in range(1, self.d):
            for x in range(self.w):
                for y in range(self.h):
                    image = self.tmxdata.get_tile_image(x, y, z)
                    draw_image(surface, image, x, y)

    def get_is_free(self):
        if self.is_free is not None:
            return self.is_free
        result = self.tmxdata.layers[0].data
        result = tuple([tuple(x) for x in result])
        self.is_free = result
        return result

    def get_prohibited_list(self):
        if self.prohibited is not None:
            return self.prohibited
        result = []
        for x in range(self.w):
            for y in range(self.h):
                if not self.is_free[y][x]:
                    result.append((x, y))
        self.prohibited = result
        return result
