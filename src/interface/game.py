from typing import Optional
from pygame import Surface
import pygame
from src.enums import States
from src.config import config
from src.objects.player import Player


class Game:
    FONT_SIZE = int(config["DEFAULT"]["FONT_SIZE"])

    def __init__(self, screen: Surface) -> None:
        self.screen = screen
        x = self.screen.get_width() // 2
        y = self.screen.get_height() // 2
        self.player = Player(x, y)
        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.cursor = pygame.image.load("assets/images/scope.png")
        self.waves = ...  # список загружается из json
        self.score = 0
        self.current_wave = 1
        self.enemies_count = 10
        self.font = pygame.font.Font("assets/fonts/Sjz.otf", self.FONT_SIZE)
        self.bg = pygame.image.load("assets/images/field_background.png")
        self.bg = pygame.transform.scale(
            self.bg, (self.screen.get_width(), self.screen.get_height())
        )
        self.all_sprites.add(self.player)

    def handle_events(self) -> Optional[States]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return States.EXIT

        return None

    def get_enemies_count(self) -> None:
        return len(self.waves[self.current_wave])

    def update(self) -> None:
        keys = pygame.key.get_pressed()
        dx = 0
        dy = 0
        speed = self.player.speed
        
        if keys[pygame.K_a]:
            dx -= speed
        if keys[pygame.K_d]:
            dx += speed
        if keys[pygame.K_w]:
            dy -= speed
        if keys[pygame.K_s]:
            dy += speed
            
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            self.player.shoot(self.bullets, self.all_sprites)
        self.player.move(dx, dy)
        self.all_sprites.update()

    def next_wave(self) -> None:
        self.current_wave += 1
        self.enemies_count = self.get_enemies_count()

    def draw(self) -> None:
        self.screen.blit(self.bg, (0, 0))
        wave_count = self.font.render(f"Волна {self.current_wave}", True, (0, 0, 0))
        enemies_count = self.font.render(
            f"Врагов осталось: {self.enemies_count}", True, (0, 0, 0)
        )
        self.all_sprites.draw(self.screen)
        pygame.mouse.set_visible(False)
        cursor_rect = self.cursor.get_rect(center=pygame.mouse.get_pos())
        self.screen.blit(self.cursor, cursor_rect)
        self.screen.blit(wave_count, (30, 20))
        self.screen.blit(enemies_count, (200, 20))
