import pytest
from exceptions.exceptions import BatteryException
from source.battery import Battery


def get_battery():
    return Battery()


def test_init():
    battery = get_battery()
    assert battery.battery_level == 100


def test_charge():
    battery = get_battery()
    battery.battery_level = 10
    assert battery.battery_level == 10
    battery.charge(30)
    assert battery.battery_level == 40
    battery.charge(60)
    with pytest.raises(BatteryException):
        battery.charge(10)
        battery.charge(-10)
        battery.charge(0)


def test_discharge():
    battery = get_battery()
    battery.discharge(30)
    assert battery.battery_level == 70
    battery.discharge(70)
    with pytest.raises(BatteryException):
        battery.discharge(10)
        battery.discharge(-15)
        battery.discharge(0)
