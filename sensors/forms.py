from django import forms
from .models import Sensor, SensorType
from robot.models import Robot


class AddSensorForm(forms.ModelForm):
    type = forms.ModelChoiceField(queryset=SensorType.objects.all())
    robot_id = forms.ModelChoiceField(queryset=Robot.objects.all(), required=False)
    
    class Meta:
        model = Sensor
        fields = ["name", "type" ,"creator", "robot_id"]
