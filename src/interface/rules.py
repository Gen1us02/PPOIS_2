from typing import Optional

from pygame import Surface
import pygame
from src.config import config
from src.states import States
from src.utils.utils import Utils
from .button import Button


class Rules:
    BUTTON_WIDTH = int(config["DEFAULT"]["BUTTON_WIDTH"])
    BUTTON_HEIGHT = int(config["DEFAULT"]["BUTTON_HEIGHT"])
    FONT_SIZE = int(config["DEFAULT"]["FONT_SIZE"])

    def __init__(self, screen: Surface) -> None:
        self.screen = screen
        self.rect_x = 20
        self.rect_y = 20
        self.rect_width = self.screen.get_width() - 2 * self.rect_x
        self.rect_height = (
            self.screen.get_height() - 2 * self.rect_y - self.BUTTON_HEIGHT - 30
        )
        self.font = pygame.font.Font("assets/fonts/Sjz.otf", self.FONT_SIZE - 1)
        self.bg = pygame.image.load("assets/images/menu_background.png").convert_alpha()
        self.bg = pygame.transform.scale(
            self.bg, (self.screen.get_width(), self.screen.get_height())
        )
        button_x = (self.screen.get_width() - self.BUTTON_WIDTH) // 2
        button_y = self.rect_y + self.rect_height + 20
        self.button = Button(
            button_x,
            button_y,
            self.BUTTON_WIDTH,
            self.BUTTON_HEIGHT,
            "Назад",
            (186, 2, 2),
            (230, 57, 57),
            States.MENU,
        )
        self.rect_surface = pygame.Surface(
            (self.rect_width, self.rect_height), pygame.SRCALPHA
        )
        self.rect_surface.fill((100, 100, 100, 180))
        self.rules = Utils.load_rules("rules.txt")

    def draw(self) -> None:
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.rect_surface, (self.rect_x, self.rect_y))
        current_y = self.rect_y + 20
        for string in self.rules:
            text = self.font.render(string, True, (255, 255, 255))
            text_rect = text.get_rect(topleft=(self.rect_x + 20, current_y))
            self.screen.blit(text, text_rect)
            current_y += self.FONT_SIZE

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
