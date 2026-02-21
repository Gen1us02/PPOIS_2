from typing import List
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtCore import Qt
from src.db.db_manager import DBManager
from src.db.models import Student


class Paginator:
    MAX_PAGE_NUM = 1000000000000000000000

    def __init__(self, db: DBManager, ui: object) -> None:
        self.__ui = ui
        self.__db = db
        self.__current_page = int(self.__ui.current_page.text())
        self.__items_count = int(self.__ui.items_count.currentText())
        self.__min_page = 1
        self.__max_page = self.MAX_PAGE_NUM

    def return_to_first_page(self, students: List[Student]) -> None:
        self.__current_page = self.__min_page
        self.update_page_label()
        self.display_current_page(students)

    def return_to_last_page(self, students: List[Student]) -> None:
        self.__current_page = self.__max_page
        self.update_page_label()
        self.display_current_page(students)

    def next_page(self, students: List[Student]) -> None:
        if self.__current_page != self.__max_page:
            self.__current_page += 1
            self.update_page_label()
            self.display_current_page(students)

    def prev_page(self, students: List[Student]) -> None:
        if self.__current_page != self.__min_page:
            self.__current_page -= 1
            self.update_page_label()
            self.display_current_page(students)

    def update_items_count(self, text, students: List[Student]) -> None:
        self.__items_count = int(text)
        self.update_max_page(students)
        self.update_page_label()
        self.display_current_page(students)

    def update_page_label(self) -> None:
        self.__ui.current_page.setText(str(self.__current_page))

    def update_max_page(self, students: List[Student]) -> None:
        pages_count = len(students) // self.__items_count

        self.__max_page = (
            pages_count if len(students) % self.__items_count == 0 else pages_count + 1
        )

        if self.__current_page > self.__max_page:
            self.__current_page = self.__max_page

    def display_current_page(self, students: List[Student]) -> None:
        table = self.__ui.student_table

        while table.rowCount() > 3:
            table.removeRow(3)

        start = (self.__current_page - 1) * self.__items_count
        end = min(start + self.__items_count, len(students))

        target_students = students[start:end]

        for row, student in enumerate(target_students):
            table.insertRow(row + 3)

            fio_item = QTableWidgetItem(student.full_name)
            fio_item.setTextAlignment(Qt.AlignCenter)
            table.setItem(row + 3, 0, fio_item)

            group_item = QTableWidgetItem(student.group.number)
            group_item.setTextAlignment(Qt.AlignCenter)
            table.setItem(row + 3, 1, group_item)

            grades_by_subject = {}
            for score in student.scores:
                subject_name = score.exam.subject.name
                grades_by_subject[subject_name] = score.grade

            group_exams = self.__db.get_all_exams_in_group(student.group.number)

            for i, subject_name in enumerate(group_exams):
                col = 2 + i * 2
                if col + 1 < table.columnCount():
                    subj_item = QTableWidgetItem(subject_name)
                    subj_item.setTextAlignment(Qt.AlignCenter)
                    table.setItem(row + 3, col, subj_item)

                    grade = grades_by_subject.get(subject_name, "")
                    grade_item = QTableWidgetItem(str(grade) if grade else "")
                    grade_item.setTextAlignment(Qt.AlignCenter)
                    table.setItem(row + 3, col + 1, grade_item)

            for i in range(len(group_exams), 5):
                col = 2 + i * 2
                if col + 1 < table.columnCount():
                    dash_subj = QTableWidgetItem("-")
                    dash_subj.setTextAlignment(Qt.AlignCenter)
                    table.setItem(row + 3, col, dash_subj)

                    dash_grade = QTableWidgetItem("-")
                    dash_grade.setTextAlignment(Qt.AlignCenter)
                    table.setItem(row + 3, col + 1, dash_grade)
