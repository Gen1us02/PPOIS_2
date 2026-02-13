import json
import os
import sys
from typing import List, Optional
from .validator import Validator
from .control_system import ControlSystem
from .enums import Direction
from exceptions.exceptions import ControlSystemException, RobotException
from .fabric import Fabric


class RobotCLI:
    VALID_DIRECTIONS = {d.name.lower(): d for d in Direction}
    VALID_DIRECTION_NAMES = list(VALID_DIRECTIONS.keys())

    def __init__(self):
        self.fabric = Fabric()
        self.cs: Optional[ControlSystem] = None
        self._init_robot()

    def _init_robot(self) -> None:
        print("\n=== Создание нового робота ===")
        try:
            name = self._prompt_non_empty_string("Введите имя робота: ")
            self.cs = ControlSystem(name, self.fabric)
            print(f"Робот '{name}' успешно создан!")
            input("\nНажмите Enter, чтобы продолжить...")
        except KeyboardInterrupt:
            self.cs = None
            return

    @staticmethod
    def _prompt_non_empty_string(prompt: str) -> str:
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("Ошибка: строка не может быть пустой. Повторите ввод.")

    @staticmethod
    def _prompt_positive_int(prompt: str) -> int:
        while True:
            try:
                value = int(input(prompt))
                if value > 0:
                    return value
                print("Ошибка: число должно быть больше 0.")
            except ValueError:
                print("Ошибка: введите целое число.")

    @staticmethod
    def _prompt_version(prompt: str) -> str:
        while True:
            version = input(prompt).strip()
            if Validator.validate_version(version):
                return version
            print(
                "Ошибка: версия должна быть в формате 'цифры.цифры[.цифры...]' (например, 1.0 или 2.3.5)."
            )

    @staticmethod
    def _prompt_direction(prompt: str) -> Direction:
        while True:
            dir_str = input(prompt).strip().lower()
            if dir_str in RobotCLI.VALID_DIRECTIONS:
                return RobotCLI.VALID_DIRECTIONS[dir_str]
            print(
                f"Ошибка: допустимые направления: {', '.join(RobotCLI.VALID_DIRECTION_NAMES)}."
            )

    @staticmethod
    def _prompt_items_list(prompt: str) -> List[str]:
        while True:
            items_str = input(prompt).strip()
            if not items_str:
                print("Ошибка: введите хотя бы один предмет.")
                continue
            items = [item.strip() for item in items_str.split() if item.strip()]
            if items:
                return items
            print("Ошибка: список не может быть пустым.")

    @staticmethod
    def _prompt_yes_no(prompt: str) -> bool:
        while True:
            answer = input(prompt).strip().lower()
            if answer in ("y", "yes", "д", "да"):
                return True
            if answer in ("n", "no", "н", "нет"):
                return False
            print("Ошибка: введите 'y' (да) или 'n' (нет).")

    def _charge(self) -> None:
        print("\n=== Зарядка робота ===")
        amount = self._prompt_positive_int(
            "Введите количество энергии для зарядки (%): "
        )
        try:
            result = self.cs.charge_robot(amount)
            print(f"{result}")
        except ControlSystemException as e:
            print(f"Ошибка зарядки: {e}")

    def _move(self) -> None:
        print("\n=== Движение робота ===")
        speed = self._prompt_positive_int("Скорость (м/с): ")
        direction = self._prompt_direction(
            "Направление (forward/backward/left/right): "
        )
        time = self._prompt_positive_int("Время движения (сек): ")
        try:
            result = self.cs.move_robot(direction, speed, time)
            print(f"Результат движения:\n{result}")
        except ControlSystemException as e:
            print(f"Ошибка движения: {e}")

    def _arm_action(self) -> None:
        print("\n=== Захват предметов ===")
        items = self._prompt_items_list("Введите предметы через пробел: ")
        try:
            result = self.cs.arm_action(items)
            print(f"Результат захвата:\n{result}")
        except ControlSystemException as e:
            print(f"Ошибка захвата: {e}")

    def _status(self) -> None:
        print("\n=== Статус робота ===")
        try:
            status = self.cs.get_status()
            print("Данные сенсоров:")
            for key, value in status.items():
                if key not in ("status", "battery_level", "is_broken"):
                    print(f"  {key}: {value}")
            print("\nСостояние робота:")
            print(f"  Статус: {status['status']}")
            print(f"  Заряд батареи: {status['battery_level']}%")
            print(f"  Требуется ремонт: {'да' if status['is_broken'] else 'нет'}")
        except ControlSystemException as e:
            print(f"Ошибка получения статуса: {e}")

    def _maintenance(self) -> None:
        print("\n=== Техническое обслуживание ===")
        confirm = self._prompt_yes_no("Выполнить полный ремонт робота? (y/n): ")
        if confirm:
            try:
                result = self.cs.maintanance()
                print(f"{result}")
            except ControlSystemException as e:
                print(f"Ошибка обслуживания: {e}")

    def _program(self) -> None:
        print("\n=== Программирование робота ===")
        name = self._prompt_non_empty_string("Название ПО: ")
        version = self._prompt_version("Версия (например, 2.0.0): ")
        try:
            result = self.cs.program_robot(version, name)
            print(f"{result}")
        except ControlSystemException as e:
            print(f"Ошибка программирования: {e}")

    def _teach(self) -> None:
        print("\n=== Обучение робота ===")
        phrases = self._prompt_items_list("Введите фразы для обучения через пробел: ")
        try:
            result = self.cs.teach_robot(phrases)
            print(f"{result}")
        except ControlSystemException as e:
            print(f"Ошибка обучения: {e}")

    def _speak(self) -> None:
        try:
            print("\n=== Робот говорит ===")
            speech = self.cs.robot.speak()
            print(f"{speech}")
        except RobotException as e:
            print(f"Робот не может говорить: {e}")

    def _save(self) -> None:
        print("\n=== Сохранение состояния ===")
        try:
            self.cs.save_condition()
            print("Состояние сохранено в файл condition.json")
        except ControlSystemException as e:
            print(f"Ошибка сохранения: {e}")

    def _load(self) -> None:
        print("\n=== Загрузка состояния ===")
        print("Текущее состояние робота будет заменено!")
        if self._prompt_yes_no("Продолжить? (y/n): "):
            try:
                self.cs.load_condition()
                print(f"Состояние загружено. Робот: {self.cs.robot.name}")
            except (
                ControlSystemException,
                FileNotFoundError,
                json.JSONDecodeError,
            ) as e:
                print(f"Ошибка загрузки: {e}")

    def _print_menu(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n" + "=" * 60)
        print("  СИСТЕМА УПРАВЛЕНИЯ РОБОТОМ  ".center(60))
        print("=" * 60)
        print("   1.  Зарядить робота")
        print("   2.  Движение")
        print("   3.  Захват предметов")
        print("   4.  Получить статус")
        print("   5.  Техническое обслуживание")
        print("   6.  Программирование ПО")
        print("   7.  Обучение")
        print("   8.  Сказать фразу")
        print("   9.  Сохранить состояние")
        print("   10. Загрузить состояние")
        print("   0.  Выход")
        print("=" * 60)

    def _get_menu_choice(self) -> str:
        try:
            while True:
                choice = input("Выберите действие (0-10): ").strip()
                if choice in [str(i) for i in range(12)]:
                    return choice
                print("Ошибка: введите число от 0 до 10.")
        except KeyboardInterrupt:
            return "0"

    def run(self) -> None:
        if not self.cs:
            print("\nЗавершение работы. До свидания!")
            sys.exit(0)

        print("\nДобро пожаловать в систему управления роботом!")
        try:
            while True:
                self._print_menu()
                choice = self._get_menu_choice()

                if choice == "0":
                    print("\nЗавершение работы. До свидания!")
                    sys.exit(0)

                handlers = {
                    "1": self._charge,
                    "2": self._move,
                    "3": self._arm_action,
                    "4": self._status,
                    "5": self._maintenance,
                    "6": self._program,
                    "7": self._teach,
                    "8": self._speak,
                    "9": self._save,
                    "10": self._load,
                }

                handler = handlers.get(choice)
                if handler:
                    handler()
                else:
                    print("Ошибка: неверный пункт меню.")

                input("\nНажмите Enter, чтобы продолжить...")
        except KeyboardInterrupt:
            print("\nЗавершение работы. До свидания!")
            sys.exit(0)
