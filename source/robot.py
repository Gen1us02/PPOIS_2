import random
from typing import Any, Dict, List, Optional
from exceptions.exceptions import (
    BatteryException,
    MechanismException,
    RobotException,
    SensorException,
    SoftwareException,
)
from .mechanisms import ArmMechanism, LegMechanism
from .battery import Battery
from .software import Software
from .sensors import DistanceSensor, GPSSensor, OpticalSensor, Sensor
from .enums import Direction, RobotStatus


class Robot:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.status: RobotStatus = RobotStatus.INACTIVE
        self.sensors: List[Sensor] = []
        self.arms: List[ArmMechanism] = []
        self.legs: List[LegMechanism] = []
        self.battery: Battery = Battery()
        self.data: List[str] = []
        self.software: Optional[Software] = None

    def activate(self) -> None:
        if self.battery.battery_level <= 0:
            raise RobotException("Cannot activate – battery is empty")

        if self.is_broken:
            raise RobotException("Robot is broken")

        self.status = RobotStatus.ACTIVE

    def wait(self) -> None:
        self.status = RobotStatus.WAITING

    def maintenance(self) -> None:
        self.status = RobotStatus.MAINTENANCE

    def charging(self) -> None:
        self.status = RobotStatus.CHARGING

    def add_sensor(self, sensor: Sensor) -> None:
        self.sensors.append(sensor)

    def add_arm(self, arm: ArmMechanism) -> None:
        self.arms.append(arm)

    def add_leg(self, leg: LegMechanism) -> None:
        self.legs.append(leg)

    def update_software(self, version: str, name: str) -> None:
        if not self.software or self.software.name != name:
            self.software = Software(version, name)
        else:
            try:
                self.software.update(version)
            except SoftwareException as e:
                raise RobotException("Robot exception ", exception=e)

    def arms_action(self, items: List[str]) -> str:
        if not self.arms:
            raise RobotException("Robot without arms")

        if self.status != RobotStatus.ACTIVE:
            raise RobotException("Robot is not in active status")

        try:
            res = []
            for i, item in enumerate(items):
                res.append(self.arms[i % len(self.arms)].grab(item) + "\n")

            self.battery.discharge(10)

            for i, sensor in enumerate(self.sensors):
                if isinstance(sensor, OpticalSensor):
                    self.sensors[i].update_data(objects_count=len(items))

            return "".join(res)
        except (MechanismException, BatteryException) as e:
            raise RobotException("Robot error: ", exception=e)

    def move(self, direction: Direction, speed: int, time: int) -> str:
        if self.status != RobotStatus.ACTIVE:
            raise RobotException("Robot is not in active status")

        try:
            res = []
            for i, leg in enumerate(self.legs):
                res.append(leg.move(direction, speed, time) + "\n")

            self.battery.discharge(10)

            for i, sensor in enumerate(self.sensors):
                if isinstance(sensor, GPSSensor):
                    self.sensors[i].update_data(direction, speed * time)

                if isinstance(sensor, DistanceSensor):
                    self.sensors[i].update_data(speed * time)

            return "".join(res)
        except (MechanismException, BatteryException) as e:
            raise RobotException("Robot error: ", exception=e)

    def learn_data(self, new_data: List[str]) -> str:
        if self.status != RobotStatus.ACTIVE:
            raise RobotException("Robot is not in active status")

        self.data.extend(new_data)
        return "Robot successfuly learn new data"

    def speak(self) -> str:
        if self.status != RobotStatus.ACTIVE:
            RobotException("Robot is not in active status")

        if not self.data:
            raise RobotException("Robot dont learned any data")

        return f"Hello, I'm robot {self.name} and i learned some phrases. For example: {random.choice(self.data)}"

    def charge(self, amount: int) -> str:
        try:
            self.battery.charge(amount)
            return f"Battery is charged for {self.battery.battery_level}"
        except BatteryException as e:
            raise RobotException("Robot error: ", exception=e)

    @property
    def battery_level(self) -> int:
        return self.battery.battery_level

    @property
    def is_broken(self) -> bool:
        return (
            any(sensor.is_broken() for sensor in self.sensors)
            or any(arm.is_broken() for arm in self.arms)
            or any(leg.is_broken() for leg in self.legs)
        )

    def get_sensors_data(self) -> Dict[str, Any]:
        try:
            data = {}
            for sensor in self.sensors:
                data.update(sensor.read_data())

            return data
        except SensorException as e:
            raise RobotException("Robot error: ", exception=e)

    def repair(self) -> None:
        for i in range(len(self.arms)):
            self.arms[i].repair()

        for i in range(len(self.legs)):
            self.legs[i].repair()

        for i in range(len(self.sensors)):
            self.sensors[i].repair()
