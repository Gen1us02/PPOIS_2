import pygame
from pygame import Surface
from src.enums import States
from src.config import config


class GameOverScreen:
    FONT_SIZE = int(config["DEFAULT"]["FONT_SIZE"])

    def __init__(self, screen: Surface):
        self.screen = screen
        self.font = pygame.font.Font("assets/fonts/Sjz.otf", self.FONT_SIZE)
        self.score = 0
        self.is_highscore = False

    def set_score(self, score: int, is_highscore: bool):
        self.score = score
        self.is_highscore = is_highscore

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
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))

        title = self.font.render("ИГРА ОКОНЧЕНА", True, (255, 100, 100))
        title_rect = title.get_rect(center=(self.screen.get_width() // 2, 150))
        self.screen.blit(title, title_rect)

        score_text = self.font.render(f"Ваш счёт: {self.score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(self.screen.get_width() // 2, 250))
        self.screen.blit(score_text, score_rect)

        if self.is_highscore:
            prompt = self.font.render(
                "Новый рекорд! Нажмите Enter, чтобы ввести имя", True, (255, 255, 0)
            )
        else:
            prompt = self.font.render(
                "Нажмите Enter, чтобы вернуться в меню", True, (255, 255, 255)
            )
        prompt_rect = prompt.get_rect(center=(self.screen.get_width() // 2, 350))
        self.screen.blit(prompt, prompt_rect)
