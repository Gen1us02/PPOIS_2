from django.contrib import admin
from .models import Object

# Register your models here.
@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["id", "name"]