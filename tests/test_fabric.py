from source.fabric import Fabric
from source.mechanisms import ArmMechanism, LegMechanism
from source.sensors import DistanceSensor, GPSSensor, OpticalSensor, TemperatureSensor


def get_fabric():
    return Fabric()


def test_create_temperature_sensor():
    fabric = get_fabric()
    obj = fabric.create_temperature_sensor()
    assert isinstance(obj, TemperatureSensor)
    assert obj.temperature == 27
    assert obj.temp_unit == "C"
    obj_kw = fabric.create_temperature_sensor(temperature=35, temp_unit="F")
    assert obj_kw.temperature == 35
    assert obj_kw.temp_unit == "F"


def test_create_gps_sensor():
    fabric = get_fabric()
    obj = fabric.create_gps_sensor()
    assert isinstance(obj, GPSSensor)
    assert obj.longitude == 27.34
    assert obj.latitude == 53.9
    obj_kw = fabric.create_gps_sensor(latitude=35.8, longitude=60.0)
    assert obj_kw.longitude == 60.0
    assert obj_kw.latitude == 35.8


def test_create_distance_sensor():
    fabric = get_fabric()
    obj = fabric.create_distance_sensor()
    assert isinstance(obj, DistanceSensor)
    assert obj.distance == 0
    assert obj.dist_unit == "m"
    obj_kw = fabric.create_distance_sensor(distance=10, dist_unit="cm")
    assert obj_kw.distance == 10
    assert obj_kw.dist_unit == "cm"


def test_create_optical_sensor():
    fabric = get_fabric()
    obj = fabric.create_optical_sensor()
    assert isinstance(obj, OpticalSensor)
    assert obj.objects_count == 0
    obj_kw = fabric.create_optical_sensor(objects_count=5)
    assert obj_kw.objects_count == 5


def test_create_arm():
    fabric = get_fabric()
    obj = fabric.create_arm()
    assert isinstance(obj, ArmMechanism)
    assert obj.curr_damage == 0
    assert obj.item is None


def test_create_leg():
    fabric = get_fabric()
    obj = fabric.create_leg()
    assert isinstance(obj, LegMechanism)
    assert obj.curr_damage == 0
    assert obj.speed == 0
