# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_form.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDialog,
    QDoubleSpinBox, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpinBox, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_SearchForm(object):
    def setupUi(self, SearchForm):
        if not SearchForm.objectName():
            SearchForm.setObjectName(u"SearchForm")
        SearchForm.resize(1070, 600)
        self.horizontalLayout_3 = QHBoxLayout(SearchForm)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.filters_frame = QFrame(SearchForm)
        self.filters_frame.setObjectName(u"filters_frame")
        self.filters_frame.setMinimumSize(QSize(0, 300))
        self.filters_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.filters_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.filters_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 50)
        self.search_label = QLabel(self.filters_frame)
        self.search_label.setObjectName(u"search_label")
        self.search_label.setMaximumSize(QSize(16777215, 30))
        self.search_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.search_label)

        self.avg_rating_label = QLabel(self.filters_frame)
        self.avg_rating_label.setObjectName(u"avg_rating_label")
        self.avg_rating_label.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.avg_rating_label)

        self.avg_rating_widget = QWidget(self.filters_frame)
        self.avg_rating_widget.setObjectName(u"avg_rating_widget")
        self.avg_rating_widget.setMinimumSize(QSize(0, 70))
        self.avg_rating_widget.setMaximumSize(QSize(16777215, 60))
        self.gridLayout_6 = QGridLayout(self.avg_rating_widget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setVerticalSpacing(0)
        self.avg_min_label = QLabel(self.avg_rating_widget)
        self.avg_min_label.setObjectName(u"avg_min_label")
        self.avg_min_label.setMinimumSize(QSize(10, 10))
        self.avg_min_label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_6.addWidget(self.avg_min_label, 0, 0, 1, 1)

        self.avg_max_label = QLabel(self.avg_rating_widget)
        self.avg_max_label.setObjectName(u"avg_max_label")
        self.avg_max_label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_6.addWidget(self.avg_max_label, 0, 1, 1, 1)

        self.avg_rating_max = QDoubleSpinBox(self.avg_rating_widget)
        self.avg_rating_max.setObjectName(u"avg_rating_max")
        self.avg_rating_max.setMinimumSize(QSize(0, 30))
        self.avg_rating_max.setDecimals(1)
        self.avg_rating_max.setMaximum(10.000000000000000)
        self.avg_rating_max.setSingleStep(0.100000000000000)
        self.avg_rating_max.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_6.addWidget(self.avg_rating_max, 1, 1, 1, 1)

        self.avg_rating_min = QDoubleSpinBox(self.avg_rating_widget)
        self.avg_rating_min.setObjectName(u"avg_rating_min")
        self.avg_rating_min.setMinimumSize(QSize(0, 30))
        self.avg_rating_min.setDecimals(1)
        self.avg_rating_min.setMaximum(10.000000000000000)
        self.avg_rating_min.setSingleStep(0.100000000000000)

        self.gridLayout_6.addWidget(self.avg_rating_min, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.avg_rating_widget)

        self.rating_label = QLabel(self.filters_frame)
        self.rating_label.setObjectName(u"rating_label")
        self.rating_label.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.rating_label)

        self.rating_widget = QWidget(self.filters_frame)
        self.rating_widget.setObjectName(u"rating_widget")
        self.rating_widget.setMinimumSize(QSize(0, 70))
        self.rating_widget.setMaximumSize(QSize(16777215, 60))
        self.gridLayout_5 = QGridLayout(self.rating_widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(0)
        self.rating_min_label = QLabel(self.rating_widget)
        self.rating_min_label.setObjectName(u"rating_min_label")
        self.rating_min_label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_5.addWidget(self.rating_min_label, 1, 0, 1, 1)

        self.rating_max_label = QLabel(self.rating_widget)
        self.rating_max_label.setObjectName(u"rating_max_label")
        self.rating_max_label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_5.addWidget(self.rating_max_label, 1, 1, 1, 1)

        self.rating_min = QSpinBox(self.rating_widget)
        self.rating_min.setObjectName(u"rating_min")
        self.rating_min.setMinimumSize(QSize(0, 30))
        self.rating_min.setMaximum(10)

        self.gridLayout_5.addWidget(self.rating_min, 2, 0, 1, 1)

        self.rating_max = QSpinBox(self.rating_widget)
        self.rating_max.setObjectName(u"rating_max")
        self.rating_max.setMinimumSize(QSize(0, 30))
        self.rating_max.setMaximum(10)

        self.gridLayout_5.addWidget(self.rating_max, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.rating_widget)

        self.groups_list = QComboBox(self.filters_frame)
        self.groups_list.setObjectName(u"groups_list")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groups_list.sizePolicy().hasHeightForWidth())
        self.groups_list.setSizePolicy(sizePolicy)
        self.groups_list.setMinimumSize(QSize(0, 30))
        self.groups_list.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.groups_list)

        self.subject_list = QComboBox(self.filters_frame)
        self.subject_list.setObjectName(u"subject_list")
        sizePolicy.setHeightForWidth(self.subject_list.sizePolicy().hasHeightForWidth())
        self.subject_list.setSizePolicy(sizePolicy)
        self.subject_list.setMinimumSize(QSize(0, 30))
        self.subject_list.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.subject_list)

        self.search_students = QPushButton(self.filters_frame)
        self.search_students.setObjectName(u"search_students")
        self.search_students.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.search_students)


        self.horizontalLayout_3.addWidget(self.filters_frame)

        self.tabWidget = QTabWidget(SearchForm)
        self.tabWidget.setObjectName(u"tabWidget")
        self.no_data_search_tab = QWidget()
        self.no_data_search_tab.setObjectName(u"no_data_search_tab")
        self.verticalLayout_3 = QVBoxLayout(self.no_data_search_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.no_data_label = QLabel(self.no_data_search_tab)
        self.no_data_label.setObjectName(u"no_data_label")
        self.no_data_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.no_data_label)

        self.tabWidget.addTab(self.no_data_search_tab, "")
        self.students_search_table_tab = QWidget()
        self.students_search_table_tab.setObjectName(u"students_search_table_tab")
        self.horizontalLayout = QHBoxLayout(self.students_search_table_tab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.table_frame = QFrame(self.students_search_table_tab)
        self.table_frame.setObjectName(u"table_frame")
        self.table_frame.setMinimumSize(QSize(800, 300))
        self.table_frame.setMaximumSize(QSize(16777215, 16777215))
        self.table_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.table_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.table_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.table_widget = QTableWidget(self.table_frame)
        if (self.table_widget.columnCount() < 3):
            self.table_widget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.table_widget.rowCount() < 1):
            self.table_widget.setRowCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_widget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        self.table_widget.setObjectName(u"table_widget")
        self.table_widget.setEnabled(True)
        self.table_widget.setMinimumSize(QSize(0, 100))
        self.table_widget.horizontalHeader().setCascadingSectionResizes(True)
        self.table_widget.horizontalHeader().setMinimumSectionSize(30)
        self.table_widget.horizontalHeader().setDefaultSectionSize(170)
        self.table_widget.horizontalHeader().setHighlightSections(True)
        self.table_widget.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.verticalHeader().setCascadingSectionResizes(True)
        self.table_widget.verticalHeader().setMinimumSectionSize(24)
        self.table_widget.verticalHeader().setDefaultSectionSize(30)
        self.table_widget.verticalHeader().setProperty(u"showSortIndicator", True)
        self.table_widget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.table_widget)

        self.pagination_frame = QFrame(self.table_frame)
        self.pagination_frame.setObjectName(u"pagination_frame")
        self.pagination_frame.setMinimumSize(QSize(0, 50))
        self.pagination_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.pagination_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.pagination_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.items_count = QComboBox(self.pagination_frame)
        self.items_count.addItem("")
        self.items_count.addItem("")
        self.items_count.addItem("")
        self.items_count.setObjectName(u"items_count")
        self.items_count.setMinimumSize(QSize(200, 0))
        self.items_count.setMaximumSize(QSize(230, 16777215))

        self.horizontalLayout_2.addWidget(self.items_count)

        self.prev_page_button = QPushButton(self.pagination_frame)
        self.prev_page_button.setObjectName(u"prev_page_button")
        self.prev_page_button.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_2.addWidget(self.prev_page_button)

        self.first_page_button = QPushButton(self.pagination_frame)
        self.first_page_button.setObjectName(u"first_page_button")
        self.first_page_button.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_2.addWidget(self.first_page_button)

        self.current_page = QLabel(self.pagination_frame)
        self.current_page.setObjectName(u"current_page")
        self.current_page.setMinimumSize(QSize(0, 0))
        self.current_page.setMaximumSize(QSize(50, 16777215))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(11)
        self.current_page.setFont(font)
        self.current_page.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.current_page)

        self.last_page_button = QPushButton(self.pagination_frame)
        self.last_page_button.setObjectName(u"last_page_button")
        self.last_page_button.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_2.addWidget(self.last_page_button)

        self.next_page_button = QPushButton(self.pagination_frame)
        self.next_page_button.setObjectName(u"next_page_button")
        self.next_page_button.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_2.addWidget(self.next_page_button)


        self.verticalLayout_2.addWidget(self.pagination_frame)


        self.horizontalLayout.addWidget(self.table_frame)

        self.tabWidget.addTab(self.students_search_table_tab, "")

        self.horizontalLayout_3.addWidget(self.tabWidget)


        self.retranslateUi(SearchForm)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SearchForm)
    # setupUi

    def retranslateUi(self, SearchForm):
        SearchForm.setWindowTitle(QCoreApplication.translate("SearchForm", u"Dialog", None))
        self.search_label.setText(QCoreApplication.translate("SearchForm", u"\u041f\u043e\u0438\u0441\u043a \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u043e\u0432", None))
        self.avg_rating_label.setText(QCoreApplication.translate("SearchForm", u"\u0421\u0440\u0435\u0434\u043d\u0438\u0439 \u0431\u0430\u043b\u043b \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0430", None))
        self.avg_min_label.setText(QCoreApplication.translate("SearchForm", u"\u041d\u0438\u0436\u043d\u0438\u0439 \u043f\u0440\u0435\u0434\u0435\u043b", None))
        self.avg_max_label.setText(QCoreApplication.translate("SearchForm", u"\u0412\u0435\u0440\u0445\u043d\u0438\u0439 \u043f\u0440\u0435\u0434\u0435\u043b", None))
        self.rating_label.setText(QCoreApplication.translate("SearchForm", u"\u0411\u0430\u043b\u043b \u043f\u043e \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0443", None))
        self.rating_min_label.setText(QCoreApplication.translate("SearchForm", u"\u041d\u0438\u0436\u043d\u0438\u0439 \u043f\u0440\u0435\u0434\u0435\u043b", None))
        self.rating_max_label.setText(QCoreApplication.translate("SearchForm", u"\u0412\u0435\u0440\u0445\u043d\u0438\u0439 \u043f\u0440\u0435\u0434\u0435\u043b", None))
        self.groups_list.setPlaceholderText(QCoreApplication.translate("SearchForm", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0433\u0440\u0443\u043f\u043f", None))
        self.subject_list.setPlaceholderText(QCoreApplication.translate("SearchForm", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u043e\u0432", None))
        self.search_students.setText(QCoreApplication.translate("SearchForm", u"\u041f\u043e\u0438\u0441\u043a \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u043e\u0432", None))
        self.no_data_label.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.no_data_search_tab), QCoreApplication.translate("SearchForm", u"\u041d\u0435\u0442 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        ___qtablewidgetitem = self.table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SearchForm", u"\u0424\u0418\u041e", None));
        ___qtablewidgetitem1 = self.table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SearchForm", u"\u0413\u0440\u0443\u043f\u043f\u0430", None));
        ___qtablewidgetitem2 = self.table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SearchForm", u"\u042d\u043a\u0437\u0430\u043c\u0435\u043d\u044b", None));
        self.items_count.setItemText(0, QCoreApplication.translate("SearchForm", u"5", None))
        self.items_count.setItemText(1, QCoreApplication.translate("SearchForm", u"10", None))
        self.items_count.setItemText(2, QCoreApplication.translate("SearchForm", u"15", None))

        self.items_count.setPlaceholderText(QCoreApplication.translate("SearchForm", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435", None))
        self.prev_page_button.setText(QCoreApplication.translate("SearchForm", u"<", None))
        self.first_page_button.setText(QCoreApplication.translate("SearchForm", u"\u041f\u0435\u0440\u0432\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
        self.current_page.setText(QCoreApplication.translate("SearchForm", u"1", None))
        self.last_page_button.setText(QCoreApplication.translate("SearchForm", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u044f\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
        self.next_page_button.setText(QCoreApplication.translate("SearchForm", u">", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.students_search_table_tab), QCoreApplication.translate("SearchForm", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0445 \u0437\u0430\u043f\u0438\u0441\u0435\u0439", None))
    # retranslateUi

