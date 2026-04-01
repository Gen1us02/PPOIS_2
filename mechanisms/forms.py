from django import forms
from django.db.models import Q, Count
from .models import Mechanism, MechanismType
from robot.models import Robot


class AddMechanismForm(forms.ModelForm):
    type = forms.ModelChoiceField(queryset=MechanismType.objects.all(), label="Тип")
    robot_id = forms.ModelChoiceField(
        queryset=Robot.objects.all(), required=False, label="Робот"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        selected_type = self.initial.get("type") or self.data.get("type")
        if not selected_type and self.instance.pk:
            selected_type = self.instance.type_id

        if selected_type:
            try:
                available_robots = Robot.objects.annotate(
                    limb_count=Count(
                        "mechanisms",
                        filter=Q(mechanisms__type__name="Рука")
                        & Q(mechanisms__type__name="Нога"),
                    )
                ).filter(limb_count__lt=2)
                if self.instance.pk and self.instance.robot_id:
                    available_robots |= Robot.objects.filter(
                        pk=self.instance.robot_id.pk
                    )
                self.fields["robot_id"].queryset = available_robots
            except MechanismType.DoesNotExist:
                pass

    def clean_robot_id(self):
        robot = self.cleaned_data.get("robot_id")
        mechanism_type = self.cleaned_data.get("type")
        if (
            robot
            and mechanism_type
            and (mechanism_type.name == "Рука" or mechanism_type.name == "Нога")
        ):
            existing = (
                robot.mechanisms.filter(type=mechanism_type)
                .exclude(pk=self.instance.pk)
                .count()
            )
            if existing >= 2:
                raise forms.ValidationError(
                    f"У робота уже есть 2 механизма типа «{mechanism_type.name}». "
                    "Добавление ещё одного невозможно."
                )
        return robot

    class Meta:
        model = Mechanism
        fields = ["name", "creator", "type", "robot_id"]
