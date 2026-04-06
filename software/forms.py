from django import forms
from django.core.exceptions import ValidationError
from .models import Software, SoftwareTypes
import re


class AddSoftwareForm(forms.ModelForm):
    software_type = forms.ModelChoiceField(queryset=SoftwareTypes.objects.all())

    class Meta:
        model = Software
        fields = ["software_type", "version", "size", "creator"]

    def clean_version(self):
        version = self.cleaned_data["version"]
        pattern = re.compile(r"^\d+(?:\.\d+)+$")

        if not pattern.match(version):
            raise ValidationError(
                "Версия должна быть в формате 'цифры.цифры[.цифры...]' (например, 1.0 или 2.3.5)."
            )

        return version
