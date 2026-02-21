from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from src.interface.ui.main_window_ui import Ui_MainWindow
from src.db.db_manager import DBManager
from .adding_form import AddForm
from .deleting_form import DeleteForm
from .search_form import SearchForm


class MainWindow(QMainWindow):
    MAX_PAGE_NUM = 1000000000000000000000

    def __init__(self, db_manager: DBManager) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = db_manager
        self.students = []
        self.current_page = int(self.ui.current_page_main.text())
        self.items_count = int(self.ui.items_count_main.currentText())
        self.__min_page = 1
        self.__max_page = self.MAX_PAGE_NUM

        self.__no_data_setup()
        self.__setup_table()
        self.__tabs_selection()

        self.ui.first_page_button_main.clicked.connect(self.__return_to_first_page)
        self.ui.last_page_button_main.clicked.connect(self.__return_to_last_page)
        self.ui.load_database_button.clicked.connect(self.__load_db)
        self.ui.load_file_button.clicked.connect(self.__load_file)
        self.ui.next_page_button_main.clicked.connect(self.__next_page)
        self.ui.prev_page_button_main.clicked.connect(self.__prev_page)
        self.ui.items_count_main.currentTextChanged.connect(self.__update_items_count)
        self.ui.add_students_button.clicked.connect(self.__adding_student)
        self.ui.delete_students_button.clicked.connect(self.__deleting_student)
        self.ui.search_students_button.clicked.connect(self.__search_students)

    def __setup_table(self) -> None:
        table = self.ui.table_widget_main

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
        
    def __no_data_setup(self) -> None:
        label = self.ui.no_data_label_main
        label.setPixmap(QPixmap("images/no-data.png"))
        label.setScaledContents(False)
        self.ui.table_tab_widget.setCurrentWidget(self.ui.no_data_tab)

    def __tabs_selection(self) -> None:
        self.ui.work_tab_widget.tabBar().hide()
        self.ui.table_tab_widget.tabBar().hide()

        self.ui.work_tab_widget.setCurrentWidget(self.ui.data_load_tab)
        self.ui.table_tab_widget.setCurrentWidget(self.ui.no_data_tab)

    def __load_file(self) -> None:
        self.ui.table_tab_widget.setCurrentWidget(self.ui.student_table_tab)
        self.ui.work_tab_widget.setCurrentWidget(self.ui.data_work_tab)
        # Дальнейшая логика

    def __load_db(self) -> None:
        self.ui.table_tab_widget.setCurrentWidget(self.ui.student_table_tab)
        self.ui.work_tab_widget.setCurrentWidget(self.ui.data_work_tab)

        students = self.db.get_all_records()
        self.students = students
        self.__update_max_page()
        self.__display_current_page()

    def __update_page_label(self) -> None:
        self.ui.current_page_main.setText(str(self.current_page))

    def __display_current_page(self) -> None:
        if len(self.students)  == 0:
            self.__no_data_setup()
            return 
        
        table = self.ui.table_widget_main

        while table.rowCount() > 3:
            table.removeRow(3)

        start = (self.current_page - 1) * self.items_count
        end = min(start + self.items_count, len(self.students))

        target_students = self.students[start:end]

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

    def __update_max_page(self) -> None:
        pages_count = len(self.students) // self.items_count

        self.__max_page = (
            pages_count
            if len(self.students) % self.items_count == 0
            else pages_count + 1
        )

        if self.current_page > self.__max_page:
            self.current_page = self.__max_page

    def __adding_student(self) -> None:
        add_form = AddForm(self.db)
        add_form.exec()
        self.__load_db()

    def __deleting_student(self) -> None:
        delete_form = DeleteForm(self.db)
        delete_form.exec()
        self.__load_db()

    def __search_students(self) -> None:
        search_form = SearchForm(self.db)
        search_form.exec()