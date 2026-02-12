from source.fabric import Fabric
from source.serializer import Serializer
from source.robot import Robot


def test_convert_to_dict():
    robot = Robot("MyRobot")
    assert Serializer.convert_to_dict(robot) == {
        "name": "MyRobot",
        "status": "INACTIVE",
        "battery": 100,
        "sensors": [],
        "arms": [],
        "legs": [],
        "software": None,
        "data": [],
    }


def test_create_from_dict():
    data = {
        "name": "MyRobot2",
        "status": "WAITING",
        "battery": 78,
        "sensors": [],
        "arms": [],
        "legs": [],
        "software": {"name": "PO", "version": "2.7"},
        "data": ["Hello"],
    }
    fabric = Fabric()
    robot = Serializer.create_from_dict(data, fabric)
    assert robot.name == "MyRobot2"
    assert robot.status.name == "WAITING"
    assert robot.battery_level == 78
    assert len(robot.sensors) == 0
    assert len(robot.arms) == 0
    assert len(robot.legs) == 0
    assert robot.software.name == "PO"
    assert robot.software.version == "2.7"
    assert robot.data == ["Hello"]
