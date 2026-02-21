# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deleting_form.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_DeleteForm(object):
    def setupUi(self, DeleteForm):
        if not DeleteForm.objectName():
            DeleteForm.setObjectName(u"DeleteForm")
        DeleteForm.resize(400, 400)
        DeleteForm.setMinimumSize(QSize(400, 400))
        DeleteForm.setMaximumSize(QSize(400, 400))
        self.verticalLayout = QVBoxLayout(DeleteForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.form_frame = QFrame(DeleteForm)
        self.form_frame.setObjectName(u"form_frame")
        self.form_frame.setMinimumSize(QSize(300, 300))
        self.form_frame.setMaximumSize(QSize(16777215, 16777215))
        self.form_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.form_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.form_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.deleting_label = QLabel(self.form_frame)
        self.deleting_label.setObjectName(u"deleting_label")
        self.deleting_label.setMaximumSize(QSize(16777215, 30))
        self.deleting_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.deleting_label)

        self.avg_rating_label = QLabel(self.form_frame)
        self.avg_rating_label.setObjectName(u"avg_rating_label")
        self.avg_rating_label.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.avg_rating_label)

        self.avg_rating_widget = QWidget(self.form_frame)
        self.avg_rating_widget.setObjectName(u"avg_rating_widget")
        self.avg_rating_widget.setMaximumSize(QSize(16777215, 60))
        self.gridLayout = QGridLayout(self.avg_rating_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.avg_rating_min = QDoubleSpinBox(self.avg_rating_widget)
        self.avg_rating_min.setObjectName(u"avg_rating_min")
        self.avg_rating_min.setDecimals(1)
        self.avg_rating_min.setMaximum(10.000000000000000)
        self.avg_rating_min.setSingleStep(0.100000000000000)

        self.gridLayout.addWidget(self.avg_rating_min, 1, 0, 1, 1)

        self.avg_rating_max = QDoubleSpinBox(self.avg_rating_widget)
        self.avg_rating_max.setObjectName(u"avg_rating_max")
        self.avg_rating_max.setDecimals(1)
        self.avg_rating_max.setMaximum(10.000000000000000)
        self.avg_rating_max.setSingleStep(0.100000000000000)
        self.avg_rating_max.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.avg_rating_max, 1, 1, 1, 1)

        self.avg_min_label = QLabel(self.avg_rating_widget)
        self.avg_min_label.setObjectName(u"avg_min_label")
        self.avg_min_label.setMinimumSize(QSize(10, 10))
        self.avg_min_label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.avg_min_label, 0, 0, 1, 1)

        self.avg_max_label = QLabel(self.avg_rating_widget)
        self.avg_max_label.setObjectName(u"avg_max_label")
        self.avg_max_label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.avg_max_label, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.avg_rating_widget)

        self.rating_label = QLabel(self.form_frame)
        self.rating_label.setObjectName(u"rating_label")
        self.rating_label.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.rating_label)

        self.rating_widget = QWidget(self.form_frame)
        self.rating_widget.setObjectName(u"rating_widget")
        self.rating_widget.setMaximumSize(QSize(16777215, 60))
        self.gridLayout_2 = QGridLayout(self.rating_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(0)
        self.rating_max_label = QLabel(self.rating_widget)
        self.rating_max_label.setObjectName(u"rating_max_label")
        self.rating_max_label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.rating_max_label, 1, 1, 1, 1)

        self.rating_min_label = QLabel(self.rating_widget)
        self.rating_min_label.setObjectName(u"rating_min_label")
        self.rating_min_label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.rating_min_label, 1, 0, 1, 1)

        self.rating_min = QSpinBox(self.rating_widget)
        self.rating_min.setObjectName(u"rating_min")
        self.rating_min.setMaximum(10)

        self.gridLayout_2.addWidget(self.rating_min, 2, 0, 1, 1)

        self.rating_max = QSpinBox(self.rating_widget)
        self.rating_max.setObjectName(u"rating_max")
        self.rating_max.setMaximum(10)

        self.gridLayout_2.addWidget(self.rating_max, 2, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.rating_widget)

        self.groups_list = QComboBox(self.form_frame)
        self.groups_list.setObjectName(u"groups_list")
        self.groups_list.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.groups_list)

        self.subject_list = QComboBox(self.form_frame)
        self.subject_list.setObjectName(u"subject_list")
        self.subject_list.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.subject_list)


        self.verticalLayout.addWidget(self.form_frame)

        self.delete_button_frame = QFrame(DeleteForm)
        self.delete_button_frame.setObjectName(u"delete_button_frame")
        self.delete_button_frame.setMaximumSize(QSize(16777215, 60))
        self.delete_button_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.delete_button_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.delete_button_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.delete_button = QPushButton(self.delete_button_frame)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setMaximumSize(QSize(360, 40))

        self.horizontalLayout.addWidget(self.delete_button)


        self.verticalLayout.addWidget(self.delete_button_frame)


        self.retranslateUi(DeleteForm)

        QMetaObject.connectSlotsByName(DeleteForm)
    # setupUi

    def retranslateUi(self, DeleteForm):
        DeleteForm.setWindowTitle(QCoreApplication.translate("DeleteForm", u"Dialog", None))
        self.deleting_label.setText(QCoreApplication.translate("DeleteForm", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u043e\u0432", None))
        self.avg_rating_label.setText(QCoreApplication.translate("DeleteForm", u"\u0421\u0440\u0435\u0434\u043d\u0438\u0439 \u0431\u0430\u043b\u043b \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0430", None))
        self.avg_min_label.setText(QCoreApplication.translate("DeleteForm", u"\u041d\u0438\u0436\u043d\u0438\u0439 \u043f\u0440\u0435\u0434\u0435\u043b", None))
        self.avg_max_label.setText(QCoreApplication.translate("DeleteForm", u"\u0412\u0435\u0440\u0445\u043d\u0438\u0439 \u043f\u0440\u0435\u0434\u0435\u043b", None))
        self.rating_label.setText(QCoreApplication.translate("DeleteForm", u"\u0411\u0430\u043b\u043b \u043f\u043e \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0443", None))
        self.rating_max_label.setText(QCoreApplication.translate("DeleteForm", u"\u0412\u0435\u0440\u0445\u043d\u0438\u0439 \u043f\u0440\u0435\u0434\u0435\u043b", None))
        self.rating_min_label.setText(QCoreApplication.translate("DeleteForm", u"\u041d\u0438\u0436\u043d\u0438\u0439 \u043f\u0440\u0435\u0434\u0435\u043b", None))
        self.groups_list.setPlaceholderText(QCoreApplication.translate("DeleteForm", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0433\u0440\u0443\u043f\u043f", None))
        self.subject_list.setPlaceholderText(QCoreApplication.translate("DeleteForm", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u043e\u0432", None))
        self.delete_button.setText(QCoreApplication.translate("DeleteForm", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u043e\u0432", None))
    # retranslateUi

