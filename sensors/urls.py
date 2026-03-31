from django.urls import path
from .views import SensorsView, SensorCreateView, SensorEditView, SensorDeleteView, SensorDetachView

app_name = "sensors"

urlpatterns = [
    path("", SensorsView.as_view(), name="index"),
    path("add-sensor/", SensorCreateView.as_view(), name="add_sensor"),
    path("edit/<int:sensor_id>/", SensorEditView.as_view(), name="edit_sensor"),
    path("delete/<int:sensor_id>/", SensorDeleteView.as_view(), name="delete_sensor"),
    path("detach-sensor/<int:sensor_id>/", SensorDetachView.as_view(), name="detach_sensor")
]
