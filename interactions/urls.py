from django.urls import path
from .views import InteractionsView

app_name = "main"

urlpatterns = [
    path("<str:robot_name>/", InteractionsView.as_view(), name="index"),
]
