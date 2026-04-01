from django.db import models
from robot.models import Robot


# Create your models here.
class SensorType(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="Тип сенсора")

    class Meta:
        db_table = "sensor_types"
        verbose_name = "тип сенсора"
        verbose_name_plural = "Типы сенсоров"

    def __str__(self):
        return self.name


class Sensor(models.Model):
    name = models.CharField(max_length=30, verbose_name="Наименование")
    damage = models.IntegerField(default=0, verbose_name="Состояние")
    type = models.ForeignKey(
        to=SensorType, on_delete=models.CASCADE, verbose_name="Тип сенсора"
    )
    is_active = models.BooleanField(default=False, verbose_name="Активен ли")
    creator = models.CharField(
        max_length=30, blank=True, null=True, verbose_name="Изготовитель"
    )
    data = models.JSONField(default=dict, verbose_name="Данные")
    robot_id = models.ForeignKey(
        to=Robot,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="sensors",
        verbose_name="Робот",
    )

    class Meta:
        db_table = "sensors"
        verbose_name = "сенсор"
        verbose_name_plural = "Сенсоры"

    def __str__(self):
        return f"{self.type.name}: {self.name}"
