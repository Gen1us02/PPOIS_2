from robot.models import RobotStatus
from mechanisms.models import Mechanism
from sensors.models import Sensor
import requests
import os
from dotenv import load_dotenv

load_dotenv()


def discharge_robot(robot, amount):
    robot.battery = max(0, robot.battery - amount)
    if robot.battery == 0:
        robot.status = RobotStatus.objects.get(name="Разряжен")
    robot.save()


def repair_check(robot):
    all_mechanisms = Mechanism.objects.filter(robot_id=robot)
    all_sensors = Sensor.objects.filter(robot_id=robot)

    count = sum(1 for mech in all_mechanisms if mech.damage == 100) + sum(
        1 for sens in all_sensors if sens.damage == 100
    )

    if count > (len(all_mechanisms) + len(all_sensors)) // 2:
        robot.status = RobotStatus.objects.get(name="Требуется ремонт")
        robot.save()


def parse_weather():
    api = os.getenv("API_KEY")
    url = os.getenv("URL")

    params = {"q": "Minsk", "appid": api, "units": "metric", "lang": "ru"}

    request = requests.get(url, params=params)
    data = request.json()

    if data["cod"] == 200:
        temp = data["main"]["temp"]

        return (temp, "C")

    return 27, "C"
