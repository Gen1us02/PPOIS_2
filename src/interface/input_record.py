from typing import Tuple
import pygame
from pygame import Surface
from src.enums import States
from src.config import config


class RecordInputScreen:
    FONT_SIZE = int(config["DEFAULT"]["FONT_SIZE"])

    def __init__(self, screen: Surface):
        self.screen = screen
        self.font = pygame.font.Font("assets/fonts/Sjz.otf", self.FONT_SIZE)
        self.name = ""
        self.max_length = 15
        self.score = 0

    def set_score(self, score: int):
        self.score = score

    def handle_events(self) -> Tuple[States, str]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return States.EXIT, ""
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.name.strip():
                        return States.LEADERS, self.name.strip()
                    else:
                        return States.MENU, ""
                elif event.key == pygame.K_BACKSPACE:
                    self.name = self.name[:-1]
                elif event.key == pygame.K_ESCAPE:
                    return States.MENU, ""
                else:
                    if len(self.name) < self.max_length and event.unicode.isprintable():
                        self.name += event.unicode
        return None, ""

    def draw(self):
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        self.screen.blit(overlay, (0, 0))

        prompt = self.font.render("Введите ваше имя:", True, (255, 255, 255))
        prompt_rect = prompt.get_rect(center=(self.screen.get_width() // 2, 200))
        self.screen.blit(prompt, prompt_rect)

        input_text = self.font.render(self.name + "_", True, (255, 255, 0))
        input_rect = input_text.get_rect(center=(self.screen.get_width() // 2, 280))
        self.screen.blit(input_text, input_rect)

        instr = self.font.render(
            "Enter - подтвердить, Esc - отмена", True, (180, 180, 180)
        )
        instr_rect = instr.get_rect(center=(self.screen.get_width() // 2, 360))
        self.screen.blit(instr, instr_rect)
