from abc import ABC, abstractmethod
import pygame
from pygame.sprite import Group
from .bullet import Bullet


class Weapon(ABC):
    @abstractmethod
    def shoot(self, x: int, y: int, bullets: Group, all_sprites: Group) -> None:
        pass

    @abstractmethod
    def reload(self) -> None:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass


class Gun(Weapon):
    def __init__(self) -> None:
        self.shooting_sound = pygame.mixer.Sound("assets/audio/gun_shot.mp3")
        self.max_ammo = 8
        self.ammo = self.max_ammo
        self.damage = 10
        self.shot_delay = 350
        self.reload_time = 1000
        self.last_shot_time = 0
        self.is_reloading = False
        self.start_reload = 0

    def shoot(self, x: int, y: int, bullets: Group, all_sprites: Group) -> None:
        current_time = pygame.time.get_ticks()
        if (
            not self.is_reloading
            and self.ammo > 0
            and current_time - self.last_shot_time >= self.shot_delay
        ):
            self.last_shot_time = current_time
            self.ammo -= 1
            mouse_x, mouse_y = pygame.mouse.get_pos()
            bullet = Bullet(x, y, mouse_x, mouse_y)
            self.shooting_sound.play()
            bullets.add(bullet)
            all_sprites.add(bullet)

    def reload(self) -> None:
        if not self.is_reloading and self.ammo < self.max_ammo:
            self.is_reloading = True
            self.start_reload = pygame.time.get_ticks()

    def update(self) -> None:
        if self.is_reloading:
            current_time = pygame.time.get_ticks()
            if current_time - self.start_reload >= self.reload_time:
                self.ammo = self.max_ammo
                self.is_reloading = False

    def reset(self) -> None:
        self.ammo = self.max_ammo
        self.is_reloading = False
        self.last_shot_time = 0
        self.start_reload = 0


class Rifle(Weapon):
    def __init__(self) -> None:
        self.shooting_sound = pygame.mixer.Sound("assets/audio/rifle_shot.mp3")
        self.shooting_sound.set_volume(0.8)
        self.max_ammo = 30
        self.ammo = self.max_ammo
        self.damage = 20
        self.shot_delay = 150
        self.reload_time = 1500
        self.last_shot_time = 0
        self.is_reloading = False
        self.start_reload = 0

    def shoot(self, x: int, y: int, bullets: Group, all_sprites: Group) -> None:
        current_time = pygame.time.get_ticks()
        if (
            not self.is_reloading
            and self.ammo > 0
            and current_time - self.last_shot_time >= self.shot_delay
        ):
            self.last_shot_time = current_time
            self.ammo -= 1
            mouse_x, mouse_y = pygame.mouse.get_pos()
            bullet = Bullet(x, y, mouse_x, mouse_y)
            self.shooting_sound.play()
            bullets.add(bullet)
            all_sprites.add(bullet)

    def reload(self) -> None:
        if not self.is_reloading and self.ammo < self.max_ammo:
            self.is_reloading = True
            self.start_reload = pygame.time.get_ticks()

    def update(self) -> None:
        if self.is_reloading:
            current_time = pygame.time.get_ticks()
            if current_time - self.start_reload >= self.reload_time:
                self.ammo = self.max_ammo
                self.is_reloading = False

    def reset(self) -> None:
        self.ammo = self.max_ammo
        self.is_reloading = False
        self.last_shot_time = 0
        self.start_reload = 0


class Shotgun(Weapon):
    def __init__(self) -> None:
        self.shooting_sound = pygame.mixer.Sound("assets/audio/shotgun_shot.mp3")
        self.shooting_sound.set_volume(0.3)
        self.max_ammo = 6
        self.ammo = self.max_ammo
        self.damage = 30
        self.shot_delay = 450
        self.reload_time = 2000
        self.last_shot_time = 0
        self.is_reloading = False
        self.start_reload = 0

    def shoot(self, x: int, y: int, bullets: Group, all_sprites: Group) -> None:
        current_time = pygame.time.get_ticks()
        if (
            not self.is_reloading
            and self.ammo > 0
            and current_time - self.last_shot_time >= self.shot_delay
        ):
            self.last_shot_time = current_time
            self.ammo -= 1
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i in range(4):
                offset = (-1 if i % 2 == 0 else 1) * i * 10
                bullet = Bullet(x, y, mouse_x + offset, mouse_y)
                bullets.add(bullet)
                all_sprites.add(bullet)
            self.shooting_sound.play()

    def reload(self) -> None:
        if not self.is_reloading and self.ammo < self.max_ammo:
            self.is_reloading = True
            self.start_reload = pygame.time.get_ticks()

    def update(self) -> None:
        if self.is_reloading:
            current_time = pygame.time.get_ticks()
            if current_time - self.start_reload >= self.reload_time:
                self.ammo = self.max_ammo
                self.is_reloading = False

    def reset(self) -> None:
        self.ammo = self.max_ammo
        self.is_reloading = False
        self.last_shot_time = 0
        self.start_reload = 0
