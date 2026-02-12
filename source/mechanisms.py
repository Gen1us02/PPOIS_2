from .enums import Direction
from .device import Device
from exceptions.exceptions import MechanismException


class ArmMechanism(Device):
    def __init__(self) -> None:
        super().__init__()
        self.item = None

    def grab(self, item: str) -> str:
        if self.is_broken():
            raise MechanismException("Robot arm is broken")

        self.damage(5)

        if not self.item:
            self.item = item
            return f"Robot arm grab {item}"

        try:
            action = self.drop() + f" and grab {item}"
            self.item = item
            return action
        except MechanismException as e:
            raise e

    def drop(self) -> str:
        if not self.item:
            raise MechanismException("Robot arm without items")

        if self.is_broken():
            raise MechanismException("Robot arm is broken")

        self.damage(2)

        return f"Robot arm drop {self.item}"


class LegMechanism(Device):
    def __init__(self) -> None:
        super().__init__()
        self.speed = 0

    def move(self, direction: Direction, speed: int, time: int) -> str:
        if self.is_broken():
            raise MechanismException("Robot leg is broken")

        self.damage(5)

        self.speed = speed
        return f"Robot leg moved {direction.value} with speed {speed} m/s. It passed {self.speed * time} m"
