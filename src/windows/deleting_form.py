from PySide6.QtWidgets import QDialog, QMessageBox
from src.interface.ui.deleting_form_ui import Ui_DeleteForm
from src.db.db_manager import DBManager


class DeleteForm(QDialog):
    def __init__(self, db_manager: DBManager) -> None:
        super().__init__()
        self.db = db_manager
        self.ui = Ui_DeleteForm()
        self.ui.setupUi(self)
        self.setWindowTitle("Удаление")

        self.__setup_groups()
        self.__setup_subjects()
        self.ui.delete_button.clicked.connect(self.__delete_students)

    def __setup_groups(self) -> None:
        groups = self.db.get_all_groups()
        self.ui.groups_list.clear()
        self.ui.groups_list.addItem("Не выбрана")
        self.ui.groups_list.addItems(groups)

    def __setup_subjects(self) -> None:
        subjects = self.db.get_all_subjects()
        self.ui.subject_list.clear()
        self.ui.subject_list.addItem("Не выбран")
        self.ui.subject_list.addItems(subjects)

    def __delete_students(self) -> None:
        errors = []

        avg_min_text = self.ui.avg_rating_min.text()
        avg_min_value = (
            float(avg_min_text.replace(",", ".")) if avg_min_text != "0,0" else None
        )

        avg_max_text = self.ui.avg_rating_max.text()
        avg_max_value = (
            float(avg_max_text.replace(",", ".")) if avg_max_text != "0,0" else None
        )

        rating_min_text = self.ui.rating_min.text()
        rating_min_value = int(rating_min_text) if rating_min_text != "0" else None

        rating_max_text = self.ui.rating_max.text()
        rating_max_value = int(rating_max_text) if rating_max_text != "0" else None

        group = self.ui.groups_list.currentText()
        if group == "Не выбрана":
            group = None

        subject = self.ui.subject_list.currentText()
        if subject == "Не выбран":
            subject = None

        if (rating_min_value or rating_max_value) and not subject:
            errors.append("Для удаления по оценкам требуется ввести название предмета")

        if subject and not (rating_min_value or rating_max_value):
            errors.append("Для удаления по оценкам требуется ввести диапазоны оценок")

        if (avg_min_value and avg_max_value) and avg_min_value >= avg_max_value:
            errors.append("Нижняя граница среднего балла должна быть меньше верхней")

        if (
            rating_min_value and rating_max_value
        ) and rating_min_value >= rating_max_value:
            errors.append("Нижняя граница оценки за экзамен должна быть меньше верхней")

        if not any(
            (
                avg_min_value,
                avg_max_value,
                rating_min_value,
                rating_max_value,
                subject,
                group,
            )
        ):
            errors.append("Введите данные для удаления")

        if errors:
            QMessageBox.critical(self, "Ошибка ввода", "\n".join(errors))
            return

        delete_data = {
            "avg_min": avg_min_value,
            "avg_max": avg_max_value,
            "rating_min": rating_min_value,
            "rating_max": rating_max_value,
            "group": group,
            "subject": subject,
        }

        delete_students_count = self.db.delete_students(**delete_data)
        QMessageBox.information(
            self,
            "Удаленные записи",
            f"Количество удаленных записей: {delete_students_count}"
            if delete_students_count > 0
            else "Записей не найдено",
        )
