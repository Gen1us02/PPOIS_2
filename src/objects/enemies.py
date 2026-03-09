import math
import random
from typing import Optional
import pygame
from pygame.mixer import Sound
from src.objects.player import Player
from src.utils.utils import Utils
from src.enums import EnemyType
from src.objects.bonuses import Bonus


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
        self.weights = [75, 5, 5, 5, 5, 5]

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
    
    def spawn_bonus(self) -> Optional[Bonus]:
        bonuses = [None]
        bonuses.extend(Utils.create_all_bonuses())
        bonus = random.choices(bonuses, weights=self.weights, k=1)
        bonus = bonus[0]
        if bonus:
            bonus.set_center(self.rect.x, self.rect.y)
            return bonus
        
        return None


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
        self.dead_picture = pygame.image.load(
            "assets/images/dead_zombie.png"
        ).convert_alpha()
        self.dead_picture = Utils.scale_image(self.dead_picture, 40)
        self.attack_image = Utils.scale_image(self.attack_image, 40)
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
        if not self.is_alive:
            return

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

    def dead(self) -> None:
        if not self.is_alive:
            self.is_dead = True
            self.image = self.dead_picture
            self.rect = self.image.get_rect(center=self.rect.center)
            self.speed = 0
            self.hit_damage = 0


class Spider(Enemy):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(
            100, 2, 100, 15, 700, pygame.mixer.Sound("assets/audio/zombie_hit.mp3")
        )
        self.original_image = pygame.image.load(
            "assets/images/spider.png"
        ).convert_alpha()
        self.type = EnemyType.SPIDER
        self.original_image = Utils.scale_image(self.original_image, 50)
        self.attack_image = pygame.image.load(
            "assets/images/zombie_attack.png"
        ).convert_alpha()
        self.dead_picture = pygame.image.load(
            "assets/images/dead_zombie.png"
        ).convert_alpha()
        self.dead_picture = Utils.scale_image(self.dead_picture, 40)
        self.attack_image = Utils.scale_image(self.attack_image, 40)
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle_offset = 90
        self.attack_duration = 200
        self.attack_end = 0

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)

    def damage(self, player: Player) -> None:
        if super().damage(player):
            self.attack_end = pygame.time.get_ticks() + self.attack_duration

    def update(self, *args, **kwargs) -> None:
        if not self.is_alive:
            return

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

    def dead(self) -> None:
        if not self.is_alive:
            self.is_dead = True
            self.image = self.dead_picture
            self.rect = self.image.get_rect(center=self.rect.center)
            self.speed = 0
            self.hit_damage = 0


class Lizard(Enemy):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(
            120, 2, 150, 15, 500, pygame.mixer.Sound("assets/audio/zombie_hit.mp3")
        )
        self.original_image = pygame.image.load(
            "assets/images/lizard.png"
        ).convert_alpha()
        self.type = EnemyType.LIZARD
        self.original_image = Utils.scale_image(self.original_image, 60)
        self.attack_image = pygame.image.load(
            "assets/images/zombie_attack.png"
        ).convert_alpha()
        self.dead_picture = pygame.image.load(
            "assets/images/dead_zombie.png"
        ).convert_alpha()
        self.dead_picture = Utils.scale_image(self.dead_picture, 60)
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle_offset = 90
        self.attack_duration = 200
        self.attack_end = 0

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)

    def damage(self, player: Player) -> None:
        if super().damage(player):
            self.attack_end = pygame.time.get_ticks() + self.attack_duration

    def update(self, *args, **kwargs) -> None:
        if not self.is_alive:
            return

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

    def dead(self) -> None:
        if not self.is_alive:
            self.is_dead = True
            self.image = self.dead_picture
            self.rect = self.image.get_rect(center=self.rect.center)
            self.speed = 0
            self.hit_damage = 0


class WildDog(Enemy):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(
            100, 4, 250, 10, 600, pygame.mixer.Sound("assets/audio/zombie_hit.mp3")
        )
        self.original_image = pygame.image.load(
            "assets/images/wild_dog.png"
        ).convert_alpha()
        self.type = EnemyType.WILD_DOG
        self.original_image = Utils.scale_image(self.original_image, 50)
        self.attack_image = pygame.image.load(
            "assets/images/zombie_attack.png"
        ).convert_alpha()
        self.dead_picture = pygame.image.load(
            "assets/images/dead_zombie.png"
        ).convert_alpha()
        self.dead_picture = Utils.scale_image(self.dead_picture, 40)
        self.attack_image = Utils.scale_image(self.attack_image, 40)
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
        if not self.is_alive:
            return

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

    def dead(self) -> None:
        if not self.is_alive:
            self.is_dead = True
            self.image = self.dead_picture
            self.rect = self.image.get_rect(center=self.rect.center)
            self.speed = 0
            self.hit_damage = 0


class Thug(Enemy):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(
            500, 1, 1000, 50, 2000, pygame.mixer.Sound("assets/audio/zombie_hit.mp3")
        )
        self.original_image = pygame.image.load(
            "assets/images/thug.png"
        ).convert_alpha()
        self.type = EnemyType.SPIDER
        self.original_image = Utils.scale_image(self.original_image, 80)
        self.attack_image = pygame.image.load(
            "assets/images/zombie_attack.png"
        ).convert_alpha()
        self.dead_picture = pygame.image.load(
            "assets/images/dead_zombie.png"
        ).convert_alpha()
        self.dead_picture = Utils.scale_image(self.dead_picture, 40)
        self.attack_image = Utils.scale_image(self.attack_image, 40)
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
        if not self.is_alive:
            return

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

    def dead(self) -> None:
        if not self.is_alive:
            self.is_dead = True
            self.image = self.dead_picture
            self.rect = self.image.get_rect(center=self.rect.center)
            self.speed = 0
            self.hit_damage = 0
