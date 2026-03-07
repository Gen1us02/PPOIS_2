import math
import pygame
from pygame.mixer import Sound
from src.objects.player import Player
from src.utils.utils import Utils
from src.enums import EnemyType


class Enemy(pygame.sprite.Sprite):
    def __init__(
        self,
        health: int,
        speed: int,
        points: int,
        damage: int,
        cooldown: int,
        sound: Sound,
    ) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.health = health
        self.speed = speed
        self.points = points
        self.hit_damage = damage
        self.last_damage_time = 0
        self.cooldown = cooldown
        self.sound = sound

    @property
    def is_alive(self) -> bool:
        return self.health > 0

    def damage(self, player: Player) -> None:
        current_time = pygame.time.get_ticks()
        if current_time - self.last_damage_time >= self.cooldown:
            self.last_damage_time = current_time
            self.sound.play()
            player.health -= self.hit_damage
            return True
        
        return False


class Zombie(Enemy):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(
            50, 1, 50, 10, 1000, pygame.mixer.Sound("assets/audio/zombie_hit.mp3")
        )
        self.original_image = pygame.image.load(
            "assets/images/zombie.png"
        ).convert_alpha()
        self.type = EnemyType.ZOMBIE
        self.original_image = Utils.scale_image(self.original_image, 40)
        self.attack_image = pygame.image.load(
            "assets/images/zombie_attack.png"
        ).convert_alpha()
        self.attack_image = Utils.scale_image(self.attack_image, 40)
        self.attack_duration = 200
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle_offset = 270
        self.attack_duration = 200
        self.attack_end = 0

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)

    def damage(self, player: Player) -> None:
        if super().damage(player):
            self.attack_end = pygame.time.get_ticks() + self.attack_duration

    def update(self, *args, **kwargs) -> None:
        player_x, player_y = args
        dx = player_x - self.rect.centerx
        dy = player_y - self.rect.centery

        if dx != 0 or dy != 0:
            angle = math.degrees(math.atan2(-dy, dx))
            target_angle = angle - self.angle_offset
            current_time = pygame.time.get_ticks()
            if current_time < self.attack_end:
                original = self.attack_image
            else:
                original = self.original_image
                
            self.image = pygame.transform.rotate(original, target_angle)
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
