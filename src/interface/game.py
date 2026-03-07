from __future__ import annotations

import random
from typing import Optional, Tuple
from pygame import Surface
import pygame
from src.enums import States, EnemyType
from src.config import config
from src.objects.player import Player
from src.utils.fabrics import Fabric


class Game:
    FONT_SIZE = int(config["DEFAULT"]["FONT_SIZE"])

    def __init__(self, screen: Surface, fabric: Fabric) -> None:
        self.screen = screen
        x = self.screen.get_width() // 2
        y = self.screen.get_height() // 2
        self.player = Player(x, y)
        self.fabric = fabric
        self.played_music = False
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.cursor = pygame.image.load("assets/images/scope.png")
        self.waves = ...  # список загружается из json
        self.total_points = 0
        self.current_wave = 0
        self.enemies_count = 0
        self.font = pygame.font.Font("assets/fonts/Sjz.otf", self.FONT_SIZE)
        self.bg = pygame.image.load("assets/images/field_background.png")
        self.bg = pygame.transform.scale(
            self.bg, (self.screen.get_width(), self.screen.get_height())
        )
        self.all_sprites.add(self.player)

    def handle_events(self) -> Optional[States]:
        if not self.player.is_alive:
            return States.MENU

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return States.EXIT

        return None

    def reset(self) -> None:
        self.played_music = False
        self.play_music()
        x = self.screen.get_width() // 2
        y = self.screen.get_height() // 2
        self.player.rect.center = x, y
        self.player.reset_weapon()
        self.all_sprites.empty()
        self.enemies.empty()
        self.bullets.empty()
        self.all_sprites.add(self.player)
        self.player.health = 100
        self.total_points = 0
        self.current_wave = 0
        self.enemies_count = 0

    def get_enemies_count(self) -> None:
        return len(self.waves[self.current_wave])

    def resolve_enemy_collisions(self) -> None:
        enemies_list = [e for e in self.enemies if e.is_alive]
        for i in range(len(enemies_list)):
            first_enemy = enemies_list[i]
            for j in range(i + 1, len(enemies_list)):
                rest_enemy = enemies_list[j]
                if first_enemy.rect.colliderect(rest_enemy):
                    if first_enemy.rect.centerx < rest_enemy.rect.centerx:
                        first_enemy.rect.x -= 1
                        rest_enemy.rect.x += 1
                    else:
                        first_enemy.rect.x += 1
                        rest_enemy.rect.x -= 1
                    if first_enemy.rect.centery < rest_enemy.rect.centery:
                        first_enemy.rect.y -= 1
                        rest_enemy.rect.y += 1
                    else:
                        first_enemy.rect.y += 1
                        rest_enemy.rect.y -= 1

    def get_enemies_coords(self) -> Tuple[int, int]:
        directions = ["left", "right", "up", "down"]
        target_direction = random.choice(directions)
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        x, y = 0, 0

        if target_direction == "left":
            x, y = random.randint(-150, -100), random.randint(0, screen_height + 100)
        elif target_direction == "right":
            x, y = (
                random.randint(screen_width + 100, screen_width + 150),
                random.randint(0, screen_height + 100),
            )
        elif target_direction == "up":
            x, y = random.randint(0, screen_width + 100), random.randint(-150, -100)
        else:
            x, y = (
                random.randint(0, screen_width + 100),
                random.randint(screen_height + 100, screen_height + 150),
            )
            
        return x,y

    def play_music(self) -> None:
        if not self.played_music:
            self.played_music = True
            pygame.mixer.music.stop()
            pygame.mixer.music.load("assets/audio/game_music.mp3")
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1)

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
        if keys[pygame.K_r]:
            self.player.reload()

        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            if self.player.ammo > 0:
                self.player.shoot(self.bullets, self.all_sprites)
            else:
                self.player.reload()
        self.player.move(dx, dy)

        if self.enemies_count == 0:
            self.current_wave += 1
            self.enemies_count = self.current_wave * 2
            for i in range(self.enemies_count):
                x, y = self.get_enemies_coords()
                enemy = self.fabric.create(EnemyType.ZOMBIE, x, y)
                self.enemies.add(enemy)

        self.enemies.update(self.player.rect.x, self.player.rect.y)
        self.resolve_enemy_collisions()
        enemies_list = [e for e in self.enemies if e.is_alive]
        for i in range(len(enemies_list)):
            enemy = enemies_list[i]
            if not enemy.is_alive:
                continue
            if enemy.rect.colliderect(self.player):
                if enemy.rect.centerx < self.player.rect.centerx:
                    enemy.rect.x -= 1
                else:
                    enemy.rect.x += 1
                if enemy.rect.centery < self.player.rect.centery:
                    enemy.rect.y -= 1
                else:
                    enemy.rect.y += 1

        for enemy in self.enemies:
            if not enemy.is_alive:
                continue

            bullets = pygame.sprite.spritecollide(enemy, self.bullets, False)
            if bullets:
                enemy.health -= self.player.weapon_damage
                for bullet in bullets:
                    bullet.kill()
                if not enemy.is_alive:
                    self.total_points += enemy.points
                    enemy.kill()
                    self.enemies_count -= 1

            if pygame.sprite.collide_rect(self.player, enemy):
                enemy.damage(self.player)

        self.all_sprites.update()

    def next_wave(self) -> None:
        self.current_wave += 1
        self.enemies_count = self.get_enemies_count()

    def draw(self) -> None:
        self.screen.blit(self.bg, (0, 0))
        wave_count = self.font.render(f"Волна: {self.current_wave}", True, (0, 0, 0))
        enemies_count = self.font.render(
            f"Врагов осталось: {self.enemies_count}", True, (0, 0, 0)
        )
        points = self.font.render(f"Очки: {self.total_points}", True, (0, 0, 0))
        ammo = self.font.render(f"Боезапас: {self.player.ammo}", True, (0, 0, 0))
        self.enemies.draw(self.screen)
        self.all_sprites.draw(self.screen)
        self.player.draw(self.screen)
        pygame.mouse.set_visible(False)
        cursor_rect = self.cursor.get_rect(center=pygame.mouse.get_pos())
        self.screen.blit(self.cursor, cursor_rect)
        self.screen.blit(wave_count, (30, 20))
        self.screen.blit(enemies_count, (200, 20))
        self.screen.blit(points, (30, 70))
        self.screen.blit(ammo, (700, 20))
