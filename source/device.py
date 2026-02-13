from exceptions.exceptions import DeviceException


class Device:
    def __init__(self) -> None:
        self.curr_damage = 0

    def is_broken(self) -> bool:
        return self.curr_damage == 100

    def damage(self, damage_val: int) -> None:
        if damage_val <= 0:
            raise DeviceException(
                "Невалидное значение урона(урон должен быть больше 0)"
            )

        if self.curr_damage >= 100:
            raise DeviceException("Девайс сломан")

        self.curr_damage += damage_val
        if self.curr_damage > 100:
            self.curr_damage = 100

    def repair(self) -> None:
        self.curr_damage = 0
