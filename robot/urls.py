from django.urls import path
from robot.views import RobotView, RobotEditView, RobotCreateView, RobotDeleteView, PhraseCreateView, RobotSoftwareDetachView

app_name = "main"

urlpatterns = [
    path("", RobotView.as_view(), name="index"),
    path("add-robot/", RobotCreateView.as_view(), name="add_robot"),
    path("edit/<str:robot_name>/", RobotEditView.as_view(), name="edit_robot"),
    path("delete/<str:robot_name>/", RobotDeleteView.as_view(), name="delete_robot"),
    path("learn/<str:robot_name>/", PhraseCreateView.as_view(), name="learn"),
    path("detach-software/<str:robot_name>/", RobotSoftwareDetachView.as_view(), name="detach_software")
]
