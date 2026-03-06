from typing import Optional
from abc import ABC, abstractmethod
from src.enums import EnemyType
from src.objects.enemies import Enemy, Zombie, Spider, Lizard, WildDog, Thug


class Fabric(ABC):
    @abstractmethod
    def create(self, type, *args) -> None:
        pass


class EnemyFabric(Fabric):
    def create(self, type: EnemyType, *args) -> Optional[Enemy]:
        if type == EnemyType.ZOMBIE:
            return Zombie(*args)
        elif type == EnemyType.SPIDER:
            return Spider(*args)
        elif type == EnemyType.LIZARD:
            return Lizard(*args)
        elif type == EnemyType.WILD_DOG:
            return WildDog(*args)
        elif type == EnemyType.THUG:
            return Thug(*args)
        else:
            return None
