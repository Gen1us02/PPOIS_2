from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib import messages
from .models import Object
from robot.models import Robot, Phrases
from mechanisms.models import Mechanism
from sensors.models import Sensor
from .utils import discharge_robot, repair_check, parse_weather
import random
from math import ceil


class InteractionsView(View):
    template_name = "interactions/interactions.html"

    def get(self, request, *args, **kwargs):
        robot = get_object_or_404(Robot, name=self.kwargs.get("robot_name"))
        repair_check(robot)
        mechanisms = Mechanism.objects.filter(
            robot_id=robot, damage__lt=100, type__name="Рука"
        )
        objects = Object.objects.all()
        return render(
            request,
            self.template_name,
            {"robot": robot, "mechanisms": mechanisms, "objects": objects},
        )

    def post(self, request, *args, **kwargs):
        robot = get_object_or_404(Robot, name=self.kwargs.get("robot_name"))
        action = request.POST.get("action")

        if action == "move":
            direction = request.POST.get("direction")
            duration = int(request.POST.get("duration"))
            discharge = ceil(duration * 0.2)
            discharge_robot(robot, discharge)

            leg_mechanisms = Mechanism.objects.filter(robot_id=robot, type__name="Нога")
            if not leg_mechanisms:
                messages.warning(request, "У робота отсутствуют ноги")
            elif all(leg.damage == 100 for leg in leg_mechanisms):
                messages.warning(request, "Ноги робота сломаны. Движение не возможно")
            else:
                for mech in leg_mechanisms:
                    mech.damage = min(100, mech.damage + 10)
                    mech.save()

                distance = robot.speed * duration
                for sensor in Sensor.objects.filter(robot_id=robot):
                    if sensor.type.name == "Дистанционный":
                        current_distance = sensor.data.get("distance", 0)
                        sensor.data["Расстояние"] = current_distance + distance
                        sensor.save()
                    if sensor.type.name == "GPS":
                        if direction == "Вперед":
                            sensor.data["Долгота"] = (
                                sensor.data.get("Долгота", 53.9) + distance
                            )
                        elif direction == "Назад":
                            sensor.data["Долгота"] = (
                                sensor.data.get("Долгота", 53.9) - distance
                            )
                        elif direction == "Влево":
                            sensor.data["Широта"] = (
                                sensor.data.get("Широта", 27.34) - distance
                            )
                        elif direction == "Вправо":
                            sensor.data["Широта"] = (
                                sensor.data.get("Широта", 27.34) + distance
                            )
                        sensor.save()

                messages.success(
                    request, f"Робот переместился {direction} за {duration} сек."
                )

        elif action == "grab":
            discharge_robot(robot, 5)
            object_id = request.POST.get("object_id")
            mechanism_id = request.POST.get("mechanism_id")
            obj = get_object_or_404(Object, id=object_id)
            mechanism = get_object_or_404(Mechanism, id=mechanism_id)
            mechanism.damage = min(100, mechanism.damage + 10)
            mechanism.save()
            messages.success(request, f"Робот поднял {obj} рукой {mechanism.name}")

        elif action == "speak":
            discharge_robot(robot, 2)
            phrases = Phrases.objects.filter(robot_id=robot)
            if phrases:
                phrase = random.choice(phrases)
                messages.success(request, f"Робот сказал: {phrase}")
            else:
                messages.warning(request, "Робот не знает ни одной фразы.")

        elif action == "data":
            discharge_robot(robot, 5)
            sensors = Sensor.objects.filter(robot_id=robot, is_active=True)
            if not sensors:
                messages.warning(request, "У робота нет активных сенсоров.")
            else:
                lines = []
                for sensor in sensors:
                    if sensor.type.name == "Температурный":
                        data = parse_weather()
                        sensor.data = {
                            "Температура": data[0],
                            "Температурный юнит": data[1],
                        }
                        sensor.save()

                    if sensor.type.name == "Оптический":
                        objects_count = random.randint(0, 15)
                        sensor.data = {"Количество объектов": objects_count}
                        sensor.save()

                    sensor.damage = min(100, sensor.damage + 5)
                    if sensor.damage == 100:
                        sensor.is_active = False
                    sensor.save()
                    lines.append(f"{sensor.name} ({sensor.type.name})")
                    lines.append(f"   • Повреждение: {sensor.damage}/100")
                    if sensor.data:
                        data_str = ", ".join(
                            f"{k}: {v}" for k, v in sensor.data.items()
                        )
                        lines.append(f"   • Данные: {data_str}")
                    else:
                        lines.append("   • Данные: отсутствуют")

                    lines.append("")
                message = "\n".join(lines)
                messages.success(request, message)

        return redirect("interactions:index", robot_name=robot.name)
