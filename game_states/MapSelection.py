import pygame
from pygame.locals import *

from definitions import background_color
from game_state_machine.GameState import GameState
from utils import sound_path


class MapSelection(GameState):
    def __init__(self):
        super().__init__()
        self.button_size = 60, 30

        # Cores utilizadas no MapSelection
        self.button_color = pygame.Color("yellow")
        self.color_when_clicked = pygame.Color("white")
        r = self.get_screen_rect()
        K = 50

        def f(i):
            s = pygame.Rect((0, 0), self.button_size)
            s.center = r.move(0, i * K).center
            return s

        # Mensagem e Posição do canto superior esquerdo de cada botao
        self.buttons = [
            {'name': 'hall', 'msg': '1', 'pos': f(-2)},  # hall do A
            {'name': 'feijao', 'msg': '2', 'pos': f(-1)},  # feijao
            {'name': 'quadra', 'msg': '3', 'pos': f(0)},  # quadra do C
            {'name': 'apart', 'msg': '4', 'pos': f(1)},  # apart do C-
            {'name': 'menu', 'msg': 'Menu', 'pos': f(2)},
        ]

        self.rects = [(b['pos'], b) for b in self.buttons]
        self.select_sound = pygame.mixer.Sound(sound_path('select.ogg'))
        self.enter_sound = pygame.mixer.Sound(sound_path('enter.ogg'))
        self.hover = False

    def startup(self):
        pass

    def cleanup(self):
        pass

    def update(self):
        pass

    def draw(self, surface):
        surface.fill(background_color)
        for b in self.buttons:
            self.draw_button(surface, b)

    def draw_button(self, surface, button_info):
        name = button_info['name']
        pos = button_info['pos']
        msg = button_info['msg']
        size = self.button_size

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(num_buttons=3)

        rect = pos
        inside = rect.collidepoint(mouse)
        color = self.color_when_clicked if inside else self.button_color
        pygame.draw.rect(surface, color, rect)

        # colocando texto no botão
        small_text = self.fonts['h2']  # fixme: h2 or m?
        text_surf, text_rect = self.text_objects(msg, small_text)
        text_rect.center = rect.center
        surface.blit(text_surf, text_rect)

    def on_key_up(self, e):
        if K_1 <= e.key <= K_4:
            selected = str(e.key - K_1 + 1)
            button = next(b for b in self.buttons if b['msg'] == selected)
            self.enter_sound.play()
            self.next_state = self.get_gameplay_state(button)
            self.done = True
        elif e.key == K_m:
            self.next_state = 'Menu'
            self.enter_sound.play()
            self.done = True

    def on_mouse_up(self, e):
        if e.button == 1:
            collided, next_state = self.get_collisions(e.pos)
            if collided:
                self.enter_sound.play()
                self.next_state = next_state
                self.done = True

    def get_collisions(self, pos):
        collided, msg = False, ''
        for r, button in self.rects:
            if r.collidepoint(pos):
                msg = button['msg']
                if msg.isnumeric():
                    next_state = self.get_gameplay_state(button)
                else:
                    next_state = msg
                return True, next_state
        return False, None

    def get_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            previous = self.hover
            self.hover = False
            for rect, button in self.rects:
                if rect.collidepoint(event.pos):
                    self.hover = True
            if self.hover and not previous:
                self.select_sound.play()

        super(MapSelection, self).get_event(event)

    @staticmethod
    def get_gameplay_state(button):
        return 'Playing' + button['name'].title().replace(' ', '')

    @staticmethod
    def text_objects(text, font):
        """
        Cria o retângulo com escrita (o botão)
        """
        text_surface = font.render(text, True, pygame.Color("black"))
        return text_surface, text_surface.get_rect()
