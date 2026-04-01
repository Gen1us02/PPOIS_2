from django.db import models
from robot.models import Robot


# Create your models here.
class MechanismType(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="Название")

    class Meta:
        db_table = "mechanism_types"
        verbose_name = "тип механизма"
        verbose_name_plural = "Типы механизмов"
        
    def __str__(self):
        return self.name


class Mechanism(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    creator = models.CharField(max_length=30, verbose_name="Производитель")
    type = models.ForeignKey(
        to=MechanismType, on_delete=models.CASCADE, verbose_name="Тип механизма"
    )
    damage = models.IntegerField(default=0, verbose_name="Состояние")
    robot_id = models.ForeignKey(
        to=Robot,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="mechanisms",
        verbose_name="Робот",
    )

    class Meta:
        db_table = "mechanisms"
        verbose_name = "механизм"
        verbose_name_plural = "Механизмы"
        
    def __str__(self):
        return self.name
