from django.urls import path
from .views import SensorsView, SensorCreateView, SensorEditView, SensorDeleteView, SensorDetachView, SensorRepairView

app_name = "sensors"

urlpatterns = [
    path("", SensorsView.as_view(), name="index"),
    path("add-sensor/", SensorCreateView.as_view(), name="add_sensor"),
    path("edit/<int:sensor_id>/", SensorEditView.as_view(), name="edit_sensor"),
    path("delete/<int:sensor_id>/", SensorDeleteView.as_view(), name="delete_sensor"),
    path("detach-sensor/<int:sensor_id>/", SensorDetachView.as_view(), name="detach_sensor"),
    path("repair/", SensorRepairView.as_view(), name="repair_all"),
    path("repair/<int:sensor_id>/", SensorRepairView.as_view(), name="repair_one")
]
