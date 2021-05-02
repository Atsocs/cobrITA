import pygame

from definitions import PX


def draw_image(surface: pygame.Surface, image, x, y):
    if image is None:
        return
    surface.blit(image, (x * PX, y * PX))
