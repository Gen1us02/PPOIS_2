import pytest
from source.mechanisms import ArmMechanism, LegMechanism
from exceptions.exceptions import MechanismException
from source.enums import Direction


def test_grab():
    arm = ArmMechanism()
    assert arm.grab("box") == "Рука робота взяла box"
    assert arm.curr_damage == 5
    assert arm.grab("apple") == "Рука робота бросила box и взяла apple"
    assert arm.curr_damage == 12
    arm.curr_damage = 100
    with pytest.raises(MechanismException):
        arm.grab("paper")


def test_drop():
    arm = ArmMechanism()
    arm.grab("box")
    assert arm.drop() == "Рука робота бросила box"
    with pytest.raises(MechanismException):
        arm.drop()
        arm.curr_damage = 100
        arm.drop()


def test_move():
    leg = LegMechanism()
    assert (
        leg.move(Direction.FORWARD, 10, 60)
        == "Нога робота перемещается вперед со скоростью 10 м/с. Она прошла 600 м"
    )
    assert leg.curr_damage == 5
    leg.curr_damage = 100
    with pytest.raises(MechanismException):
        leg.move(Direction.LEFT, 5, 30)
