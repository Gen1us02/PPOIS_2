from django.db import models


# Create your models here.
class SoftwareTypes(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="Название ПО")

    class Meta:
        db_table = "software_types"
        verbose_name = "тип ПО"
        verbose_name_plural = "Типы ПО"

    def __str__(self):
        return self.name


class Software(models.Model):
    software_type = models.ForeignKey(
        to=SoftwareTypes, on_delete=models.CASCADE, verbose_name="Тип ПО"
    )
    version = models.CharField(max_length=10, verbose_name="Версия ПО")
    size = models.IntegerField(verbose_name="Размер ПО")
    creator = models.CharField(
        max_length=30, null=True, blank=True, verbose_name="Изготовитель"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего обновления"
    )

    class Meta:
        db_table = "software"
        verbose_name = "програмное обеспечение"
        verbose_name_plural = "Програмные обеспечения"

    def __str__(self):
        return f"{self.software_type.name} v{self.version}"
