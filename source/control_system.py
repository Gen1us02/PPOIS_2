from typing import Any, Dict, List, Optional
from enums import Direction
from exceptions.exceptions import ControlSystemException, RobotException
from robot import Robot
from serializer import Serializer
from fabric import DefaultFabric
import json


class ControlSystem:
    def __init__(self, fabric: DefaultFabric) -> None:
        self.robot: Optional[Robot] = None
        self.fabric = fabric

    def save_condition(self) -> None:
        with open("condition.json", "w", encoding="utf-8") as file:
            json.dump(Serializer.convert_to_dict(self.robot), file)

    def load_condition(self) -> None:
        with open("condition.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        self.robot = Serializer.create_from_dict(data, self.fabric)

    def create_robot(self, name: str) -> None:
        if self.robot:
            raise ControlSystemException("Robot is already exists")

        self.robot = Robot(name)
        self.robot.add_sensor(self.fabric.create_temperature_sensor())
        self.robot.add_sensor(self.fabric.create_optical_sensor())
        self.robot.add_sensor(self.fabric.create_gps_sensor())
        self.robot.add_sensor(self.fabric.create_distance_sensor())

        for _ in range(2):
            self.robot.add_arm(self.fabric.create_arm())

        for _ in range(2):
            self.robot.add_leg(self.fabric.create_leg())

        self.robot.add_software("1.0.0", "Base Software")

    def charge_robot(self, amount) -> str:
        if not self.robot:
            raise ControlSystemException("Robot is not exists")

        try:
            self.robot.charging()
            res = self.robot.charge(amount)
            self.robot.wait()
            return res
        except RobotException as e:
            raise ControlSystemException("System error\n", exception=e)

    def move_robot(self, speed: int, direction: Direction, time: int) -> str:
        if not self.robot:
            raise ControlSystemException("Robot is not exists")

        try:
            self.robot.activate()
            res = self.robot.move(speed, direction, time)
            self.robot.wait()
            return res
        except RobotException as e:
            raise ControlSystemException("System error\n", exception=e)

    def arm_action(self, items: List[str]) -> str:
        if not self.robot:
            raise ControlSystemException("Robot is not exists")

        try:
            self.robot.activate()
            res = self.robot.arms_action(items)
            self.robot.wait()
            return res
        except RobotException as e:
            raise ControlSystemException("System error\n", exception=e)

    def get_status(self) -> Dict[str, Any]:
        if not self.robot:
            raise ControlSystemException("Robot is not exists")

        try:
            sensors_data = self.robot.get_sensors_data()
            robot_status = {
                "status": self.robot.status.name,
                "battery_level": self.robot.battery_level,
                "is_broken": self.robot.is_broken,
            }

            status_data = sensors_data | robot_status
            return status_data
        except RobotException as e:
            raise ControlSystemException("System error\n", exception=e)

    def maintanance(self) -> str:
        if not self.robot:
            raise ControlSystemException("Robot is not exists")

        try:
            self.robot.maintenance()
            self.robot.repair()
            self.robot.wait()
            return "Maintanance finish succesfully"
        except RobotException as e:
            raise ControlSystemException("System error\n", exception=e)

    def program_robot(self, version: str, name: str) -> str:
        if not self.robot:
            raise ControlSystemException("Robot is not exists")

        try:
            self.robot.maintenance()
            self.robot.update_software(version, name)
            self.robot.wait()
            return "Succesfully program robot"
        except RobotException as e:
            raise ControlSystemException("System error\n", exception=e)

    def teach_robot(self, data: List[str]) -> str:
        if not self.robot:
            raise ControlSystemException("Robot is not exists")

        self.robot.activate()
        res = self.robot.learn_data(data)
        self.robot.wait()
        return res
