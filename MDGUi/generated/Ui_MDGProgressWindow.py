# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MDGProgressWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)
from . import resources_rc

class Ui_MDGProgressWindow(object):
    def setupUi(self, MDGProgressWindow):
        if not MDGProgressWindow.objectName():
            MDGProgressWindow.setObjectName(u"MDGProgressWindow")
        MDGProgressWindow.resize(1100, 546)
        MDGProgressWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/images/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MDGProgressWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MDGProgressWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout.addWidget(self.label_9)

        self.init_progress_bar = QProgressBar(self.centralwidget)
        self.init_progress_bar.setObjectName(u"init_progress_bar")
        self.init_progress_bar.setValue(0)
        self.init_progress_bar.setTextVisible(False)

        self.horizontalLayout.addWidget(self.init_progress_bar)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.copy_progress_bar = QProgressBar(self.centralwidget)
        self.copy_progress_bar.setObjectName(u"copy_progress_bar")
        self.copy_progress_bar.setValue(0)
        self.copy_progress_bar.setTextVisible(False)

        self.horizontalLayout.addWidget(self.copy_progress_bar)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.mdk_init_progress_bar = QProgressBar(self.centralwidget)
        self.mdk_init_progress_bar.setObjectName(u"mdk_init_progress_bar")
        self.mdk_init_progress_bar.setValue(0)
        self.mdk_init_progress_bar.setTextVisible(False)

        self.horizontalLayout.addWidget(self.mdk_init_progress_bar)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.deobf_progress_bar = QProgressBar(self.centralwidget)
        self.deobf_progress_bar.setObjectName(u"deobf_progress_bar")
        self.deobf_progress_bar.setValue(0)
        self.deobf_progress_bar.setTextVisible(False)

        self.horizontalLayout.addWidget(self.deobf_progress_bar)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.decomp_progress_bar = QProgressBar(self.centralwidget)
        self.decomp_progress_bar.setObjectName(u"decomp_progress_bar")
        self.decomp_progress_bar.setValue(0)
        self.decomp_progress_bar.setTextVisible(False)

        self.horizontalLayout.addWidget(self.decomp_progress_bar)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.merge_progress_bar = QProgressBar(self.centralwidget)
        self.merge_progress_bar.setObjectName(u"merge_progress_bar")
        self.merge_progress_bar.setValue(0)
        self.merge_progress_bar.setTextVisible(False)

        self.horizontalLayout.addWidget(self.merge_progress_bar)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout.addWidget(self.label_8)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.currently_label = QLabel(self.centralwidget)
        self.currently_label.setObjectName(u"currently_label")

        self.horizontalLayout_3.addWidget(self.currently_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.logger_text_edit = QTextEdit(self.centralwidget)
        self.logger_text_edit.setObjectName(u"logger_text_edit")
        self.logger_text_edit.setReadOnly(True)

        self.verticalLayout.addWidget(self.logger_text_edit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.open_log_button = QPushButton(self.centralwidget)
        self.open_log_button.setObjectName(u"open_log_button")

        self.horizontalLayout_2.addWidget(self.open_log_button)

        self.stop_button = QPushButton(self.centralwidget)
        self.stop_button.setObjectName(u"stop_button")

        self.horizontalLayout_2.addWidget(self.stop_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MDGProgressWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MDGProgressWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1100, 22))
        MDGProgressWindow.setMenuBar(self.menubar)

        self.retranslateUi(MDGProgressWindow)

        QMetaObject.connectSlotsByName(MDGProgressWindow)
    # setupUi

    def retranslateUi(self, MDGProgressWindow):
        MDGProgressWindow.setWindowTitle(QCoreApplication.translate("MDGProgressWindow", u"MDGProgressWindow", None))
        self.label_9.setText(QCoreApplication.translate("MDGProgressWindow", u"init", None))
#if QT_CONFIG(accessibility)
        self.init_progress_bar.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label.setText(QCoreApplication.translate("MDGProgressWindow", u"copy", None))
#if QT_CONFIG(accessibility)
        self.copy_progress_bar.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label_4.setText(QCoreApplication.translate("MDGProgressWindow", u"mdk init", None))
        self.label_5.setText(QCoreApplication.translate("MDGProgressWindow", u"deobfuscate", None))
        self.label_6.setText(QCoreApplication.translate("MDGProgressWindow", u"decompile", None))
        self.label_7.setText(QCoreApplication.translate("MDGProgressWindow", u"merge", None))
        self.label_8.setText(QCoreApplication.translate("MDGProgressWindow", u"completed", None))
        self.label_2.setText(QCoreApplication.translate("MDGProgressWindow", u"Currently:", None))
        self.currently_label.setText(QCoreApplication.translate("MDGProgressWindow", u"init", None))
#if QT_CONFIG(accessibility)
        self.logger_text_edit.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.open_log_button.setText(QCoreApplication.translate("MDGProgressWindow", u"open full log", None))
        self.stop_button.setText(QCoreApplication.translate("MDGProgressWindow", u"stop", None))
    # retranslateUi

