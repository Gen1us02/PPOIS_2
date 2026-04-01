from django.urls import path
from software.views import (
    SoftwareView,
    SoftwareCreateView,
    SoftwareEditView,
    SoftwareDeleteView,
)

app_name = "software"

urlpatterns = [
    path("", SoftwareView.as_view(), name="index"),
    path("add-software/", SoftwareCreateView.as_view(), name="add_software"),
    path("edit/<int:software_id>/", SoftwareEditView.as_view(), name="edit_software"),
    path(
        "delete/<int:software_id>/",
        SoftwareDeleteView.as_view(),
        name="delete_software",
    ),
]
