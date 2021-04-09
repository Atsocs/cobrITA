import os
import json

import pygame

from definitions import SPRITES_DIR


class Spritesheet:
    def __init__(self, spritesheet_name: str):
        png_path = os.path.join(SPRITES_DIR, spritesheet_name + '.png')
        json_path = os.path.join(SPRITES_DIR, spritesheet_name + '.json')
        self.sprite_sheet = pygame.image.load(png_path).convert()
        with open(json_path) as f:
            self.metadata = json.load(f)

    def parse_sprite(self, name: str) -> pygame.Surface:
        data = self.metadata['frames'][name]['frame']
        x, y, w, h = data['x'], data['y'], data['w'], data['h']
        sprite = pygame.Surface((w, h))
        rect = pygame.Rect(x, y, w, h)
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sprite_sheet, (0, 0), rect)
        return sprite
