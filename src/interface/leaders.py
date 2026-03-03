from typing import Optional

from src.interface.button import Button
from src.config import config
from pygame import Surface
from src.utils.utils import Utils
from src.states import States
import pygame

BUTTON_WIDTH = int(config["DEFAULT"]["BUTTON_WIDTH"])
BUTTON_HEIGHT = int(config["DEFAULT"]["BUTTON_HEIGHT"])
BUTTON_PADDING = int(config["DEFAULT"]["BUTTON_PADDING"])


class LeadersTable:
    def __init__(self, screen: Surface) -> None:
        self.screen = screen
        self.players = Utils.load_file("leaders.json")
        self.bg = pygame.image.load("assets/images/menu_background.png").convert_alpha()
        self.bg = pygame.transform.scale(
            self.bg, (self.screen.get_width(), self.screen.get_height())
        )

        self.table_name = "Таблица рекордов"
        button_x = (self.screen.get_width() - BUTTON_WIDTH) // 2
        self.headers = ["Номер в таблице", "Имя", "Очки"]
        self.font = pygame.font.Font("assets/fonts/Sjz.otf", 30)
        self.button = Button(
            button_x,
            self.screen.get_height() - BUTTON_HEIGHT - BUTTON_PADDING,
            BUTTON_WIDTH,
            BUTTON_HEIGHT,
            "Назад",
            (186, 2, 2),
            (230, 57, 57),
            States.MENU,
        )
        self.col_x = [150, 500, 800]
        self.y_headers = 50
        self.row_height = 50

    def draw(self) -> None:
        self.screen.blit(self.bg, (0, 0))

        title = self.font.render(self.table_name, True, (255, 255, 255))
        title_rect = title.get_rect(center=(self.screen.get_width() // 2, 30))
        self.screen.blit(title, title_rect)

        for i, header in enumerate(self.headers):
            text = self.font.render(header, True, (255, 255, 255))
            self.screen.blit(text, (self.col_x[i], self.y_headers))
        
         
        for i, (name, score) in enumerate(self.players, 1):
            number_text =  self.font.render(str(i), True, (255, 255, 255))
            name_text = self.font.render(name, True, (255, 255, 255))
            score_text = self.font.render(str(score), True, (255, 255, 255))
            
            self.screen.blit(number_text, (self.col_x[0], self.y_headers + self.row_height * i))
            self.screen.blit(name_text, (self.col_x[1], self.y_headers + self.row_height * i))
            self.screen.blit(score_text, (self.col_x[2], self.y_headers + self.row_height * i))

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
