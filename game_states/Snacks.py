import pygame
from definitions import PX, L
from tkinter import messagebox
from tkinter import *


def snack_gameplay(state_name, state, screen):
    if state_name in ['PlayingApart', 'PlayingHall', 'PlayingFeijao', 'PlayingQuadra']:
        if state.score < 0.005 * PX * L:
            global_snack.pop()
            global_snack.push("Você está com D - Desligamento")
            global_snack.draw(screen)
        elif state.score < 0.010 * PX * L:
            global_snack.pop()
            global_snack.push("Você está com I - Incapaz")
            global_snack.draw(screen)
        elif state.score < 0.015 * PX * L:
            global_snack.pop()
            global_snack.push("Você está com R - Ruim")
            global_snack.draw(screen)
        elif state.score < 0.020 * PX * L:
            global_snack.pop()
            global_snack.push("Você está com B - Bom")
            global_snack.draw(screen)
        elif state.score < 0.3 * PX * L:
            global_snack.pop()
            global_snack.push("Você está com MB - Muito Bom")
            global_snack.draw(screen)
        else:
            global_snack.pop()
            global_snack.push("Você está com L - Lunático")
            global_snack.draw(screen)


class Snacks:
    def __init__(self):
        self.stack = []

    def push(self, message):
        if not self.empty():
            if message == self.stack[0]:
                return
        self.stack.append(message)

    def pop(self):
        if not self.empty():
            self.stack.pop()

    def draw(self, screen):
        if not self.empty():
            f = pygame.font.Font(None, 20)
            text_surf = f.render(self.stack[0], True, pygame.color.Color('Red'))
            text_rect = text_surf.get_rect(center=(500, 15))
            screen.blit(text_surf, text_rect)
        else:
            f = pygame.font.Font(None, 20)
            text_surf = f.render("", True, pygame.color.Color('Red'))
            text_rect = text_surf.get_rect(center=(500, 15))
            screen.blit(text_surf, text_rect)

    def empty(self):
        counter = 0
        for i in self.stack:
            counter+=1
        if counter == 0:
            return True
        return False

    def special(self):
        Tk().wm_withdraw()
        messagebox.showinfo('Seu desempenho', self.stack[0] if self.stack is not self.empty() else "Obrigado")


global_snack = Snacks()


