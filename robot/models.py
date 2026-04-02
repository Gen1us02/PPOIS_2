from django.db import models
from django.db.models import Q
from software.models import Software


# Create your models here.
class RobotStatus(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")

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


class Phrases(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="Фраза")
    robot_id = models.ForeignKey(
        to=Robot, on_delete=models.CASCADE, verbose_name="Робот"
    )

    class Meta:
        db_table = "phrases"
        verbose_name = "фразу"
        verbose_name_plural = "Фразы"
