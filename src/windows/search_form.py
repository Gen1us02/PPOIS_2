from PySide6.QtWidgets import QDialog, QMessageBox, QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from src.interface.ui.search_form_ui import Ui_SearchForm
from src.db.db_manager import DBManager
from src.utils.paginator import Paginator


class SearchForm(QDialog):
    def __init__(self, db_manager: DBManager) -> None:
        super().__init__()
        self.searched_students = []
        self.db = db_manager
        self.ui = Ui_SearchForm()
        self.ui.setupUi(self)

        self.paginator = Paginator(db_manager, self.ui)

        self.ui.tabWidget.tabBar().hide()
        self.__no_data_setup()
        self.__setup_table()
        self.__setup_groups()
        self.__setup_subjects()

        self.ui.search_students.clicked.connect(self.__search_students)
        self.ui.next_page_button.clicked.connect(
            lambda: self.paginator.next_page(self.searched_students)
        )
        self.ui.prev_page_button.clicked.connect(
            lambda: self.paginator.prev_page(self.searched_students)
        )
        self.ui.first_page_button.clicked.connect(
            lambda: self.paginator.return_to_first_page(self.searched_students)
        )
        self.ui.last_page_button.clicked.connect(
            lambda: self.paginator.return_to_last_page(self.searched_students)
        )
        self.ui.items_count.currentTextChanged.connect(
            lambda text: self.paginator.update_items_count(text, self.searched_students)
        )

    def __setup_table(self) -> None:
        table = self.ui.student_table

        table.setRowCount(3)
        table.setColumnCount(12)

        table.setSpan(0, 0, 3, 1)
        table.setSpan(0, 1, 3, 1)
        table.setSpan(0, 2, 1, 10)

        fio_item = QTableWidgetItem("ФИО\nстудента")
        fio_item.setTextAlignment(Qt.AlignCenter)
        table.setItem(0, 0, fio_item)

        group_item = QTableWidgetItem("группа")
        group_item.setTextAlignment(Qt.AlignCenter)
        table.setItem(0, 1, group_item)

        exams_item = QTableWidgetItem("Экзамены")
        exams_item.setTextAlignment(Qt.AlignCenter)
        table.setItem(0, 2, exams_item)

        for i in range(5):
            table.setSpan(1, 2 + i * 2, 1, 2)
            exam_num = QTableWidgetItem(str(i + 1))
            exam_num.setTextAlignment(Qt.AlignCenter)
            table.setItem(1, 2 + i * 2, exam_num)

            exam_name = QTableWidgetItem("наим")
            exam_name.setTextAlignment(Qt.AlignCenter)
            score = QTableWidgetItem("балл")
            score.setTextAlignment(Qt.AlignCenter)
            table.setItem(2, 2 + i * 2, exam_name)
            table.setItem(2, 3 + i * 2, score)

        table.horizontalHeader().setVisible(False)
        table.verticalHeader().setVisible(False)

        table.setColumnWidth(0, 250)
        table.setColumnWidth(1, 170)

        for i in range(2, 12):
            table.setColumnWidth(i, 60)

        table.setEditTriggers(QTableWidget.NoEditTriggers)
        table.setSelectionMode(QTableWidget.NoSelection)

        table.resizeRowsToContents()

    def __setup_groups(self) -> None:
        groups = self.db.get_all_groups()
        self.ui.groups_list.clear()
        self.ui.groups_list.addItem("Не выбрана")
        self.ui.groups_list.addItems(groups)

    def __no_data_setup(self) -> None:
        label = self.ui.no_data_label
        label.setPixmap(QPixmap("images/no-data.png"))
        label.setScaledContents(False)
        self.ui.tabWidget.setCurrentWidget(self.ui.no_data_search_tab)

    def __setup_subjects(self) -> None:
        subjects = self.db.get_all_subjects()
        self.ui.subject_list.clear()
        self.ui.subject_list.addItem("Не выбран")
        self.ui.subject_list.addItems(subjects)

    def __search_students(self) -> None:
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
            errors.append("Для поиска по оценкам требуется ввести название предмета")

        if subject and not (rating_min_value or rating_max_value):
            errors.append("Для поиска по оценкам требуется ввести диапазоны оценок")

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
            errors.append("Введите данные для поиска")

        if errors:
            QMessageBox.critical(self, "Ошибка ввода", "\n".join(errors))
            return

        search_data = {
            "avg_min": avg_min_value,
            "avg_max": avg_max_value,
            "rating_min": rating_min_value,
            "rating_max": rating_max_value,
            "group": group,
            "subject": subject,
        }

        searched_students = self.db.search_students(**search_data)
        self.searched_students = searched_students
        QMessageBox.information(
            self,
            "Найденные записи",
            f"Количество найденных записей: {len(searched_students)}"
            if len(searched_students) > 0
            else "Записей не найдено",
        )

        self.ui.tabWidget.setCurrentWidget(self.ui.students_search_table_tab) if len(
            searched_students
        ) > 0 else self.__no_data_setup()
        self.paginator.update_max_page(self.searched_students)
        self.paginator.display_current_page(self.searched_students)
