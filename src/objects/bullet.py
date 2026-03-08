import pygame
import math
from src.utils.utils import Utils


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, target_x: int, target_y: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/images/bullet.png")
        self.image = Utils.scale_image(self.image, 10)
        self.rect = self.image.get_rect()
        self.speed = 15
        dx = target_x - x
        dy = target_y - y
        distance = math.hypot(dx, dy)
        if distance != 0:
            self.dx = dx / distance
            self.dy = dy / distance
        else:
            self.dx, self.dy = 0, 0

        self.rect.center = (x, y)

    def update(self, *args, **kwargs) -> None:
        self.rect.x += self.dx * self.speed
        self.rect.y += self.dy * self.speed

        screen_rect = pygame.display.get_surface().get_rect()
        if not screen_rect.colliderect(self.rect):
            self.kill()
