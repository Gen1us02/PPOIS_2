from abc import ABC, abstractmethod
import pygame
from pygame import Surface
from src.objects.weapons import Weapon, Gun, Rifle, Shotgun
from src.objects.player import Player
from src.utils.utils import Utils


class Bonus(ABC, pygame.sprite.Sprite):
    def __init__(self, time: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.time = time

    def set_center(self, x: int, y: int) -> None:
        self.rect.center = (x, y)

    def draw(self, screen: Surface) -> None:
        screen.blit(self.image, self.rect)

    def update(self) -> None:
        current_time = pygame.time.get_ticks()
        if current_time - self.spawn_time > self.time:
            self.kill()
        elif current_time - self.spawn_time > self.time - 5000:
            if (current_time // 200) % 2 == 0:
                self.image.set_alpha(80)
            else:
                self.image.set_alpha(255)

    @abstractmethod
    def action(self, player: Player) -> None:
        pass


class FirstAid(Bonus):
    def __init__(self) -> None:
        super().__init__(15000)
        self.image = pygame.image.load("assets/images/first_aid.png")
        self.image = Utils.scale_image(self.image, 64)
        self.rect = self.image.get_rect()
        self.spawn_time = pygame.time.get_ticks()

    def action(self, player) -> None:
        player.health += 25
        if player.health > 100:
            player.health = 100


class SpeedBoost(Bonus):
    def __init__(self) -> None:
        super().__init__(15000)
        self.image = pygame.image.load("assets/images/speed_boost.png")
        self.image = Utils.scale_image(self.image, 64)
        self.rect = self.image.get_rect()
        self.spawn_time = pygame.time.get_ticks()

    def action(self, player) -> None:
        if not player.is_double_speed:
            player.is_double_speed = True
            player.current_speed *= 2

        player.double_speed_time = pygame.time.get_ticks()


class WeaponBox(Bonus):
    def __init__(self, weapon: Weapon, box_image: Surface) -> None:
        super().__init__(15000)
        self.weapon = weapon
        self.image = box_image

    def action(self, player) -> None:
        player.weapon = self.weapon


class GunBox(WeaponBox):
    def __init__(self) -> None:
        gun = Gun()
        image = pygame.image.load("assets/images/gun_box.png")
        super().__init__(gun, image)
        self.image = Utils.scale_image(self.image, 40)
        self.rect = self.image.get_rect()
        self.spawn_time = pygame.time.get_ticks()


class RifleBox(WeaponBox):
    def __init__(self) -> None:
        gun = Rifle()
        image = pygame.image.load("assets/images/rifle_box.png")
        super().__init__(gun, image)
        self.image = Utils.scale_image(self.image, 40)
        self.rect = self.image.get_rect()
        self.spawn_time = pygame.time.get_ticks()


class ShotgunBox(WeaponBox):
    def __init__(self) -> None:
        gun = Shotgun()
        image = pygame.image.load("assets/images/shotgun_box.png")
        super().__init__(gun, image)
        self.image = Utils.scale_image(self.image, 40)
        self.rect = self.image.get_rect()
        self.spawn_time = pygame.time.get_ticks()
