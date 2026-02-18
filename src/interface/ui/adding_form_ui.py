# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adding_form.ui'
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
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_AddWindow(object):
    def setupUi(self, AddWindow):
        if not AddWindow.objectName():
            AddWindow.setObjectName(u"AddWindow")
        AddWindow.resize(400, 550)
        AddWindow.setMinimumSize(QSize(400, 550))
        AddWindow.setMaximumSize(QSize(400, 550))
        self.centralwidget = QWidget(AddWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(300, 300))
        self.frame.setMaximumSize(QSize(16777215, 1677215))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 9, -1, 9)
        self.student_add_lable = QLabel(self.frame)
        self.student_add_lable.setObjectName(u"student_add_lable")
        self.student_add_lable.setMaximumSize(QSize(16777215, 30))
        self.student_add_lable.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.student_add_lable)

        self.last_name = QLineEdit(self.frame)
        self.last_name.setObjectName(u"last_name")
        self.last_name.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.last_name)

        self.first_name = QLineEdit(self.frame)
        self.first_name.setObjectName(u"first_name")
        self.first_name.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.first_name)

        self.middle_name = QLineEdit(self.frame)
        self.middle_name.setObjectName(u"middle_name")
        self.middle_name.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.middle_name)

        self.groups = QComboBox(self.frame)
        self.groups.setObjectName(u"groups")
        self.groups.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.groups)

        self.exam_container = QWidget(self.frame)
        self.exam_container.setObjectName(u"exam_container")

        self.verticalLayout.addWidget(self.exam_container)


        self.verticalLayout_2.addWidget(self.frame)

        self.button_frame = QFrame(self.centralwidget)
        self.button_frame.setObjectName(u"button_frame")
        self.button_frame.setMaximumSize(QSize(16777215, 70))
        self.button_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.button_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.button_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_button = QPushButton(self.button_frame)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setMinimumSize(QSize(40, 40))
        self.add_button.setMaximumSize(QSize(360, 50))

        self.horizontalLayout.addWidget(self.add_button)


        self.verticalLayout_2.addWidget(self.button_frame)

        AddWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddWindow)

        QMetaObject.connectSlotsByName(AddWindow)
    # setupUi

    def retranslateUi(self, AddWindow):
        AddWindow.setWindowTitle(QCoreApplication.translate("AddWindow", u"MainWindow", None))
        self.student_add_lable.setText(QCoreApplication.translate("AddWindow", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0430", None))
        self.last_name.setText("")
        self.last_name.setPlaceholderText(QCoreApplication.translate("AddWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.first_name.setText("")
        self.first_name.setPlaceholderText(QCoreApplication.translate("AddWindow", u"\u0418\u043c\u044f", None))
        self.middle_name.setText("")
        self.middle_name.setPlaceholderText(QCoreApplication.translate("AddWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.groups.setPlaceholderText(QCoreApplication.translate("AddWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0433\u0440\u0443\u043f\u043f\u044b", None))
        self.add_button.setText(QCoreApplication.translate("AddWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0430", None))
    # retranslateUi

