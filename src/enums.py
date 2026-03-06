from enum import Enum


class States(Enum):
    MENU = "menu"
    GAME = "game"
    LEADERS = "leaders"
    RULES = "rules"
    EXIT = "exit"
    START = "start"


class EnemyType(Enum):
    ZOMBIE = "zombie"
    SPIDER = "spider"
    LIZARD = "lizard"
    WILD_DOG = "wild_dog"
    THUG = "thug"
