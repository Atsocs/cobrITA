import pygame
import os
from definitions import PX, SOUND_DIR


def draw_image(surface: pygame.Surface, image, x, y):
    if image is None:
        return
    surface.blit(image, (x * PX, y * PX))


def sound_path(filename: str):
    return os.path.join(SOUND_DIR, filename)
