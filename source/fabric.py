from mechanisms import ArmMechanism, LegMechanism
from sensors import DistanceSensor, GPSSensor, OpticalSensor, TemperatureSensor
from abc import ABC, abstractmethod


class DefaultFabric(ABC):
    @abstractmethod
    def create_temperature_sensor(**kwargs):
        pass

    @abstractmethod
    def create_gps_sensor(**kwargs):
        pass

    @abstractmethod
    def create_optical_sensor(**kwargs):
        pass

    @abstractmethod
    def create_distance_sensor(**kwargs):
        pass

    @abstractmethod
    def create_arm():
        pass

    @abstractmethod
    def create_leg():
        pass


class Fabric(DefaultFabric):
    def create_temperature_sensor(**kwargs):
        if kwargs:
            return TemperatureSensor(**kwargs)

        return TemperatureSensor()

    def create_gps_sensor(**kwargs):
        if kwargs:
            return GPSSensor(**kwargs)

        return GPSSensor()

    def create_optical_sensor(**kwargs):
        if kwargs:
            return OpticalSensor(**kwargs)

        return OpticalSensor()

    def create_distance_sensor(**kwargs):
        if kwargs:
            return DistanceSensor(**kwargs)

        return DistanceSensor()

    def create_arm():
        return ArmMechanism()

    def create_leg():
        return LegMechanism()
