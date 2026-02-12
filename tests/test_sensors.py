import pytest
from source.sensors import TemperatureSensor, GPSSensor, OpticalSensor, DistanceSensor
from exceptions.exceptions import SensorException
from source.enums import Direction


def test_temp_init():
    sensor = TemperatureSensor(36)
    assert sensor.temperature == 36
    assert sensor.temp_unit == "C"


def test_temp_read_data():
    sensor = TemperatureSensor(20)
    assert sensor.read_data() == {"temperature": 20, "temp_unit": "C"}
    sensor.is_active = False
    with pytest.raises(SensorException):
        sensor.read_data()


def test_temp_update_data():
    sensor = TemperatureSensor()
    assert sensor.read_data() == {"temperature": 27, "temp_unit": "C"}
    sensor.update_data(120, "F")
    assert sensor.read_data() == {"temperature": 120, "temp_unit": "F"}
    sensor.is_active = False
    with pytest.raises(SensorException):
        sensor.update_data()


def test_dist_init():
    sensor = DistanceSensor(15)
    assert sensor.distance == 15
    assert sensor.dist_unit == "m"


def test_dist_read_data():
    sensor = DistanceSensor(20)
    assert sensor.read_data() == {"distance": 20, "dist_unit": "m"}
    sensor.is_active = False
    with pytest.raises(SensorException):
        sensor.read_data()


def test_dist_update_data():
    sensor = DistanceSensor()
    assert sensor.read_data() == {"distance": 0, "dist_unit": "m"}
    sensor.update_data(100, "cm")
    assert sensor.read_data() == {"distance": 100, "dist_unit": "cm"}
    sensor.is_active = False
    with pytest.raises(SensorException):
        sensor.update_data()


def test_gps_init():
    sensor = GPSSensor()
    assert sensor.longitude == 27.34
    assert sensor.latitude == 53.9


def test_gps_read_data():
    sensor = GPSSensor(29.0, 56.0)
    assert sensor.read_data() == {"latitude": 29.0, "longitude": 56.0}
    sensor.is_active = False
    with pytest.raises(SensorException):
        sensor.read_data()


def test_gps_update_data():
    sensor = GPSSensor()
    assert sensor.read_data() == {"latitude": 53.9, "longitude": 27.34}
    sensor.update_data(Direction.FORWARD, 10)
    assert sensor.read_data() == {"latitude": 63.9, "longitude": 27.34}
    sensor.is_active = False
    with pytest.raises(SensorException):
        sensor.update_data()


def test_opt_init():
    sensor = OpticalSensor()
    assert sensor.objects_count == 0


def test_opt_read_data():
    sensor = OpticalSensor(7)
    assert sensor.read_data() == {"objects_count": 7}
    sensor.is_active = False
    with pytest.raises(SensorException):
        sensor.read_data()


def test_opt_update_data():
    sensor = OpticalSensor(5)
    assert sensor.read_data() == {"objects_count": 5}
    sensor.update_data(10)
    assert sensor.read_data() == {"objects_count": 10}
    sensor.is_active = False
    with pytest.raises(SensorException):
        sensor.update_data()
