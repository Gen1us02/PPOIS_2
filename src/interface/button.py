from typing import Optional, Tuple
from src.states import States
from src.config import config
from pygame import Surface
import pygame


class Button:
    FONT_SIZE = int(config["DEFAULT"]["FONT_SIZE"])

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        text: str,
        color: Tuple[int, int, int],
        hover_color: Tuple[int, int, int],
        action: States,
    ) -> None:
        self.__rect = pygame.Rect(x, y, width, height)
        self.__text = text
        self.__color = color
        self.__hover_color = hover_color
        self.__action = action
        self.__font = pygame.font.Font("assets/fonts/Sjz.otf", self.FONT_SIZE)

    def draw(self, screen: Surface) -> None:
        mouse_pos = pygame.mouse.get_pos()
        current_color = (
            self.__hover_color if self.__rect.collidepoint(mouse_pos) else self.__color
        )

        pygame.draw.rect(screen, current_color, self.__rect)
        text = self.__font.render(self.__text, True, (0, 0, 0))
        text_rect = text.get_rect(center=self.__rect.center)
        screen.blit(text, text_rect)

    def check_event(self, event) -> Optional[States]:
        if self.__rect.collidepoint(event.pos):
            return self.__action

        return None
