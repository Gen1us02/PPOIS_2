from enums import Direction
from device import Device
from exceptions.exceptions import MechanismException


class ArmMechanism(Device):
    def __init__(self) -> None:
        self.item = None

    def grab(self, item: str) -> str:
        if self.is_broken():
            raise MechanismException("Robot arm is broken")

        if not self.item:
            return f"Robot arm grab {item}"

        action = self.drop() + "and grab {item}"
        self.item = item
        return action

    def drop(self) -> str:
        if self.is_broken():
            raise MechanismException("Robot arm is broken")

        return f"Robot arm drop {self.item}"


class LegMechanism(Device):
    def __init__(self) -> None:
        self.speed = 0

    def move(self, direction: Direction, speed: int, time: int) -> str:
        if self.is_broken():
            raise MechanismException("Robot leg is broken")

        self.speed += speed
        return f"Robot leg moved {direction.name} with speed {speed} m/s. It passed {self.speed * time} m"
