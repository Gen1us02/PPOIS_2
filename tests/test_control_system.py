import pytest
from source.enums import Direction
from source.control_system import ControlSystem
from exceptions.exceptions import ControlSystemException
from source.fabric import Fabric

def get_control_system():
    fabric = Fabric()
    return ControlSystem("TestRobot", fabric)

def test_create_robot():
    control = get_control_system()
    assert control.robot.name == "TestRobot"
    assert len(control.robot.sensors) == 4
    assert len(control.robot.arms) == 2
    assert len(control.robot.legs) == 2
    assert control.robot.software.version == "1.0.0"
    assert control.robot.software.name == "Base Software"

def test_charge_robot():
    control = get_control_system()
    control.robot.battery.discharge(20)
    assert control.charge_robot(20) == "Батарея заряжена на 100%"
    assert control.robot.battery_level == 100
    assert control.robot.status.name == "WAITING"
    
    with pytest.raises(ControlSystemException):
        control.charge_robot(-10)

def test_move_robot():
    control = get_control_system()
    result = control.move_robot(Direction.FORWARD, 10, 20)
    assert "Нога робота перемещается вперед" in result
    assert control.robot.status.name == "WAITING"
    assert control.robot.battery_level == 90

def test_arm_action():
    control = get_control_system()
    item1 = "apple"
    item2 = "box"
    index = 0
    result1 = control.arm_action(index, item1)
    result2 = control.arm_action(index, item2)
    assert "Рука робота взяла apple" in result1
    assert "Рука робота бросила apple и взяла box" in result2
    assert control.robot.status.name == "WAITING"
    assert control.robot.battery_level == 80

def test_get_status():
    control = get_control_system()
    status = control.get_status()
    
    assert "status" in status
    assert "battery_level" in status
    assert "is_broken" in status
    assert "temperature" in status
    assert status["battery_level"] == 100
    assert not status["is_broken"]

def test_maintenance():
    control = get_control_system()
    result = control.maintanance()
    
    assert result == "Обслуживание завершилось успешно"
    assert not control.robot.is_broken
    assert control.robot.status.name == "WAITING"

def test_program_robot():
    control = get_control_system()
    result = control.program_robot("2.0.0", "New Software")
    
    assert result == "Робот успешно запрограммирован"
    assert control.robot.software.version == "2.0.0"
    assert control.robot.software.name == "New Software"
    assert control.robot.status.name == "WAITING"

def test_teach_robot():
    control = get_control_system()
    data = ["Hello", "World"]
    result = control.teach_robot(data)
    
    assert result == "Робот успешно выучил новые данные"
    assert len(control.robot.data) == 2
    assert control.robot.data[0] == "Hello"
    assert control.robot.data[1] == "World"
    assert control.robot.status.name == "WAITING"

def test_save_load_condition():
    control = get_control_system()
    control.robot.battery.discharge(20)
    control.teach_robot(["Test Data"])
    
    control.save_condition()
    
    new_control = get_control_system()
    new_control.load_condition()
    
    assert new_control.robot.battery_level == 80
    assert len(new_control.robot.data) == 1
    assert new_control.robot.data[0] == "Test Data"