from django.urls import path
from .views import MechanismsView, MechanismCreateView, MechanismUpdateView, MechanismDeleteView, MechanismDetachView

app_name = "mechanisms"

urlpatterns = [
    path("", MechanismsView.as_view(), name="index"),
    path("add-mechanism/", MechanismCreateView.as_view(), name="add_mechanism"),
    path("edit-mechanism/<str:mechanism_name>/", MechanismUpdateView.as_view(), name="edit_mechanism"),
    path("delete-mechanism/<int:mechanism_id>/", MechanismDeleteView.as_view(), name="delete_mechanism"),
    path("detach-mechanism/<int:mechanism_id>/", MechanismDetachView.as_view(), name="detach_mechanism")
]
