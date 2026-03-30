from django import forms
from .models import Software, SoftwareTypes


class AddSoftwareForm(forms.ModelForm):
    software_type = forms.ModelChoiceField(queryset=SoftwareTypes.objects.all())
    
    class Meta:
        model = Software
        fields = ["software_type" ,"version", "size", "creator"]
