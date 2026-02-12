import pytest
from source.enums import Direction
from source.mechanisms import ArmMechanism, LegMechanism
from source.robot import Robot
from exceptions.exceptions import RobotException
from source.sensors import DistanceSensor, GPSSensor, TemperatureSensor


def get_robot():
    return Robot("MyRobot")


def test_activate():
    robot = get_robot()
    assert robot.status.name == "INACTIVE"
    robot.activate()
    assert robot.status.name == "ACTIVE"
    with pytest.raises(RobotException):
        for _ in range(10):
            robot.move(10, Direction.FORWARD, 30)
        robot.activate()


def test_wait():
    robot = get_robot()
    assert robot.status.name == "INACTIVE"
    robot.wait()
    assert robot.status.name == "WAITING"


def test_maintenance():
    robot = get_robot()
    assert robot.status.name == "INACTIVE"
    robot.maintenance()
    assert robot.status.name == "MAINTENANCE"


def test_charging():
    robot = get_robot()
    assert robot.status.name == "INACTIVE"
    robot.charging()
    assert robot.status.name == "CHARGING"


def test_add_sensor():
    robot = get_robot()
    sensors = [TemperatureSensor(), DistanceSensor(), GPSSensor()]
    for sensor in sensors:
        robot.add_sensor(sensor)

    assert len(robot.sensors) == 3


def test_add_arm():
    robot = get_robot()
    for _ in range(4):
        robot.add_arm(ArmMechanism())

    assert len(robot.arms) == 4


def test_add_leg():
    robot = get_robot()
    for _ in range(3):
        robot.add_leg(LegMechanism())

    assert len(robot.legs) == 3


def test_update_software():
    robot = get_robot()
    name, version = "Software", "1.0.0"
    robot.update_software(version, name)
    assert robot.software.name == "Software" and robot.software.version == "1.0.0"
    robot.update_software("1.2.0", "Software")
    assert robot.software.name == "Software" and robot.software.version == "1.2.0"
    robot.update_software("0.8.0", "Base Po")
    assert robot.software.name == "Base Po" and robot.software.version == "0.8.0"
    with pytest.raises(RobotException):
        robot.update_software("0.6", "Base Po")


def test_arms_action():
    robot = get_robot()
    for _ in range(2):
        robot.add_arm(ArmMechanism())

    robot.activate()
    assert (
        robot.arms_action(items=["apple", "box"])
        == "Robot arm grab apple\nRobot arm grab box\n"
    )

    assert robot.battery_level == 90


def test_move():
    robot = get_robot()
    for _ in range(2):
        robot.add_leg(LegMechanism())

    robot.activate()
    assert (
        robot.move(Direction.FORWARD, 10, 20)
        == "Robot leg moved forward with speed 10 m/s. It passed 200 m\nRobot leg moved forward with speed 10 m/s. It passed 200 m\n"
    )

    assert robot.battery_level == 90


def test_learn_data():
    robot = get_robot()
    data = ["Hello", "Artemdjdj"]
    with pytest.raises(RobotException):
        robot.learn_data(data)
    robot.activate()
    assert robot.learn_data(data) == "Robot successfuly learn new data"
    assert len(robot.data) == 2
    assert robot.data[0] == "Hello"
    assert robot.data[1] == "Artemdjdj"


def test_speak():
    robot = get_robot()
    with pytest.raises(RobotException):
        robot.speak()
        robot.activate()
        robot.speak()


def test_charge():
    robot = get_robot()
    robot.battery.discharge(20)
    assert robot.battery_level == 80
    robot.charge(20)
    assert robot.battery_level == 100
    with pytest.raises(RobotException):
        robot.charge(-10)
        robot.charge(20)


def test_get_sensor_data():
    robot = get_robot()
    robot.add_sensor(TemperatureSensor())
    assert robot.get_sensors_data() == {"temperature": 27, "temp_unit": "C"}


def test_repair():
    robot = get_robot()
    sensors = [TemperatureSensor(), DistanceSensor(), GPSSensor()]
    for sensor in sensors:
        robot.add_sensor(sensor)
    robot.repair()
    assert not robot.is_broken
