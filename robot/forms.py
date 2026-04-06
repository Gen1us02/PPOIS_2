from django import forms
from software.models import Software
from .models import Robot, Phrases


class AddRobotForm(forms.ModelForm):
    name = forms.CharField()
    image = forms.ImageField(required=False)
    speed = forms.IntegerField()
    software = forms.ModelChoiceField(queryset=Software.objects.all(), required=False)

    class Meta:
        model = Robot
        fields = ["name", "image", "speed", "software"]


class AddPhraseForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Phrases
        fields = ["name"]
