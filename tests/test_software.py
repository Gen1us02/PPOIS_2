import pytest
from source.software import Software
from exceptions.exceptions import SoftwareException


def get_software():
    return Software("1.0.0", "BaseSoftware")


def test_init():
    name = "Software"
    correct_version = "2.12.5"
    software = Software(correct_version, name)
    assert software.name == "Software" and software.version == "2.12.5"
    with pytest.raises(SoftwareException):
        Software("oajdiak", "Base Software")


def test_update():
    software = get_software()
    software.update("2.13.9")
    assert software.version == "2.13.9"
    with pytest.raises(SoftwareException):
        software.update("0.9.11")
        software.update("jbfdhaj")
