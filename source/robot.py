import random
from typing import Any, Dict, List, Optional
from exceptions.exceptions import (
    BatteryException,
    MechanismException,
    RobotException,
    SensorException,
)
from mechanisms import ArmMechanism, LegMechanism
from battery import Battery
from software import Software
from sensors import DistanceSensor, GPSSensor, OpticalSensor, Sensor, TemperatureSensor
from enums import Direction, RobotStatus


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

    def add_sensor(self, sensor: Sensor) -> None:
        self.sensors.append(sensor)

    def add_arm(self, arm: ArmMechanism) -> None:
        self.arms.append(arm)

    def add_leg(self, leg: LegMechanism) -> None:
        self.legs.append(leg)

    def add_software(self, software: Software) -> None:
        self.software = software

    def arms_action(self, items: List[str]) -> str:
        if self.status != RobotStatus.ACTIVE:
            raise RobotException("Robot is not in active status")

        try:
            res = []
            for i, item in enumerate(items):
                res.append(self.arms[i].grab(item) + "\n")
                self.arms[i].damage(5)

            self.battery.discharge(10)

            for i, sensor in enumerate(self.sensors):
                if isinstance(sensor, OpticalSensor):
                    self.sensors[i].update_data(objects_count=len(items))

            return "".join(res)
        except (MechanismException, BatteryException) as e:
            raise RobotException("Robot error: ", exception=e)

    def move(self, speed: int, direction: Direction, time: int) -> str:
        if self.status != RobotStatus.ACTIVE:
            raise RobotException("Robot is not in active status")

        try:
            res = []
            for i, leg in enumerate(self.legs):
                res.append(leg.move(direction, speed, time) + "\n")
                self.legs[i].damage(5)

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
        if not self.data:
            raise RobotException("Robot dont learned any data")

        return f"Hello, I'm robot {self.name} and i learned some phrases. For example: {random.choice(self.data)}"

    def charge(self, amount: int) -> str:
        try:
            self.battery.charge(amount)
            return f"Battery is charged for {self.battery.battery_level}"
        except BatteryException as e:
            raise RobotException("Robot error: ", exception=e)

    def get_sensors_data(self) -> Dict[str, Any]:
        try:
            data = {}
            for i, sensor in enumerate(self.sensors):
                data.update(sensor.read_data())
                self.sensors[i].damage(5)

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

    def convert_to_dict(self) -> None:
        return {
            "name": self.name,
            "status": self.status,
            "battery": self.battery.battery_level,
            "sensors": [
                {"type": s.type.name, "is_active": s.is_active, "data": s.read_data()}
                for s in self.sensors
            ],
            "arms": len(self.arms),
            "legs": len(self.legs),
            "software": {"name": self.software.name, "version": self.software.version},
        }

    @classmethod
    def create_from_dict(cls, data: Dict[str, Any]) -> None:
        robot = cls(data["name"])
        robot.status = RobotStatus[data["status"]]
        robot.battery = Battery(data["battery_level"])

        software_data = data["software"]
        robot.add_software(Software(software_data["version"], software_data["name"]))

        robot.data = data["data"]

        for _ in range(data["arms"]):
            robot.add_arm(ArmMechanism())

        for _ in range(data["legs"]):
            robot.add_leg(LegMechanism())

        for sensor in data["sensors"]:
            if sensor["type"] == "temperature":
                sensor_obj = TemperatureSensor(**sensor["data"])
            elif sensor["type"] == "optical":
                sensor_obj = OpticalSensor(**sensor["data"])
            elif sensor["type"] == "gps":
                sensor_obj = GPSSensor(**sensor["data"])
            else:
                sensor_obj = DistanceSensor(**sensor["data"])

            robot.add_sensor(sensor_obj)

        return robot
