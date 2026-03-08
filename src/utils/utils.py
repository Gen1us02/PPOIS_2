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
    def load_rules(filename: str) -> List[str]:
        with open(filename, "r", encoding="utf-8") as file:
            rules = file.readlines()

        return [string.strip("\n") for string in rules]
    
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
