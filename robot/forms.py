from django import forms
from .models import Robot, Phrases


class AddRobotForm(forms.ModelForm):
    name = forms.CharField()
    image = forms.ImageField()
    speed = forms.IntegerField()
    
    class Meta:
        model = Robot
        fields = ["name", "image", "speed"]
        
class AddPhraseForm(forms.ModelForm):
    name = forms.CharField()
    
    class Meta:
        model = Phrases
        fields = ["name"]