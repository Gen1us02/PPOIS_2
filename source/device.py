from exceptions.exceptions import DeviceException


class Device:
    def __init__(self) -> None:
        self.curr_damage = 0

    def condition(self) -> int:
        return self.curr_damage

    def is_broken(self) -> bool:
        return self.curr_damage == 100

    def damage(self, damage: int) -> None:
        if self.curr_damage >= 100:
            raise DeviceException("Device is broken")

        self.curr_damage += damage
        if self.curr_damage > 100:
            self.curr_damage = 100

    def repair(self) -> None:
        self.curr_damage = 0
