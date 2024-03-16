# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MDGMdkWindow.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextBrowser, QVBoxLayout, QWidget)
from . import resources_rc

class Ui_MDGMdkWindow(object):
    def setupUi(self, MDGMdkWindow):
        if not MDGMdkWindow.objectName():
            MDGMdkWindow.setObjectName(u"MDGMdkWindow")
        MDGMdkWindow.resize(1380, 930)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MDGMdkWindow.sizePolicy().hasHeightForWidth())
        MDGMdkWindow.setSizePolicy(sizePolicy)
        MDGMdkWindow.setMinimumSize(QSize(0, 0))
        MDGMdkWindow.setMaximumSize(QSize(10000, 16777215))
        self.centralwidget = QWidget(MDGMdkWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mdk_path = QTextBrowser(self.centralwidget)
        self.mdk_path.setObjectName(u"mdk_path")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mdk_path.sizePolicy().hasHeightForWidth())
        self.mdk_path.setSizePolicy(sizePolicy1)
        self.mdk_path.setMinimumSize(QSize(0, 95))
        self.mdk_path.setMaximumSize(QSize(16777215, 95))
        self.mdk_path.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mdk_path.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout.addWidget(self.mdk_path)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setPixmap(QPixmap(u":/images/mdk_instruction.png"))

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.close_button = QPushButton(self.centralwidget)
        self.close_button.setObjectName(u"close_button")

        self.horizontalLayout.addWidget(self.close_button)

        self.forge_button = QPushButton(self.centralwidget)
        self.forge_button.setObjectName(u"forge_button")

        self.horizontalLayout.addWidget(self.forge_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MDGMdkWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MDGMdkWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1380, 22))
        MDGMdkWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MDGMdkWindow)
        self.statusbar.setObjectName(u"statusbar")
        MDGMdkWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MDGMdkWindow)

        QMetaObject.connectSlotsByName(MDGMdkWindow)
    # setupUi

    def retranslateUi(self, MDGMdkWindow):
        MDGMdkWindow.setWindowTitle(QCoreApplication.translate("MDGMdkWindow", u"MDGMdkWindow", None))
        self.mdk_path.setHtml(QCoreApplication.translate("MDGMdkWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">How to download MDK:</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Click on the &quot;open MinecraftForge downloads&quot; button.</li>\n"
"<li styl"
                        "e=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">On the opened page in your web browser, on the left side of the page, select the version of Minecraft you are using.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Click on the &quot;Mdk&quot; button. On versions of Minecraft 1.7.10 and bellow &quot;Mdk&quot; is renamed with &quot;Src&quot;.</li></ol></body></html>", None))
        self.label.setText("")
        self.close_button.setText(QCoreApplication.translate("MDGMdkWindow", u"close", None))
        self.forge_button.setText(QCoreApplication.translate("MDGMdkWindow", u"open MinecraftForge downloads", None))
    # retranslateUi

