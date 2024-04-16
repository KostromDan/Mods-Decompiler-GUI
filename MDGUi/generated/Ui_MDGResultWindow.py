# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MDGResultWindow.ui'
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
    QMenuBar, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)
from . import resources_rc

class Ui_MDGResultWindow(object):
    def setupUi(self, MDGResultWindow):
        if not MDGResultWindow.objectName():
            MDGResultWindow.setObjectName(u"MDGResultWindow")
        MDGResultWindow.resize(800, 418)
        MDGResultWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/images/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MDGResultWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MDGResultWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_text_edit = QTextEdit(self.centralwidget)
        self.result_text_edit.setObjectName(u"result_text_edit")
        self.result_text_edit.setReadOnly(True)

        self.verticalLayout.addWidget(self.result_text_edit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.deobfuscated_mods_button = QPushButton(self.centralwidget)
        self.deobfuscated_mods_button.setObjectName(u"deobfuscated_mods_button")

        self.horizontalLayout.addWidget(self.deobfuscated_mods_button)

        self.decompiled_mods_button = QPushButton(self.centralwidget)
        self.decompiled_mods_button.setObjectName(u"decompiled_mods_button")

        self.horizontalLayout.addWidget(self.decompiled_mods_button)

        self.merged_mdk_button = QPushButton(self.centralwidget)
        self.merged_mdk_button.setObjectName(u"merged_mdk_button")

        self.horizontalLayout.addWidget(self.merged_mdk_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.intellij_idea_button = QPushButton(self.centralwidget)
        self.intellij_idea_button.setObjectName(u"intellij_idea_button")

        self.horizontalLayout_3.addWidget(self.intellij_idea_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.close_button = QPushButton(self.centralwidget)
        self.close_button.setObjectName(u"close_button")

        self.horizontalLayout_2.addWidget(self.close_button)

        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setObjectName(u"exit_button")

        self.horizontalLayout_2.addWidget(self.exit_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MDGResultWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MDGResultWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MDGResultWindow.setMenuBar(self.menubar)

        self.retranslateUi(MDGResultWindow)

        QMetaObject.connectSlotsByName(MDGResultWindow)
    # setupUi

    def retranslateUi(self, MDGResultWindow):
        MDGResultWindow.setWindowTitle(QCoreApplication.translate("MDGResultWindow", u"MDGResltWindow", None))
        self.result_text_edit.setHtml(QCoreApplication.translate("MDGResultWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Finished with success:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Thanks for using this tool. We hope that it has made your life more convenient.<br />Now you can:</p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt"
                        "-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Open result folders you are interested in.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Open in IntelliJ IDEA as project merged_mdk.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Exit program using exit button.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Return to previous window using close button.</li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Errors:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></ht"
                        "ml>", None))
        self.label.setText(QCoreApplication.translate("MDGResultWindow", u"Open folders:", None))
        self.deobfuscated_mods_button.setText(QCoreApplication.translate("MDGResultWindow", u"deobfuscated_mods", None))
        self.decompiled_mods_button.setText(QCoreApplication.translate("MDGResultWindow", u"decompiled_mods", None))
        self.merged_mdk_button.setText(QCoreApplication.translate("MDGResultWindow", u"merged_mdk", None))
        self.label_2.setText(QCoreApplication.translate("MDGResultWindow", u"Open in IntelliJ IDEA as project:", None))
        self.intellij_idea_button.setText(QCoreApplication.translate("MDGResultWindow", u"merged_mdk", None))
        self.close_button.setText(QCoreApplication.translate("MDGResultWindow", u"close", None))
        self.exit_button.setText(QCoreApplication.translate("MDGResultWindow", u"exit", None))
    # retranslateUi

