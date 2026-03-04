from pygame import Surface
from src.utils.utils import Utils
from src.common.menu_options import MenuOptionMixin


class LeadersTable(MenuOptionMixin):
    def __init__(self, screen: Surface) -> None:
        super().__init__(screen)
        self.players = Utils.load_players("leaders.json")
        self.table_name = "Таблица рекордов"
        self.headers = ["Номер", "Имя", "Очки"]
        self.col_x = [
            self.rect_x + 50,
            self.rect_x + self.rect_width // 2 - 150,
            self.rect_x + self.rect_width - 150,
        ]
        self.y_headers = self.rect_y + 50
        self.row_height = (self.rect_height - 100) // len(self.players)

    def draw(self) -> None:
        super().draw()

        title = self.font.render(self.table_name, True, (255, 255, 255))
        title_rect = title.get_rect(
            center=(self.screen.get_width() // 2, self.rect_y + 25)
        )
        self.screen.blit(title, title_rect)

        for i, header in enumerate(self.headers):
            text = self.font.render(header, True, (255, 255, 255))
            self.screen.blit(text, (self.col_x[i], self.y_headers))

        for i, (name, score) in enumerate(self.players, 1):
            number_text = self.font.render(str(i), True, (255, 255, 255))
            name_text = self.font.render(name, True, (255, 255, 255))
            score_text = self.font.render(str(score), True, (255, 255, 255))

            self.screen.blit(
                number_text, (self.col_x[0], self.y_headers + self.row_height * i)
            )
            self.screen.blit(
                name_text, (self.col_x[1], self.y_headers + self.row_height * i)
            )
            self.screen.blit(
                score_text, (self.col_x[2], self.y_headers + self.row_height * i)
            )
