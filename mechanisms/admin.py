from django.contrib import admin
from .models import Mechanism, MechanismType


# Register your models here.
@admin.register(Mechanism)
class MechanismAdmin(admin.ModelAdmin):
    list_display = ["name", "type", "creator", "robot_id"]
    search_fields = ["id", "name", "type", "creator"]


@admin.register(MechanismType)
class MechanismTypeAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["id", "name"]
