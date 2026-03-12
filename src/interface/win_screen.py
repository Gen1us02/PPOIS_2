import pygame
from pygame import Surface
from src.common.end_screen import EndScreenMixin


class WinScreen(EndScreenMixin):
    def __init__(self, screen: Surface):
        super().__init__(screen)

    def draw(self):
        super().draw()

        title = self.font.render("ВЫ ПОБЕДИЛИ", True, (255, 100, 100))
        title_rect = title.get_rect(center=(self.screen.get_width() // 2, 150))
        self.screen.blit(title, title_rect)

        trophy = pygame.image.load("assets/images/trophy.png").convert_alpha()
        trophy_rect = trophy.get_rect(
            center=(self.screen.get_width() // 2, self.screen.get_height() - 200)
        )
        self.screen.blit(trophy, trophy_rect)
