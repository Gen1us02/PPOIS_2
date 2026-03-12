import pygame
from pygame import Surface
from src.utils.utils import Utils
from src.common.menu_options import MenuOptionMixin


class Rules(MenuOptionMixin):
    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)
        self.font = pygame.font.Font("assets/fonts/Sjz.otf", self.FONT_SIZE - 2)
        self.rules = Utils.load_rules("rules.txt")

    def draw(self) -> None:
        super().draw()
        current_y = self.rect_y + 20
        for string in self.rules:
            text = self.font.render(string, True, (255, 255, 255))
            text_rect = text.get_rect(topleft=(self.rect_x + 20, current_y))
            self.screen.blit(text, text_rect)
            current_y += self.FONT_SIZE - 2
