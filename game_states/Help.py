from game_state_machine.GameState import GameState
from definitions import background_color, L, PX
from utils import sound_path
import pygame


# Inherit from a game_state that does nothing
class Help(GameState):
    def __init__(self):
        super().__init__()
        self.speed_text = "1. The rookie chain (our adapted snake) has a constant non-zero speed."
        self.direction_text = "2. For orientation use the arrow keys in your keyboard."
        self.pause_text = "3. Press 'esc' to pause (you don't lose progress)."
        self.rules_text = "4. To upgrade your score, collect more rookies (1 rookie = 1 score point)."
        self.boundary_text = "5. The map boundaries can do you harm, watch out!"
        self.final_text = "6. Press any key to go back to the Main Menu."
        self.texts = ["Help Menu", self.speed_text, self.direction_text, self.pause_text,
                      self.rules_text, self.boundary_text, self.final_text]
        self.enter_sound = pygame.mixer.Sound(sound_path('enter.ogg'))

    def startup(self):
        self.update()

    def cleanup(self):
        pass

    def update(self):
        self.set_texts()
        self.set_rect_centers()

    def draw(self, surface):
        M = 20
        border_rect = pygame.Rect((0, 0), (L * PX - 2 * M, L * PX - 2 * M)).inflate(0, -250)
        border_rect.center = self.get_screen_rect().center
        surface.fill(background_color)
        pygame.draw.rect(surface, "orange", border_rect, width=2, border_radius=1)
        surface.blit(self.title, self.title_rect)
        surface.blit(self.speed, self.speed_rect)
        surface.blit(self.direction, self.direction_rect)
        surface.blit(self.pause, self.pause_rect)
        surface.blit(self.rules, self.rules_rect)
        surface.blit(self.boundary, self.boundary_rect)
        surface.blit(self.final, self.final_rect)

    def on_key_up(self, e):
        self.next_state = "Menu"
        self.enter_sound.play()
        self.done = True

    def on_mouse_up(self, e):
        pass

    def down(self):
        pass

    def up(self):
        pass

    # noinspection DuplicatedCode
    def set_texts(self):
        f1, f2 = (self.fonts[x] for x in ('h2', 'h3'))
        self.title = f1.render(self.texts[0], True, pygame.Color("green"))
        self.speed = f2.render(self.texts[1], True, pygame.Color("yellow"))
        self.direction = f2.render(self.texts[2], True, pygame.Color("yellow"))
        self.pause = f2.render(self.texts[3], True, pygame.Color("yellow"))
        self.rules = f2.render(self.texts[4], True, pygame.Color("yellow"))
        self.boundary = f2.render(self.texts[5], True, pygame.Color("yellow"))
        self.final = f2.render(self.texts[6], True, pygame.Color("red"))

    # noinspection DuplicatedCode
    def set_rect_centers(self):
        self.set_texts()

        r = self.get_screen_rect()
        K = 30
        self.title_center = r.move(0, -3 * K).center
        self.speed_center = r.move(0, -2 * K).center
        self.direction_center = r.move(0, - 1 * K).center
        self.pause_center = r.move(0, 0 * K).center
        self.rules_center = r.move(0, 1 * K).center
        self.boundary_center = r.move(0, 2 * K).center
        self.final_center = r.move(0, 3 * K).center

        self.title_rect = self.title.get_rect(center=self.title_center)
        self.speed_rect = self.speed.get_rect(center=self.speed_center)
        self.direction_rect = self.direction.get_rect(center=self.direction_center)
        self.pause_rect = self.pause.get_rect(center=self.pause_center)
        self.rules_rect = self.rules.get_rect(center=self.rules_center)
        self.boundary_rect = self.boundary.get_rect(center=self.boundary_center)
        self.final_rect = self.final.get_rect(center=self.final_center)
