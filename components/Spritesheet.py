import os
import json

import pygame

from definitions import SPRITES_DIR


class Spritesheet:
    def __init__(self, sprite_type: str):
        png_path = os.path.join(SPRITES_DIR, sprite_type + '.png')
        json_path = os.path.join(SPRITES_DIR, sprite_type + '.json')
        self.sprite_sheet = pygame.image.load(png_path).convert()
        with open(json_path) as f:
            self.metadata = json.load(f)
        f.close()

    def get_sprite(self, x: int, y: int, w: int, h: int) -> pygame.Surface:
        sprite = pygame.Surface((w, h))
        rect = pygame.Rect(x, y, w, h)
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sprite_sheet, (0, 0), rect)
        return sprite

    def parse_sprite(self, name: str) -> pygame.Surface:
        data = self.metadata[name]['frame']
        x, y, w, h = data['x'], data['y'], data['w'], data['h']
        image = self.get_sprite(x, y, w, h)
        return image
