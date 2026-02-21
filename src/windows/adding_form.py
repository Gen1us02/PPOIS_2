from PySide6.QtWidgets import QDialog, QLabel, QLineEdit, QVBoxLayout, QMessageBox
from src.interface.ui.adding_form_ui import Ui_AddForm
from src.db.db_manager import DBManager
from src.utils.validator import Validator


class AddForm(QDialog):
    def __init__(self, db_manager: DBManager) -> None:
        super().__init__()
        self.db = db_manager
        self.ui = Ui_AddForm()
        self.ui.setupUi(self)

        self.__setup_groups()

        self.ui.groups.currentTextChanged.connect(self.__group_selection)
        self.ui.add_button.clicked.connect(self.__add_student)

    def __setup_groups(self) -> None:
        groups = self.db.get_all_groups()
        self.ui.groups.addItems(groups)

    def __group_selection(self, text: str) -> None:
        layout = self.ui.exam_container.layout()
        if layout:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
        else:
            layout = QVBoxLayout()
            self.ui.exam_container.setLayout(layout)

        group_exams = self.db.get_all_exams_in_group(text)
        for i, exam in enumerate(group_exams):
            label = QLabel(exam, self.ui.exam_container)
            label.setObjectName(f"{i}_label")
            layout.addWidget(label)

            score = QLineEdit(parent=self.ui.exam_container)
            score.setObjectName(f"{i}_score")
            score.setPlaceholderText("Введите оценку за экзамен")
            layout.addWidget(score)

    def __add_student(self) -> None:
        errors = []
        group_name = self.ui.groups.currentText()
        if not group_name:
            errors.append("Необходимо выбрать группу")

        last_name = self.ui.last_name.text()
        if not Validator.validate_fio_part(last_name):
            errors.append("Фамилия не должна быть пустая или содержать цифр")

        first_name = self.ui.first_name.text()
        if not Validator.validate_fio_part(first_name):
            errors.append("Имя не должно быть пустым или содержать цифр")

        middle_name = self.ui.middle_name.text()
        if Validator.contains_number(middle_name):
            errors.append("Отчество не должно содержать цифр")

        group_exams = self.db.get_all_exams_in_group(group_name) if group_name else []
        scores = {}
        for i, exam in enumerate(group_exams):
            score_edit = self.ui.exam_container.findChild(QLineEdit, f"{i}_score")
            score_text = score_edit.text().strip()
            if Validator.is_empty(score_text):
                errors.append(f"Оценка по предмету {exam} не введена")
                continue
            try:
                score = int(score_text)
                if not Validator.score_validation(score):
                    errors.append(f"Оценка по предмету {exam} должна быть от 1 до 10")
                else:
                    scores[exam] = score
            except ValueError:
                errors.append(f"Оценка по предмету {exam} должна быть целым числом")

        if errors:
            QMessageBox.critical(self, "Ошибка ввода", "\n".join(errors))
            return

        student_data = {
            "first_name": first_name,
            "last_name": last_name,
            "group_name": group_name,
            "middle_name": middle_name,
            "scores": scores,
        }

        self.db.add_student(**student_data)

        QMessageBox.information(
            self, "Добавление студента", "Студент был успешно добавлен"
        )
