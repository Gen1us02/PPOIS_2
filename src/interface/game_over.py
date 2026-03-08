import pygame
from pygame import Surface
from src.enums import States
from src.common.end_screen import EndScreenMixin


class GameOverScreen(EndScreenMixin):
    def __init__(self, screen: Surface):
        super().__init__(screen)

    def handle_events(self) -> States:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return States.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.is_highscore:
                        return States.NAME_INPUT
                    else:
                        return States.MENU
                if event.key == pygame.K_ESCAPE:
                    return States.MENU
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        return None

    def draw(self):
        super().draw()
        
        title = self.font.render("ИГРА ОКОНЧЕНА", True, (255, 100, 100))
        title_rect = title.get_rect(center=(self.screen.get_width() // 2, 150))
        self.screen.blit(title, title_rect)
