import math
import pygame
from pygame import Surface
from pygame.sprite import Group
from src.utils.utils import Utils
from src.objects.weapons import Gun


class Player(pygame.sprite.Sprite):
    def __init__(
        self,
        x: int,
        y: int,
    ) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.image.load("assets/images/player.png")
        self.original_image = Utils.scale_image(self.original_image, 50)
        self.weapon = Gun()
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle_offset = 90
        self.cooldown = 0
        self.max_health = 100
        self.health = self.max_health
        self.speed = 3

    def move(self, x: int, y: int) -> None:
        self.rect.x += x
        self.rect.y += y

    def draw(self, screen: Surface) -> None:
        bar_width = 64
        bar_height = 10
        bar_x = self.rect.centerx - bar_width // 2
        bar_y = self.rect.centery - bar_height - 30
        pygame.draw.rect(screen, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))
        health_percentage = self.health / self.max_health
        current_width = bar_width * health_percentage
        pygame.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, current_width, bar_height))
        screen.blit(self.image, self.rect)

    def shoot(self, bullets: Group, all_sprites) -> None:
        self.weapon.shoot(self.rect.centerx, self.rect.centery, bullets, all_sprites)

    def reset_weapon(self) -> None:
        self.weapon.reset()

    def reload(self) -> None:
        self.weapon.reload()

    @property
    def weapon_damage(self) -> int:
        return self.weapon.damage

    @property
    def is_alive(self) -> bool:
        return self.health > 0

    @property
    def ammo(self) -> int:
        return self.weapon.ammo

    def update(self, *args, **kwargs) -> None:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - self.rect.centerx
        dy = mouse_y - self.rect.centery

        if dx != 0 or dy != 0:
            angle = math.degrees(math.atan2(-dy, dx))
            target_angle = angle - self.angle_offset
            self.image = pygame.transform.rotate(self.original_image, target_angle)
            self.rect = self.image.get_rect(center=self.rect.center)

        self.weapon.update()
