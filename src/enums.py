from enum import Enum


class States(Enum):
    MENU = "menu"
    GAME = "game"
    LEADERS = "leaders"
    RULES = "rules"
    GAME_OVER = "game_over"
    NAME_INPUT = "name_input"
    EXIT = "exit"
    START = "start"
    WIN = "win"


class EnemyType(Enum):
    ZOMBIE = "zombie"
    SPIDER = "spider"
    LIZARD = "lizard"
    WILD_DOG = "wild_dog"
    THUG = "thug"
