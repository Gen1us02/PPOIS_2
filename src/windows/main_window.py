from PySide6.QtWidgets import QMainWindow
from src.interface.ui.main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__setup_table()

        self.__tabs_selection()

    def __setup_table(self):
        pass

    def __tabs_selection(self):
        self.ui.work_tab_widget.setCurrentWidget(self.ui.data_load_tab)
        self.ui.table_tab_widget.setCurrentWidget(self.ui.no_data_tab)
