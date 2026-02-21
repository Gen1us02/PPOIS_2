# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1350, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.work_tab_widget = QTabWidget(self.centralwidget)
        self.work_tab_widget.setObjectName(u"work_tab_widget")
        self.work_tab_widget.setMaximumSize(QSize(245, 16777215))
        self.data_load_tab = QWidget()
        self.data_load_tab.setObjectName(u"data_load_tab")
        self.verticalLayout_2 = QVBoxLayout(self.data_load_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.data_load_frame = QFrame(self.data_load_tab)
        self.data_load_frame.setObjectName(u"data_load_frame")
        self.data_load_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.data_load_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.data_load_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.data_load_label = QLabel(self.data_load_frame)
        self.data_load_label.setObjectName(u"data_load_label")
        self.data_load_label.setMinimumSize(QSize(0, 0))
        self.data_load_label.setMaximumSize(QSize(16777215, 70))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        self.data_load_label.setFont(font)
        self.data_load_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.data_load_label)

        self.load_file_button = QPushButton(self.data_load_frame)
        self.load_file_button.setObjectName(u"load_file_button")
        self.load_file_button.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_4.addWidget(self.load_file_button)

        self.load_database_button = QPushButton(self.data_load_frame)
        self.load_database_button.setObjectName(u"load_database_button")
        self.load_database_button.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_4.addWidget(self.load_database_button)


        self.verticalLayout_2.addWidget(self.data_load_frame)

        self.work_tab_widget.addTab(self.data_load_tab, "")
        self.data_work_tab = QWidget()
        self.data_work_tab.setObjectName(u"data_work_tab")
        self.horizontalLayout_2 = QHBoxLayout(self.data_work_tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.control_frame = QFrame(self.data_work_tab)
        self.control_frame.setObjectName(u"control_frame")
        self.control_frame.setMinimumSize(QSize(222, 300))
        self.control_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.control_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.control_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.db_work_label = QLabel(self.control_frame)
        self.db_work_label.setObjectName(u"db_work_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.db_work_label.sizePolicy().hasHeightForWidth())
        self.db_work_label.setSizePolicy(sizePolicy)
        self.db_work_label.setMinimumSize(QSize(0, 100))
        self.db_work_label.setMaximumSize(QSize(16777215, 100))
        self.db_work_label.setFont(font)
        self.db_work_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.db_work_label)

        self.search_students_button = QPushButton(self.control_frame)
        self.search_students_button.setObjectName(u"search_students_button")
        self.search_students_button.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.search_students_button)

        self.show_tree_button = QPushButton(self.control_frame)
        self.show_tree_button.setObjectName(u"show_tree_button")
        self.show_tree_button.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.show_tree_button)

        self.hide_tree_button = QPushButton(self.control_frame)
        self.hide_tree_button.setObjectName(u"hide_tree_button")
        self.hide_tree_button.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.hide_tree_button)

        self.delete_students_button = QPushButton(self.control_frame)
        self.delete_students_button.setObjectName(u"delete_students_button")
        self.delete_students_button.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.delete_students_button)

        self.add_students_button = QPushButton(self.control_frame)
        self.add_students_button.setObjectName(u"add_students_button")
        self.add_students_button.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.add_students_button)


        self.horizontalLayout_2.addWidget(self.control_frame)

        self.work_tab_widget.addTab(self.data_work_tab, "")

        self.horizontalLayout.addWidget(self.work_tab_widget)

        self.table_tab_widget = QTabWidget(self.centralwidget)
        self.table_tab_widget.setObjectName(u"table_tab_widget")
        self.no_data_tab = QWidget()
        self.no_data_tab.setObjectName(u"no_data_tab")
        self.verticalLayout_5 = QVBoxLayout(self.no_data_tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.no_data_label_main = QLabel(self.no_data_tab)
        self.no_data_label_main.setObjectName(u"no_data_label_main")
        self.no_data_label_main.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.no_data_label_main)

        self.table_tab_widget.addTab(self.no_data_tab, "")
        self.student_tree_tab = QWidget()
        self.student_tree_tab.setObjectName(u"student_tree_tab")
        self.horizontalLayout_5 = QHBoxLayout(self.student_tree_tab)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.students_tree = QTreeWidget(self.student_tree_tab)
        self.students_tree.setObjectName(u"students_tree")

        self.horizontalLayout_5.addWidget(self.students_tree)

        self.table_tab_widget.addTab(self.student_tree_tab, "")
        self.student_table_tab = QWidget()
        self.student_table_tab.setObjectName(u"student_table_tab")
        self.horizontalLayout_4 = QHBoxLayout(self.student_table_tab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.table_frame_main = QFrame(self.student_table_tab)
        self.table_frame_main.setObjectName(u"table_frame_main")
        self.table_frame_main.setMinimumSize(QSize(800, 300))
        self.table_frame_main.setMaximumSize(QSize(16777215, 16777215))
        self.table_frame_main.setFrameShape(QFrame.Shape.StyledPanel)
        self.table_frame_main.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.table_frame_main)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.student_table = QTableWidget(self.table_frame_main)
        if (self.student_table.columnCount() < 3):
            self.student_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.student_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.student_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.student_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.student_table.rowCount() < 1):
            self.student_table.setRowCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.student_table.setVerticalHeaderItem(0, __qtablewidgetitem3)
        self.student_table.setObjectName(u"student_table")
        self.student_table.setEnabled(True)
        self.student_table.setMinimumSize(QSize(0, 100))
        self.student_table.horizontalHeader().setCascadingSectionResizes(True)
        self.student_table.horizontalHeader().setMinimumSectionSize(30)
        self.student_table.horizontalHeader().setDefaultSectionSize(170)
        self.student_table.horizontalHeader().setHighlightSections(True)
        self.student_table.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.student_table.horizontalHeader().setStretchLastSection(True)
        self.student_table.verticalHeader().setCascadingSectionResizes(True)
        self.student_table.verticalHeader().setMinimumSectionSize(24)
        self.student_table.verticalHeader().setDefaultSectionSize(30)
        self.student_table.verticalHeader().setProperty(u"showSortIndicator", True)
        self.student_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_3.addWidget(self.student_table)

        self.pagination_frame_main = QFrame(self.table_frame_main)
        self.pagination_frame_main.setObjectName(u"pagination_frame_main")
        self.pagination_frame_main.setMinimumSize(QSize(0, 50))
        self.pagination_frame_main.setFrameShape(QFrame.Shape.StyledPanel)
        self.pagination_frame_main.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.pagination_frame_main)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.items_count = QComboBox(self.pagination_frame_main)
        self.items_count.addItem("")
        self.items_count.addItem("")
        self.items_count.addItem("")
        self.items_count.setObjectName(u"items_count")
        self.items_count.setMinimumSize(QSize(200, 0))
        self.items_count.setMaximumSize(QSize(230, 16777215))

        self.horizontalLayout_3.addWidget(self.items_count)

        self.prev_page_button_main = QPushButton(self.pagination_frame_main)
        self.prev_page_button_main.setObjectName(u"prev_page_button_main")
        self.prev_page_button_main.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_3.addWidget(self.prev_page_button_main)

        self.first_page_button_main = QPushButton(self.pagination_frame_main)
        self.first_page_button_main.setObjectName(u"first_page_button_main")
        self.first_page_button_main.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_3.addWidget(self.first_page_button_main)

        self.current_page = QLabel(self.pagination_frame_main)
        self.current_page.setObjectName(u"current_page")
        self.current_page.setMinimumSize(QSize(0, 0))
        self.current_page.setMaximumSize(QSize(50, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(11)
        self.current_page.setFont(font1)
        self.current_page.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.current_page)

        self.last_page_button_main = QPushButton(self.pagination_frame_main)
        self.last_page_button_main.setObjectName(u"last_page_button_main")
        self.last_page_button_main.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_3.addWidget(self.last_page_button_main)

        self.next_page_button_main = QPushButton(self.pagination_frame_main)
        self.next_page_button_main.setObjectName(u"next_page_button_main")
        self.next_page_button_main.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_3.addWidget(self.next_page_button_main)


        self.verticalLayout_3.addWidget(self.pagination_frame_main)


        self.horizontalLayout_4.addWidget(self.table_frame_main)

        self.table_tab_widget.addTab(self.student_table_tab, "")

        self.horizontalLayout.addWidget(self.table_tab_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.work_tab_widget.setCurrentIndex(1)
        self.table_tab_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.data_load_label.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.load_file_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437 \u0444\u0430\u0439\u043b\u0430", None))
        self.load_database_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437 \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.work_tab_widget.setTabText(self.work_tab_widget.indexOf(self.data_load_tab), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.db_work_label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u0430 \u0441 \u0437\u0430\u043f\u0438\u0441\u044f\u043c\u0438", None))
        self.search_students_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u043e\u0432", None))
        self.show_tree_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0434\u0435\u0440\u0435\u0432\u043e \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u043e\u0432", None))
        self.hide_tree_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0440\u044b\u0442\u044c \u0434\u0435\u0440\u0435\u0432\u043e \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u043e\u0432", None))
        self.delete_students_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u043e\u0432", None))
        self.add_students_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u043e\u0432", None))
        self.work_tab_widget.setTabText(self.work_tab_widget.indexOf(self.data_work_tab), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u0430 \u0441 \u0437\u0430\u043f\u0438\u0441\u044f\u043c\u0438", None))
        self.no_data_label_main.setText("")
        self.table_tab_widget.setTabText(self.table_tab_widget.indexOf(self.no_data_tab), QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.table_tab_widget.setTabText(self.table_tab_widget.indexOf(self.student_tree_tab), QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0440\u0435\u0432\u043e \u0437\u0430\u043f\u0438\u0441\u0435\u0439", None))
        ___qtablewidgetitem = self.student_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None));
        ___qtablewidgetitem1 = self.student_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u0430", None));
        ___qtablewidgetitem2 = self.student_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0437\u0430\u043c\u0435\u043d\u044b", None));
        self.items_count.setItemText(0, QCoreApplication.translate("MainWindow", u"5", None))
        self.items_count.setItemText(1, QCoreApplication.translate("MainWindow", u"10", None))
        self.items_count.setItemText(2, QCoreApplication.translate("MainWindow", u"15", None))

        self.items_count.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435", None))
        self.prev_page_button_main.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.first_page_button_main.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0432\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
        self.current_page.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.last_page_button_main.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u044f\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
        self.next_page_button_main.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.table_tab_widget.setTabText(self.table_tab_widget.indexOf(self.student_table_tab), QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430", None))
    # retranslateUi

