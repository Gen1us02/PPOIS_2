from django.urls import path
from .views import (
    MechanismsView,
    MechanismCreateView,
    MechanismUpdateView,
    MechanismDeleteView,
    MechanismDetachView,
    MechanismRepairView,
)

app_name = "mechanisms"

urlpatterns = [
    path("", MechanismsView.as_view(), name="index"),
    path("add-mechanism/", MechanismCreateView.as_view(), name="add_mechanism"),
    path(
        "edit-mechanism/<str:mechanism_name>/",
        MechanismUpdateView.as_view(),
        name="edit_mechanism",
    ),
    path(
        "delete-mechanism/<int:mechanism_id>/",
        MechanismDeleteView.as_view(),
        name="delete_mechanism",
    ),
    path(
        "detach-mechanism/<int:mechanism_id>/",
        MechanismDetachView.as_view(),
        name="detach_mechanism",
    ),
    path("repair/", MechanismRepairView.as_view(), name="repair_all"),
    path(
        "repair/<int:mechanism_id>/", MechanismRepairView.as_view(), name="repair_one"
    ),
]
