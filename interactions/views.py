from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib import messages
from .models import Object
from robot.models import Robot, Phrases
from mechanisms.models import Mechanism
from sensors.models import Sensor
from .utils import discharge_robot, repair_check, parse_weather, convert_direction
from source.fabric import Fabric


class InteractionsView(View):
    template_name = "interactions/interactions.html"

    def get(self, request, *args, **kwargs):
        robot = get_object_or_404(Robot, name=self.kwargs.get("robot_name"))
        repair_check(robot)
        mechanisms = enumerate(Mechanism.objects.filter(
            robot_id=robot, damage__lt=100, type__name="Рука"
        ))
        objects = Object.objects.all()
        return render(
            request,
            self.template_name,
            {"robot": robot, "mechanisms": mechanisms, "objects": objects},
        )

    def post(self, request, *args, **kwargs):
        robot = get_object_or_404(Robot, name=self.kwargs.get("robot_name"))
        fabric = Fabric()
        cli_robot = robot.to_library_robot(fabric)
        action = request.POST.get("action")

        if action == "move":
            speed = robot.speed
            direction = request.POST.get("direction")
            duration = int(request.POST.get("duration"))

            leg_mechanisms = Mechanism.objects.filter(robot_id=robot, type__name="Нога")
            if not leg_mechanisms:
                messages.warning(request, "У робота отсутствуют ноги")
            elif all(leg.damage == 100 for leg in leg_mechanisms):
                messages.warning(request, "Ноги робота сломаны. Движение не возможно")
            else:
                lib_direction = convert_direction(direction)
                cli_robot.move(lib_direction, speed, duration)
                
                robot.update_from_library_robot(cli_robot)
                messages.success(
                    request, f"Робот переместился {direction} за {duration} сек."
                )

        elif action == "grab":
            object_id = request.POST.get("object_id")
            mechanism_id = request.POST.get("mechanism_id")
            mechanism_index = request.POST.get("mechanism_index") 
            obj = get_object_or_404(Object, id=object_id)
            mechanism = get_object_or_404(Mechanism, id=mechanism_id)
            cli_robot.arms_action(int(mechanism_index), obj)
            robot.update_from_library_robot(cli_robot)
            messages.success(request, f"Робот поднял {obj} рукой {mechanism.name}")

        elif action == "speak":
            phrases = Phrases.objects.filter(robot_id=robot)
            if phrases:
                res = cli_robot.speak()
                robot.update_from_library_robot(cli_robot)
                discharge_robot(robot, 2)
                messages.success(request, res)
            else:
                messages.warning(request, "Робот не знает ни одной фразы.")

        elif action == "data":
            sensors = Sensor.objects.filter(robot_id=robot, is_active=True)
            if not sensors:
                messages.warning(request, "У робота нет активных сенсоров.")
            else:
                res = cli_robot.get_sensors_data()
                temperature, temp_unit = parse_weather()
                if res.get("temperature", None):
                    res["temperature"] = temperature
                    res["temp_unit"] = temp_unit

                message_lines = [f"• {key}: {value}" for key, value in res.items()]
                message = "\n".join(message_lines)
                robot.update_from_library_robot(cli_robot)
                messages.success(request, message)

        return redirect("interactions:index", robot_name=robot.name)
