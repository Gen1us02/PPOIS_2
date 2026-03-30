from django.contrib import admin
from .models import Robot, Phrases

# Register your models here.
@admin.register(Robot)
class RobotAdmin(admin.ModelAdmin):
    list_display = ["name", "battery"]
    search_fields = ["id", "name"]
    

@admin.register(Phrases)
class PhrasesAdmin(admin.ModelAdmin):
    list_display = ["name", "robot_id"]
    search_fields = ["id", "name", "robot_id"]