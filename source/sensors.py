from abc import ABC, abstractmethod
from typing import Any, Dict
from enums import Direction, SensorType
from device import Device
from exceptions.exceptions import SensorException


class Sensor(Device, ABC):
    def __init__(self, sensor_type: SensorType):
        super().__init__()
        self.sensor_type = sensor_type
        self.is_active = True

    @abstractmethod
    def read_data(self) -> dict:
        pass

    @abstractmethod
    def update_data(self, **kwargs):
        pass

    def activate(self) -> None:
        self.is_active = True

    def deactivate(self) -> None:
        self.is_active = False

    def is_available(self) -> bool:
        return self.is_active and not self.is_broken()


class TemperatureSensor(Sensor):
    def __init__(self, temperature: int = "27", unit: str = "C"):
        super().__init__(SensorType.TEMPERATURE)
        self.temperature = temperature
        self.unit = unit

    def read_data(self) -> Dict[str, Any]:
        if not self.is_available():
            raise SensorException("Sensor is not available")

        return {"temperature": self.temperature, "temp_unit": self.unit}

    def update_data(self, temperature: int = None, unit: str = "C"):
        if temperature:
            self.temperature = temperature

        if unit:
            self.unit = unit


class OpticalSensor(Sensor):
    def __init__(self, objects_count: int = 0) -> None:
        super().__init__(SensorType.OPTICAL)
        self.objects_count = objects_count

    def read_data(self) -> Dict[str, Any]:
        if not self.is_available():
            raise SensorException("Sensor is not available")

        return {"objects_count": self.objects_count}

    def update_data(self, objects_count: int = None):
        if objects_count:
            self.objects_count = objects_count


class DistanceSensor(Sensor):
    def __init__(self, distance: int = 0, unit: str = "m") -> None:
        super().__init__(SensorType.DISTANCE)
        self.distance = distance
        self.unit = unit

    def read_data(self) -> Dict[str, Any]:
        if not self.is_available():
            raise SensorException("Sensor is not available")

        return {"distance": self.distance, "dist_unit": self.unit}

    def update_data(self, distance: int = None, unit: str = "m"):
        if distance:
            self.distance = distance

        if unit:
            self.unit = unit


class GPSSensor(Sensor):
    def __init__(self, lotitude: float = 53.9, longtitude: float = 27.34) -> None:
        super().__init__(SensorType.GPS)
        self.lotitude = lotitude
        self.longtitude = longtitude

    def read_data(self) -> Dict[str, Any]:
        if not self.is_available():
            raise SensorException("Sensor is not available")

        return {
            "lotitude": f"{self.lotitude} deg",
            "longtitude": f"{self.longtitude} deg",
        }

    def update_data(self, direction: Direction = None, distance: int = 0):
        if direction:
            if direction == Direction.FORWARD:
                self.latitude += distance
            elif direction == Direction.BACKWARD:
                self.latitude -= distance
            elif direction == Direction.LEFT:
                self.longitude -= distance
            elif direction == Direction.RIGHT:
                self.longitude += distance
