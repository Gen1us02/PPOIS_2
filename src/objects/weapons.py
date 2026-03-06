from abc import ABC, abstractmethod
import pygame
from pygame.sprite import Group
from .bullet import Bullet


class Weapon(ABC):
    @abstractmethod
    def shoot(self, x: int, y: int, bullets: Group, all_sprites: Group) -> None:
        pass


class Gun(Weapon):
    def __init__(self) -> None:
        self.shooting_sound = pygame.mixer.Sound("assets/audio/gun_shot.mp3")
        self.ammo = 8
        self.reload_time = 30
        self.damage = 10
        self.last_shot_time = 0
        self.shot_delay = 350

    def shoot(self, x: int, y: int, bullets: Group, all_sprites: Group) -> None:
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.shot_delay:
            self.last_shot_time = current_time
            bullet = Bullet(x, y, *pygame.mouse.get_pos())
            self.shooting_sound.play(0)
            bullets.add(bullet)
            all_sprites.add(bullet)


class Rifle(Weapon):
    def __init__(self) -> None:
        self.shooting_sound = pygame.mixer.Sound("assets/audio/rifle_shot.mp3")
        self.shooting_sound.set_volume(0.8)
        self.ammo = 30
        self.damage = 20
        self.reload_time = 30
        self.last_shot_time = 0
        self.shot_delay = 150

    def shoot(self, x: int, y: int, bullets: Group, all_sprites: Group) -> None:
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.shot_delay:
            self.last_shot_time = current_time
            bullet = Bullet(x, y, *pygame.mouse.get_pos())
            self.shooting_sound.play(0)
            bullets.add(bullet)
            all_sprites.add(bullet)


class Shotgun(Weapon):
    def __init__(self) -> None:
        self.shooting_sound = pygame.mixer.Sound("assets/audio/shotgun_shot.mp3")
        self.shooting_sound.set_volume(0.3)
        self.ammo = 6
        self.damage = 30
        self.reload_time = 40
        self.last_shot_time = 0
        self.shot_delay = 450

    def shoot(self, x: int, y: int, bullets: Group, all_sprites: Group) -> None:
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.shot_delay:
            self.last_shot_time = current_time
            mos_x, mos_y = pygame.mouse.get_pos()
            for i in range(4):
                target_posx = mos_x + (-1 if i % 2 == 0 else 1) * i * 10
                bullet = Bullet(x, y, target_posx, mos_y)
                bullets.add(bullet)
                all_sprites.add(bullet)
            self.shooting_sound.play(0)