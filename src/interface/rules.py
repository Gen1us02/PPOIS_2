from typing import Optional

from pygame import Surface
import pygame
from src.config import config
from src.states import States
from src.utils.utils import Utils
from .button import Button


class Rules:
    RECT_WIDTH = 600
    RECT_HEIGHT = 700
    BUTTON_WIDTH = int(config["DEFAULT"]["BUTTON_WIDTH"])
    BUTTON_HEIGHT = int(config["DEFAULT"]["BUTTON_HEIGHT"])
    FONT_SIZE = int(config["DEFAULT"]["FONT_SIZE"])

    def __init__(self, screen: Surface) -> None:
        self.screen = screen
        self.rect_x = 0
        self.rect_y = 0
        self.font = pygame.font.Font("assets/fonts/Sjz.otf", self.FONT_SIZE)
        button_x = (self.screen.get_width() - self.BUTTON_WIDTH) // 2
        self.bg = pygame.image.load("assets/images/menu_background.png").convert_alpha()
        self.bg = pygame.transform.scale(
            self.bg, (self.screen.get_width(), self.screen.get_height())
        )
        pygame.draw.rect(
            self.screen,
            (186, 2, 2),
            (
                self.rect_x,
                self.rect_y,
                self.RECT_WIDTH,
                self.RECT_HEIGHT,
            ),
        )
        self.button = Button(
            button_x,
            self.screen.get_height() - self.BUTTON_HEIGHT - 10,
            self.BUTTON_WIDTH,
            self.BUTTON_HEIGHT,
            "Назад",
            (186, 2, 2),
            (230, 57, 57),
            States.MENU,
        )
        self.rules = Utils.load_rules("rules.txt")

    def draw(self) -> None:
        self.screen.blit(self.bg, (0, 0))
        current_y = self.rect_y + 20
        for string in self.rules:
            text = self.font.render(string, True, (255, 255, 255))
            text_rect = text.get_rect(topleft=(self.rect_x + 20, current_y))
            self.screen.blit(text, text_rect)
            current_y += self.FONT_SIZE + 5

        self.button.draw(self.screen)

    def handle_events(self) -> Optional[States]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return States.EXIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                action = self.button.check_event(event)
                if action:
                    return action
        return None
