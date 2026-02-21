from PySide6.QtWidgets import QDialog, QMessageBox, QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt
from src.interface.ui.search_form_ui import Ui_SearchForm
from src.db.db_manager import DBManager


class SearchForm(QDialog):
    MAX_PAGE_NUM = 1000000000000000000000

    def __init__(self, db_manager: DBManager) -> None:
        super().__init__()
        self.searched_students = []
        self.db = db_manager
        self.ui = Ui_SearchForm()
        self.ui.setupUi(self)
        self.current_page = int(self.ui.current_page.text())
        self.items_count = int(self.ui.items_count.currentText())
        self.__min_page = 1
        self.__max_page = self.MAX_PAGE_NUM

        self.ui.tabWidget.tabBar().hide()
        self.__setup_table()
        self.__setup_groups()
        self.__setup_subjects()

        self.ui.search_students.clicked.connect(self.__search_students)
        self.ui.next_page_button.clicked.connect(self.__next_page)
        self.ui.prev_page_button.clicked.connect(self.__prev_page)
        self.ui.first_page_button.clicked.connect(self.__return_to_first_page)
        self.ui.last_page_button.clicked.connect(self.__return_to_last_page)
        self.ui.items_count.currentTextChanged.connect(self.__update_items_count)

    def __setup_table(self) -> None:
        table = self.ui.table_widget

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

    def __setup_subjects(self) -> None:
        subjects = self.db.get_all_subjects()
        self.ui.subject_list.clear()
        self.ui.subject_list.addItem("Не выбран")
        self.ui.subject_list.addItems(subjects)

    def __return_to_first_page(self) -> None:
        self.current_page = self.__min_page
        self.__update_page_label()
        self.__display_current_page()

    def __return_to_last_page(self) -> None:
        self.current_page = self.__max_page
        self.__update_page_label()
        self.__display_current_page()

    def __next_page(self) -> None:
        if self.current_page != self.__max_page:
            self.current_page += 1
            self.__update_page_label()
            self.__display_current_page()

    def __prev_page(self) -> None:
        if self.current_page != self.__min_page:
            self.current_page -= 1
            self.__update_page_label()
            self.__display_current_page()

    def __update_items_count(self, text) -> None:
        self.items_count = int(text)
        self.__update_max_page()
        self.__update_page_label()
        self.__display_current_page()

    def __update_page_label(self) -> None:
        self.ui.current_page.setText(str(self.current_page))

    def __update_max_page(self) -> None:
        pages_count = len(self.students) // self.items_count

        self.__max_page = (
            pages_count
            if len(self.students) % self.items_count == 0
            else pages_count + 1
        )

        if self.current_page > self.__max_page:
            self.current_page = self.__max_page

    def __display_current_page(self) -> None:
        table = self.ui.table_widget

        while table.rowCount() > 3:
            table.removeRow(3)

        start = (self.current_page - 1) * self.items_count
        end = min(start + self.items_count, len(self.searched_students))

        target_students = self.searched_students[start:end]

        for row, student in enumerate(target_students):
            table.insertRow(row + 3)

            table.setItem(row + 3, 0, QTableWidgetItem(student.full_name))
            table.setItem(row + 3, 1, QTableWidgetItem(student.group.number))

            grades_by_subject = {}
            for score in student.scores:
                subject_name = score.exam.subject.name
                grades_by_subject[subject_name] = score.grade

            group_exams = self.db.get_all_exams_in_group(student.group.number)

            for i, subject_name in enumerate(group_exams):
                col = 2 + i * 2
                if col + 1 < table.columnCount():
                    table.setItem(row + 3, col, QTableWidgetItem(subject_name))
                    grade = grades_by_subject.get(subject_name, "")
                    table.setItem(
                        row + 3, col + 1, QTableWidgetItem(str(grade) if grade else "")
                    )

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
        ) > 0 else self.ui.tabWidget.setCurrentWidget(self.ui.no_data_search_tab)
        self.__display_current_page()
