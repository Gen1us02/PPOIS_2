from PySide6.QtWidgets import (
    QMainWindow,
    QTableWidgetItem,
    QTableWidget,
    QTreeWidgetItem,
    QHeaderView,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from src.interface.ui.main_window_ui import Ui_MainWindow
from src.db.db_manager import DBManager
from src.utils.paginator import Paginator
from .adding_form import AddForm
from .deleting_form import DeleteForm
from .search_form import SearchForm
from collections import defaultdict


class MainWindow(QMainWindow):
    def __init__(self, db_manager: DBManager) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = db_manager
        self.students = []
        self.paginator = Paginator(db_manager, self.ui)
        self.setWindowTitle("Главное окно")

        self.__no_data_setup()
        self.__setup_table()
        self.__tabs_selection()
        self.ui.hide_tree_button.hide()

        self.ui.first_page_button_main.clicked.connect(
            lambda: self.paginator.return_to_first_page(self.students)
        )
        self.ui.last_page_button_main.clicked.connect(
            lambda: self.paginator.return_to_last_page(self.students)
        )
        self.ui.load_database_button.clicked.connect(self.__load_db)
        self.ui.load_file_button.clicked.connect(self.__load_file)
        self.ui.next_page_button_main.clicked.connect(
            lambda: self.paginator.next_page(self.students)
        )
        self.ui.prev_page_button_main.clicked.connect(
            lambda: self.paginator.prev_page(self.students)
        )
        self.ui.items_count.currentTextChanged.connect(
            lambda text: self.paginator.update_items_count(text, self.students)
        )
        self.ui.add_students_button.clicked.connect(self.__adding_student)
        self.ui.delete_students_button.clicked.connect(self.__deleting_student)
        self.ui.search_students_button.clicked.connect(self.__search_students)
        self.ui.show_tree_button.clicked.connect(self.__create_tree)
        self.ui.hide_tree_button.clicked.connect(self.__hide_tree)

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
        self.ui.hide_tree_button.hide()

        students = self.db.get_all_records()
        self.students = students
        self.paginator.update_max_page(self.students)
        self.paginator.display_current_page(self.students)

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

    def __create_tree(self) -> None:
        tree = self.ui.students_tree
        tree.setHeaderLabel("Дерево студентов")
        tree.header().setDefaultAlignment(Qt.AlignCenter)
        font = tree.header().font()
        font.setPointSize(12)
        font.setBold(True)
        tree.header().setFont(font)
        tree.clear()

        students_in_groups = defaultdict(list)
        for student in self.students:
            group_num = student.group.number
            students_in_groups[group_num].append(student)

        for group, students in students_in_groups.items():
            group_item = QTreeWidgetItem(tree)
            group_item.setText(0, group)

            for student in students:
                student_item = QTreeWidgetItem(group_item)
                student_item.setText(0, student.full_name)

        tree.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        tree.header().setStretchLastSection(False)
        tree.expandAll()
        self.ui.table_tab_widget.setCurrentWidget(self.ui.student_tree_tab)
        self.ui.show_tree_button.hide()
        self.ui.hide_tree_button.show()

    def __hide_tree(self) -> None:
        self.ui.show_tree_button.show()
        self.ui.hide_tree_button.hide()
        self.ui.table_tab_widget.setCurrentWidget(self.ui.student_table_tab)
