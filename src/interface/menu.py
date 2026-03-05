from typing import Optional
from pygame import Surface
from src.enums import States
from src.interface.button import Button
from src.utils.utils import Utils
from src.config import config
import pygame


class Menu:
    BUTTON_WIDTH = int(config["DEFAULT"]["BUTTON_WIDTH"])
    BUTTON_HEIGHT = int(config["DEFAULT"]["BUTTON_HEIGHT"])
    BUTTON_Y = int(config["DEFAULT"]["BUTTON_Y"])
    BUTTON_PADDING = int(config["DEFAULT"]["BUTTON_PADDING"])

    def __init__(self, screen: Surface) -> None:
        self.screen = screen
        button_x = (self.screen.get_width() - self.BUTTON_WIDTH) // 2
        self.buttons = [
            Button(
                button_x,
                self.BUTTON_Y,
                self.BUTTON_WIDTH,
                self.BUTTON_HEIGHT,
                "Начать",
                (186, 2, 2),
                (230, 57, 57),
                States.START,
            ),
            Button(
                button_x,
                self.BUTTON_Y + self.BUTTON_PADDING,
                self.BUTTON_WIDTH,
                self.BUTTON_HEIGHT,
                "Таблица лидеров",
                (186, 2, 2),
                (230, 57, 57),
                States.LEADERS,
            ),
            Button(
                button_x,
                self.BUTTON_Y + self.BUTTON_PADDING * 2,
                self.BUTTON_WIDTH,
                self.BUTTON_HEIGHT,
                "Справка",
                (186, 2, 2),
                (230, 57, 57),
                States.RULES,
            ),
            Button(
                button_x,
                self.BUTTON_Y + self.BUTTON_PADDING * 3,
                self.BUTTON_WIDTH,
                self.BUTTON_HEIGHT,
                "Выход",
                (186, 2, 2),
                (230, 57, 57),
                States.EXIT,
            ),
        ]
        self.bg = pygame.image.load("assets/images/menu_background.png").convert_alpha()
        self.bg = pygame.transform.scale(
            self.bg, (self.screen.get_width(), self.screen.get_height())
        )
        self.game_name = pygame.image.load("assets/images/name.png").convert_alpha()
        self.game_name = Utils.scale_image(self.game_name, target_width=400)

        self.name_rect = self.game_name.get_rect()
        self.name_rect.centerx = self.screen.get_width() // 2
        self.name_rect.y = -100

    def handle_events(self) -> Optional[str]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return States.EXIT

            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    action = button.check_event(event)
                    if action:
                        return action

        return None

    def draw(self) -> None:
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.game_name, self.name_rect)
        for button in self.buttons:
            button.draw(self.screen)
