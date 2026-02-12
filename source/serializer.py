from typing import Any, Dict
from .battery import Battery
from .enums import RobotStatus
from .robot import Robot
from .fabric import Fabric


class Serializer:
    @staticmethod
    def convert_to_dict(robot: Robot) -> Dict[str, Any]:
        return {
            "name": robot.name,
            "status": robot.status.name,
            "battery": robot.battery.battery_level,
            "sensors": [
                {
                    "type": sensor.sensor_type.name,
                    "is_active": sensor.is_active,
                    "data": sensor.read_data(),
                    "damage": sensor.curr_damage,
                }
                for sensor in robot.sensors
            ],
            "arms": [{"damage": arm.curr_damage} for arm in robot.arms],
            "legs": [{"damage": leg.curr_damage} for leg in robot.legs],
            "software": {"name": robot.software.name, "version": robot.software.version}
            if robot.software
            else None,
            "data": robot.data
        }

    @staticmethod
    def create_from_dict(data: Dict[str, Any], fabric: Fabric):
        robot = Robot(data["name"])
        robot.status = RobotStatus[data["status"]]
        robot.battery = Battery(data["battery"])

        software_data = data["software"]
        robot.update_software(software_data["version"], software_data["name"])

        robot.data = data["data"]

        for arm in data["arms"]:
            arm_obj = fabric.create_arm()
            arm_obj.curr_damage = arm["damage"]
            robot.add_arm(arm_obj)

        for leg in data["legs"]:
            leg_obj = fabric.create_leg()
            leg_obj.curr_damage = leg["damage"]
            robot.add_leg(leg_obj)

        for sensor in data["sensors"]:
            if sensor["type"] == "TEMPERATURE":
                sensor_obj = fabric.create_temperature_sensor(**sensor["data"])
            elif sensor["type"] == "OPTICAL":
                sensor_obj = fabric.create_optical_sensor(**sensor["data"])
            elif sensor["type"] == "GPS":
                sensor_obj = fabric.create_gps_sensor(**sensor["data"])
            else:
                sensor_obj = fabric.create_distance_sensor(**sensor["data"])

            sensor_obj.is_active = sensor["is_active"]
            sensor_obj.curr_damage = sensor["damage"]

            robot.add_sensor(sensor_obj)

        return robot
