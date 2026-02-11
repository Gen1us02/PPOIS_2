from enum import Enum


class SensorType(Enum):
    TEMPERATURE = "temperature"
    OPTICAL = "optical"
    GPS = "gps"
    DISTANCE = "distance"


class RobotStatus(Enum):
    WAITING = "waiting"
    ACTIVE = "active"
    CHARGING = "charging"
    INACTIVE = "inactive"
    MAINTENANCE = "maintenance"


class Direction(Enum):
    FORWARD = "forward"
    BACKWARD = "backward"
    LEFT = "left"
    RIGHT = "right"
