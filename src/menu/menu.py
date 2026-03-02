from typing import Optional
from pygame import Surface
from src.states import States
import pygame


class Menu:
    def __init__(self, screen: Surface) -> None:
        self.screen = screen
        self.buttons = [
            {
                "rect": pygame.Rect(300, 200, 200, 50),
                "text": "Начать",
                "action": States.START,
            },
            {
                "rect": pygame.Rect(300, 300, 200, 50),
                "text": "Таблица лидеров",
                "action": States.LEADERS,
            },
            {
                "rect": pygame.Rect(300, 400, 200, 50),
                "text": "Справка",
                "action": States.RULES,
            },
            {
                "rect": pygame.Rect(300, 500, 200, 50),
                "text": "Выйти",
                "action": States.EXIT,
            },
        ]
        self.font = pygame.font.Font("assets/fonts/Sjz.otf", 30)
        self.bg = pygame.image.load("assets/images/menu_background.png").convert_alpha()
        self.game_name = pygame.image.load("assets/images/name.png").convert_alpha()
        self.game_name = self._scale_image(self.game_name, target_width=400)

        self.name_rect = self.game_name.get_rect()
        self.name_rect.centerx = self.screen.get_width() // 2
        self.name_rect.y = -100

    def handle_events(self) -> Optional[str]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    if button["rect"].collidepoint(event.pos):
                        return button["action"]

        return None

    def _scale_image(self, image: Surface, target_width: int):
        original_width, original_height = image.get_size()
        scale_factor = target_width / original_width
        new_height = int(original_height * scale_factor)
        return pygame.transform.smoothscale(image, (target_width, new_height))

    def draw(self) -> None:
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.game_name, self.name_rect)
        for button in self.buttons:
            pygame.draw.rect(self.screen, (186, 2, 2), button["rect"])
            text = self.font.render(button["text"], True, (0, 0, 0))
            text_rect = text.get_rect(center=button["rect"].center)
            self.screen.blit(text, text_rect)
