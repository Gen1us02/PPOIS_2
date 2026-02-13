from exceptions.exceptions import BatteryException


class Battery:
    def __init__(self, battery_level: int = 100) -> None:
        self.battery_level = battery_level

    def charge(self, amount: int) -> None:
        if amount <= 0:
            raise BatteryException("Невалидный заряд (заряд должен быть больше 0)")

        if self.battery_level == 100:
            raise BatteryException("Батарея полностью заряжена")

        if self.battery_level + amount >= 100:
            self.battery_level = 100
        else:
            self.battery_level += amount

    def discharge(self, amount: int) -> None:
        if amount <= 0:
            raise BatteryException("Невалидный заряд (заряд должен быть больше 0)")

        if self.battery_level == 0:
            raise BatteryException("Батарея полностью заряжена")

        if self.battery_level - amount <= 0:
            self.battery_level = 0
        else:
            self.battery_level -= amount
