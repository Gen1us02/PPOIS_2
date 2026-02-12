import pytest
from exceptions.exceptions import DeviceException
from source.device import Device


def get_device():
    return Device()


def test_is_broken():
    device = get_device()
    assert not device.is_broken()
    device.curr_damage = 100
    assert device.is_broken()


def test_damage():
    device = Device()
    assert device.curr_damage == 0
    device.damage(20)
    assert device.curr_damage == 20
    device.damage(100)
    with pytest.raises(DeviceException):
        device.damage(10)
        device.damage(-30)
        device.damage(0)


def test_repair():
    device = get_device()
    device.damage(70)
    assert device.curr_damage == 70
    device.repair()
    assert device.curr_damage == 0
