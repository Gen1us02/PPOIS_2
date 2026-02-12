import pytest
from source.mechanisms import ArmMechanism, LegMechanism
from exceptions.exceptions import MechanismException
from source.enums import Direction


def test_grab():
    arm = ArmMechanism()
    assert arm.grab("box") == "Robot arm grab box"
    assert arm.curr_damage == 5
    assert arm.grab("apple") == "Robot arm drop box and grab apple"
    assert arm.curr_damage == 12
    arm.curr_damage = 100
    with pytest.raises(MechanismException):
        arm.grab("paper")


def test_drop():
    arm = ArmMechanism()
    arm.grab("box")
    assert arm.drop() == "Robot arm drop box"
    with pytest.raises(MechanismException):
        arm.drop()
        arm.curr_damage = 100
        arm.drop()


def test_move():
    leg = LegMechanism()
    assert (
        leg.move(Direction.FORWARD, 10, 60)
        == "Robot leg moved forward with speed 10 m/s. It passed 600 m"
    )
    assert leg.curr_damage == 5
    leg.curr_damage = 100
    with pytest.raises(MechanismException):
        leg.move(Direction.LEFT, 5, 30)
