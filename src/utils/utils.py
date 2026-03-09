import json
from typing import Any, Dict, List, Tuple
from pygame import Surface
import pygame


class Utils:
    @staticmethod
    def load_players(filename: str) -> List[Tuple[str, int]]:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        players = []
        for player in data:
            players.append((player["name"], player["score"]))

        players = sorted(players, key=lambda x: -x[1])
        return players

    @staticmethod
    def save_leaderboard(filename: str, leaderboard):
        data = []
        for leader in leaderboard:
            data.append({"name": leader[0], "score": leader[1]})

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def is_highscore(score, leaderboard):
        if len(leaderboard) == 0:
            return True

        return score > leaderboard[0][1]

    @staticmethod
    def add_score(name, score, leaderboard):
        leaderboard.append((name, score))
        leaderboard.sort(key=lambda x: x[1], reverse=True)
        return leaderboard[:10]

    @staticmethod
    def load_rules(filename: str) -> List[str]:
        with open(filename, "r", encoding="utf-8") as file:
            rules = file.readlines()

        return [string.strip("\n") for string in rules]

    @staticmethod
    def load_waves(filename: str) -> List[Dict[str, Any]]:
        with open(filename, "r", encoding="utf-8") as file:
            waves = json.load(file)

        return waves["waves"]

    @staticmethod
    def scale_image(image: Surface, target_width: int):
        original_width, original_height = image.get_size()
        scale_factor = target_width / original_width
        new_height = int(original_height * scale_factor)
        return pygame.transform.smoothscale(image, (target_width, new_height))

    @staticmethod
    def update_sound_and_mouse(music_path: str, volume: float = 0.5) -> None:
        pygame.mouse.set_visible(True)
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)
        
    @staticmethod
    def create_all_bonuses() -> Tuple[Any]:
        from src.objects.bonuses import GunBox, RifleBox, ShotgunBox, FirstAid, SpeedBoost
        first_aid = FirstAid()
        speed_boost = SpeedBoost()
        gun_box = GunBox()
        rifle_box = RifleBox()
        shotgun_box = ShotgunBox()
            
        return first_aid, speed_boost, gun_box, rifle_box, shotgun_box
        
