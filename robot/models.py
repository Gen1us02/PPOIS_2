from django.db import models
from django.db.models import Q
from software.models import Software
from sensors.models import Sensor, SensorType
from mechanisms.models import Mechanism, MechanismType
import source.robot as cli_robot
import source.software as cli_software
import source.enums as cli_enums
from source.battery import Battery
from source.fabric import Fabric
from source.serializer import Serializer
from .utils import convert_from_library_sensor, convert_to_library_sensor


# Create your models here.
class RobotStatus(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="Название")

    class Meta:
        db_table = "robot_statuses"
        verbose_name = "статус"
        verbose_name_plural = "Статусы"

    def __str__(self):
        return self.name


class Robot(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя робота")
    speed = models.IntegerField(default=10, verbose_name="Скорость")
    image = models.ImageField(
        upload_to="robot_images", verbose_name="Изображение робота"
    )
    battery = models.IntegerField(default=100, verbose_name="Заряд")
    software = models.ForeignKey(
        to=Software, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ПО"
    )
    status = models.ForeignKey(
        to=RobotStatus,
        on_delete=models.SET_DEFAULT,
        default=2,
        verbose_name="Статус",
    )

    class Meta:
        db_table = "robots"
        verbose_name = "робота"
        verbose_name_plural = "Роботы"
        constraints = [
            models.CheckConstraint(
                condition=Q(battery__gte=0) & Q(battery__lte=100), name="battery_range"
            ),
            models.CheckConstraint(
                condition=Q(speed__gte=1) & Q(speed__lte=50), name="speed_range"
            ),
        ]

    def __str__(self):
        return self.name

    def to_library_robot(self, fabric: Fabric) -> cli_robot.Robot:
        lib_robot = cli_robot.Robot(self.name)

        lib_robot.status = cli_enums.RobotStatus[self.status.name]
        lib_robot.battery = Battery(self.battery)

        if self.software:
            lib_robot.software = cli_software.Software(
                self.software.version, self.software.name
            )

        phrases = Phrases.objects.filter(robot_id=self)
        lib_robot.data = [p.name for p in phrases]

        for db_sensor in self.sensors.all():
            sensor_type_name = convert_to_library_sensor(db_sensor.type.name)
            sensor_data = db_sensor.data

            if sensor_type_name == "temperature":
                sensor = fabric.create_temperature_sensor(**sensor_data)
            elif sensor_type_name == "optical":
                sensor = fabric.create_optical_sensor(**sensor_data)
            elif sensor_type_name == "gps":
                sensor = fabric.create_gps_sensor(**sensor_data)
            else:
                sensor = fabric.create_distance_sensor(**sensor_data)

            sensor.curr_damage = db_sensor.damage
            sensor.is_active = db_sensor.is_active
            sensor.name = db_sensor.name
            sensor.creator = db_sensor.creator
            lib_robot.add_sensor(sensor)

        for db_mech in self.mechanisms.all():
            mech_type_name = db_mech.type.name.lower()
            if mech_type_name == "рука":
                arm = fabric.create_arm()
                arm.curr_damage = db_mech.damage
                arm.name = db_mech.name
                arm.creator = db_mech.creator
                lib_robot.add_arm(arm)
            elif mech_type_name == "нога":
                leg = fabric.create_leg()
                leg.curr_damage = db_mech.damage
                leg.name = db_mech.name
                leg.creator = db_mech.creator
                lib_robot.add_leg(leg)

        return lib_robot

    def update_from_library_robot(self, lib_robot: cli_robot.Robot) -> None:
        self.name = lib_robot.name
        self.battery = lib_robot.battery.battery_level
        status_name = lib_robot.status.name
        self.status = RobotStatus.objects.get(name=status_name)
        if lib_robot.software:
            sw_obj, _ = Software.objects.get_or_create(
                name=lib_robot.software.name,
                defaults={"version": lib_robot.software.version},
            )
            self.software = sw_obj
        else:
            self.software = None
        self.save()

        self.phrases.all().delete()
        for phrase_text in lib_robot.data:
            Phrases.objects.create(robot_id=self, name=phrase_text)

        self.sensors.all().delete()
        robot_dict = Serializer.convert_to_dict(lib_robot)
        for sensor_dict in robot_dict["sensors"]:
            sensor_type_name = convert_from_library_sensor(sensor_dict["type"].lower())
            sensor_type_obj = SensorType.objects.get(name__iexact=sensor_type_name)

            Sensor.objects.create(
                name=sensor_dict.get("name", ""),
                damage=sensor_dict.get("damage", 0),
                type=sensor_type_obj,
                is_active=sensor_dict.get("is_active", False),
                creator=sensor_dict.get("creator", None),
                data=sensor_dict.get("data", {}),
                robot_id=self,
            )

        self.mechanisms.all().delete()
        arm_type = MechanismType.objects.get(name__iexact="Рука")
        leg_type = MechanismType.objects.get(name__iexact="Нога")

        for arm_dict in robot_dict["arms"]:
            Mechanism.objects.create(
                name=arm_dict.get("name", ""),
                creator=arm_dict.get("creator", None),
                type=arm_type,
                damage=arm_dict.get("damage", 0),
                robot_id=self,
            )
        for leg_dict in robot_dict["legs"]:
            Mechanism.objects.create(
                name=leg_dict.get("name", ""),
                creator=leg_dict.get("creator", None),
                type=leg_type,
                damage=leg_dict.get("damage", 0),
                robot_id=self,
            )


class Phrases(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="Фраза")
    robot_id = models.ForeignKey(
        to=Robot, on_delete=models.CASCADE, verbose_name="Робот"
    )

    class Meta:
        db_table = "phrases"
        verbose_name = "фразу"
        verbose_name_plural = "Фразы"

    def __str__(self):
        return self.name
