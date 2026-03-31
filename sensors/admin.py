from django.contrib import admin
from .models import Sensor, SensorType

# Register your models here.
@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ["name", "type", "creator", "data"]
    search_fields = ["id", "name", "type", "creator"]

@admin.register(SensorType)
class SensorTypeAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["id", "name"]