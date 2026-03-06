import math
import pygame
from src.utils.utils import Utils
from src.enums import EnemyType


class Enemy(pygame.sprite.Sprite):
    def __init__(self, health: int, speed: int, points: int, damage: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.health = health
        self.speed = speed
        self.points = points
        self.damage = damage

    @property
    def is_alive(self) -> bool:
        return self.health > 0


class Zombie(Enemy):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(50, 1, 50, 10)
        self.original_image = pygame.image.load(
            "assets/images/zombie.png"
        ).convert_alpha()
        self.type = EnemyType.ZOMBIE
        self.original_image = Utils.scale_image(self.original_image, 40)
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle_offset = 270

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)

    def update(self, *args, **kwargs) -> None:
        player_x, player_y = args
        dx = player_x - self.rect.centerx
        dy = player_y - self.rect.centery

        if dx != 0 or dy != 0:
            angle = math.degrees(math.atan2(-dy, dx))
            target_angle = angle - self.angle_offset
            self.image = pygame.transform.rotate(self.original_image, target_angle)
            self.rect = self.image.get_rect(center=self.rect.center)

            distance = math.hypot(dx, dy)
            if distance != 0:
                step_x = (dx / distance) * self.speed
                step_y = (dy / distance) * self.speed
                self.rect.x += step_x
                self.rect.y += step_y


class Spider(Enemy):
    pass


class Lizard(Enemy):
    pass


class WildDog(Enemy):
    pass


class Thug(Enemy):
    pass
