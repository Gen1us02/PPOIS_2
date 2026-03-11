import math
import random
from typing import Optional
import pygame
from pygame.mixer import Sound
from src.objects.player import Player
from src.utils.utils import Utils
from src.enums import EnemyType
from src.objects.bonuses import Bonus
import os


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
            "assets/images/zombie/zombie.png"
        ).convert_alpha()
        self.type = EnemyType.ZOMBIE
        self.original_image = Utils.scale_image(self.original_image, 40)
        self.move_images = []
        for i in range(len(os.listdir("assets/images/zombie/zombie_move"))):
            move_image = pygame.image.load(
                f"assets/images/zombie/zombie_move/zombie_move_{i}.png"
            ).convert_alpha()
            move_image = Utils.scale_image(move_image, 40)
            self.move_images.append(move_image)
        self.attack_images = []
        for i in range(len(os.listdir("assets/images/zombie/zombie_attack"))):
            attack_image = pygame.image.load(
                f"assets/images/zombie/zombie_attack/zombie_attack_{i}.png"
            ).convert_alpha()
            attack_image = Utils.scale_image(attack_image, 40)
            self.attack_images.append(attack_image)
        self.dead_picture = pygame.image.load(
            "assets/images/zombie/dead_zombie.png"
        ).convert_alpha()
        self.dead_picture = Utils.scale_image(self.dead_picture, 40)
        self.move_image = 0
        self.change_move_frame = 0
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
                elapsed = current_time - (self.attack_end - self.attack_duration)
                progress = elapsed / self.attack_duration
                frame = int(progress * len(self.attack_images))
                if frame >= len(self.attack_images):
                    frame = len(self.attack_images) - 1
                original = self.attack_images[frame]
            else:
                current_time = pygame.time.get_ticks()
                if current_time - self.change_move_frame >= 300:
                    self.change_move_frame = current_time
                    self.move_image = (self.move_image + 1) % len(self.move_images)
                original = self.move_images[self.move_image]

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
            "assets/images/spider/spider.png"
        ).convert_alpha()
        self.type = EnemyType.SPIDER
        self.original_image = Utils.scale_image(self.original_image, 50)
        self.dead_picture = pygame.image.load(
            "assets/images/spider/dead_spider.png"
        ).convert_alpha()
        self.move_images = []
        for i in range(len(os.listdir("assets/images/spider/spider_move"))):
            move_image = pygame.image.load(
                f"assets/images/spider/spider_move/spider_move_{i}.png"
            ).convert_alpha()
            move_image = Utils.scale_image(move_image, 50)
            self.move_images.append(move_image)
        self.attack_images = []
        for i in range(len(os.listdir("assets/images/spider/spider_attack"))):
            attack_image = pygame.image.load(
                f"assets/images/spider/spider_attack/spider_attack_{i}.png"
            ).convert_alpha()
            attack_image = Utils.scale_image(attack_image, 50)
            self.attack_images.append(attack_image)
        self.dead_picture = pygame.image.load(
            "assets/images/spider/dead_spider.png"
        ).convert_alpha()
        self.dead_picture = Utils.scale_image(self.dead_picture, 40)
        self.image = self.original_image
        self.move_image = 0
        self.change_move_frame = 0
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
                elapsed = current_time - (self.attack_end - self.attack_duration)
                progress = elapsed / self.attack_duration
                frame = int(progress * len(self.attack_images))
                if frame >= len(self.attack_images):
                    frame = len(self.attack_images) - 1
                original = self.attack_images[frame]
            else:
                current_time = pygame.time.get_ticks()
                if current_time - self.change_move_frame >= 300:
                    self.change_move_frame = current_time
                    self.move_image = (self.move_image + 1) % len(self.move_images)
                original = self.move_images[self.move_image]

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
            "assets/images/lizard/lizard.png"
        ).convert_alpha()
        self.type = EnemyType.LIZARD
        self.original_image = Utils.scale_image(self.original_image, 60)
        self.move_images = []
        for i in range(len(os.listdir("assets/images/lizard/lizard_move"))):
            move_image = pygame.image.load(
                f"assets/images/lizard/lizard_move/lizard_move_{i}.png"
            ).convert_alpha()
            move_image = Utils.scale_image(move_image, 75)
            self.move_images.append(move_image)
        self.attack_images = []
        for i in range(len(os.listdir("assets/images/lizard/lizard_attack"))):
            attack_image = pygame.image.load(
                f"assets/images/lizard/lizard_attack/lizard_attack_{i}.png"
            ).convert_alpha()
            attack_image = Utils.scale_image(attack_image, 75)
            self.attack_images.append(attack_image)
        self.dead_picture = pygame.image.load(
            "assets/images/lizard/dead_lizard.png"
        ).convert_alpha()
        self.dead_picture = Utils.scale_image(self.dead_picture, 60)
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle_offset = 90
        self.current_attack = 0
        self.attack_duration = 1000
        self.move_image = 0
        self.change_move_frame = 0
        self.attack_frame_time = 0
        self.attack_end = 0

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)

    def damage(self, player: Player) -> None:
        if super().damage(player):
            self.attack_end = pygame.time.get_ticks() + self.attack_duration
            self.attack_frame_index = 0
            self.attack_frame_time = pygame.time.get_ticks()

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
                elapsed = current_time - (self.attack_end - self.attack_duration)
                progress = elapsed / self.attack_duration
                frame = int(progress * len(self.attack_images))
                if frame >= len(self.attack_images):
                    frame = len(self.attack_images) - 1
                original = self.attack_images[frame]
            else:
                current_time = pygame.time.get_ticks()
                if current_time - self.change_move_frame >= 150:
                    self.change_move_frame = current_time
                    self.move_image = (self.move_image + 1) % len(self.move_images)
                original = self.move_images[self.move_image]

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
            "assets/images/wild_dog/wild_dog.png"
        ).convert_alpha()
        self.type = EnemyType.WILD_DOG
        self.original_image = Utils.scale_image(self.original_image, 64)
        self.move_images = []
        for i in range(len(os.listdir("assets/images/wild_dog/wild_dog_move"))):
            move_image = pygame.image.load(
                f"assets/images/wild_dog/wild_dog_move/wild_dog_move_{i}.png"
            ).convert_alpha()
            move_image = Utils.scale_image(move_image, 64)
            self.move_images.append(move_image)
        self.attack_images = []
        for i in range(len(os.listdir("assets/images/wild_dog/wild_dog_attack"))):
            attack_image = pygame.image.load(
                f"assets/images/wild_dog/wild_dog_attack/wild_dog_attack_{i}.png"
            ).convert_alpha()
            attack_image = Utils.scale_image(attack_image, 64)
            self.attack_images.append(attack_image)
        self.dead_picture = pygame.image.load(
            "assets/images/wild_dog/dead_dog.png"
        ).convert_alpha()
        self.dead_picture = Utils.scale_image(self.dead_picture, 64)
        self.image = self.original_image
        self.move_image = 0
        self.change_move_frame = 0
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
                elapsed = current_time - (self.attack_end - self.attack_duration)
                progress = elapsed / self.attack_duration
                frame = int(progress * len(self.attack_images))
                if frame >= len(self.attack_images):
                    frame = len(self.attack_images) - 1
                original = self.attack_images[frame]
            else:
                current_time = pygame.time.get_ticks()
                if current_time - self.change_move_frame >= 300:
                    self.change_move_frame = current_time
                    self.move_image = (self.move_image + 1) % len(self.move_images)
                original = self.move_images[self.move_image]

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
            "assets/images/dead_thug.png"
        ).convert_alpha()
        self.dead_picture = Utils.scale_image(self.dead_picture, 64)
        self.attack_image = Utils.scale_image(self.attack_image, 64)
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
