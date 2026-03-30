from django.contrib import admin
from .models import Software, SoftwareTypes

# Register your models here.
@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ["software_type", "version", "updated_at"]
    search_fields = ["id", "software_type"]
    

@admin.register(SoftwareTypes)
class SoftwareTypesAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["id", "name"]