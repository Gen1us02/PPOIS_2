from django.db import models


# Create your models here.
class Object(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="Название")

    class Meta:
        db_table = "objects"
        verbose_name = "объект"
        verbose_name_plural = "Объекты"

    def __str__(self):
        return self.name
