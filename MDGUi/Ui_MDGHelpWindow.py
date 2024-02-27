# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MDGHelpWindow.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QStatusBar,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MDGHelpWindow(object):
    def setupUi(self, MDGHelpWindow):
        if not MDGHelpWindow.objectName():
            MDGHelpWindow.setObjectName(u"MDGHelpWindow")
        MDGHelpWindow.resize(1200, 947)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MDGHelpWindow.sizePolicy().hasHeightForWidth())
        MDGHelpWindow.setSizePolicy(sizePolicy)
        MDGHelpWindow.setMinimumSize(QSize(1200, 0))
        MDGHelpWindow.setMaximumSize(QSize(1200, 16777215))
        self.centralwidget = QWidget(MDGHelpWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -604, 1163, 1627))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textBrowser_2 = QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy1)
        self.textBrowser_2.setMinimumSize(QSize(0, 250))
        self.textBrowser_2.setMaximumSize(QSize(16777215, 250))
        self.textBrowser_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_2.addWidget(self.textBrowser_2)

        self.mods_path = QTextBrowser(self.scrollAreaWidgetContents)
        self.mods_path.setObjectName(u"mods_path")
        sizePolicy1.setHeightForWidth(self.mods_path.sizePolicy().hasHeightForWidth())
        self.mods_path.setSizePolicy(sizePolicy1)
        self.mods_path.setMinimumSize(QSize(0, 150))
        self.mods_path.setMaximumSize(QSize(16777215, 150))
        self.mods_path.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mods_path.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_2.addWidget(self.mods_path)

        self.mdk_path = QTextBrowser(self.scrollAreaWidgetContents)
        self.mdk_path.setObjectName(u"mdk_path")
        sizePolicy1.setHeightForWidth(self.mdk_path.sizePolicy().hasHeightForWidth())
        self.mdk_path.setSizePolicy(sizePolicy1)
        self.mdk_path.setMinimumSize(QSize(0, 120))
        self.mdk_path.setMaximumSize(QSize(16777215, 120))
        self.mdk_path.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mdk_path.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_2.addWidget(self.mdk_path)

        self.mdk_button = QPushButton(self.scrollAreaWidgetContents)
        self.mdk_button.setObjectName(u"mdk_button")

        self.verticalLayout_2.addWidget(self.mdk_button)

        self.deobf_mods = QTextBrowser(self.scrollAreaWidgetContents)
        self.deobf_mods.setObjectName(u"deobf_mods")
        sizePolicy1.setHeightForWidth(self.deobf_mods.sizePolicy().hasHeightForWidth())
        self.deobf_mods.setSizePolicy(sizePolicy1)
        self.deobf_mods.setMinimumSize(QSize(0, 130))
        self.deobf_mods.setMaximumSize(QSize(16777215, 130))
        self.deobf_mods.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.deobf_mods.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_2.addWidget(self.deobf_mods)

        self.threads = QTextBrowser(self.scrollAreaWidgetContents)
        self.threads.setObjectName(u"threads")
        sizePolicy1.setHeightForWidth(self.threads.sizePolicy().hasHeightForWidth())
        self.threads.setSizePolicy(sizePolicy1)
        self.threads.setMinimumSize(QSize(0, 80))
        self.threads.setMaximumSize(QSize(16777215, 80))
        self.threads.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.threads.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_2.addWidget(self.threads)

        self.deobf_failed = QTextBrowser(self.scrollAreaWidgetContents)
        self.deobf_failed.setObjectName(u"deobf_failed")
        sizePolicy1.setHeightForWidth(self.deobf_failed.sizePolicy().hasHeightForWidth())
        self.deobf_failed.setSizePolicy(sizePolicy1)
        self.deobf_failed.setMinimumSize(QSize(0, 215))
        self.deobf_failed.setMaximumSize(QSize(16777215, 215))
        self.deobf_failed.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.deobf_failed.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_2.addWidget(self.deobf_failed)

        self.decomp_mods = QTextBrowser(self.scrollAreaWidgetContents)
        self.decomp_mods.setObjectName(u"decomp_mods")
        sizePolicy1.setHeightForWidth(self.decomp_mods.sizePolicy().hasHeightForWidth())
        self.decomp_mods.setSizePolicy(sizePolicy1)
        self.decomp_mods.setMinimumSize(QSize(0, 110))
        self.decomp_mods.setMaximumSize(QSize(16777215, 110))
        self.decomp_mods.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.decomp_mods.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_2.addWidget(self.decomp_mods)

        self.merge = QTextBrowser(self.scrollAreaWidgetContents)
        self.merge.setObjectName(u"merge")
        sizePolicy1.setHeightForWidth(self.merge.sizePolicy().hasHeightForWidth())
        self.merge.setSizePolicy(sizePolicy1)
        self.merge.setMinimumSize(QSize(0, 100))
        self.merge.setMaximumSize(QSize(16777215, 100))
        self.merge.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.merge.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_2.addWidget(self.merge)

        self.merge_resources = QTextBrowser(self.scrollAreaWidgetContents)
        self.merge_resources.setObjectName(u"merge_resources")
        sizePolicy1.setHeightForWidth(self.merge_resources.sizePolicy().hasHeightForWidth())
        self.merge_resources.setSizePolicy(sizePolicy1)
        self.merge_resources.setMinimumSize(QSize(0, 95))
        self.merge_resources.setMaximumSize(QSize(16777215, 95))
        self.merge_resources.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.merge_resources.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_2.addWidget(self.merge_resources)

        self.patch_mdk = QTextBrowser(self.scrollAreaWidgetContents)
        self.patch_mdk.setObjectName(u"patch_mdk")
        sizePolicy1.setHeightForWidth(self.patch_mdk.sizePolicy().hasHeightForWidth())
        self.patch_mdk.setSizePolicy(sizePolicy1)
        self.patch_mdk.setMinimumSize(QSize(0, 275))
        self.patch_mdk.setMaximumSize(QSize(16777215, 275))
        self.patch_mdk.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.patch_mdk.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_2.addWidget(self.patch_mdk)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        MDGHelpWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MDGHelpWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 22))
        MDGHelpWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MDGHelpWindow)
        self.statusbar.setObjectName(u"statusbar")
        MDGHelpWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MDGHelpWindow)

        QMetaObject.connectSlotsByName(MDGHelpWindow)
    # setupUi

    def retranslateUi(self, MDGHelpWindow):
        MDGHelpWindow.setWindowTitle(QCoreApplication.translate("MDGHelpWindow", u"MDGHelpWindow", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MDGHelpWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700;\">MDG (Mods Decompiler Gui)</span><span style=\" font-size:12pt; font-weight:700;\">:</span><br />The program is designed to simplify and make deobfuscation and decompilation of mods a one-click solution for everyone interest"
                        "ed.<br />In almost all English-speaking modding communities, the topic of decompilation is prohibited. If someone tries to discuss decompilation and deobfuscation, ARR hamsters will immediately ban them. Since someone will be able to decompile their paid mods and disrupt their profits. Although the majority (95%) those who are interested in this really need to see how something works, find a bug, they are not going to decompile their paid mods in order to break the protection. So it is almost impossible for a novice modder, and even more so for a modpackmaker, to learn how to do what this program does. I want to overcome this and make sure that mods decompilation and deobfuscation can be used by any person, who needs it, even those who only came to modding. A superintuitive one-click solution. You don't know how things work? Just one click and you got your decomplied code!<br />This tool could save us hundreds of hours when developing modpacks or fixing conflicts in mods. For example, it has already saved me a"
                        "round 30 hours. Instead of binary searching in mods, which takes a couple of hours, this program allows us to find conflicts/problematic mod within 5 minutes.<br />If you don't know whether you need a specific option, use the documentation below. Every option is documented.<br />If you just want the code of your modpack to see how things work, simply don't modify the settings. The program will already do what you need with default settings.<br />Program works by this algoritm; is some option disabled, it will be skipped: </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">deobfuscate -&gt; decompile -&gt; merge to mdk</p></body></html>", None))
        self.mods_path.setHtml(QCoreApplication.translate("MDGHelpWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Mods Folder Path:</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select the folder containing the mods you wish to decompile/deobfuscate. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent"
                        ":0px;\">You can do this by: </p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Clicking the &quot;Select&quot; button. </li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Dragging and dropping the folder. </li>\n"
"<li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Manually entering the path in the designated line. </li></ul></body></html>", None))
        self.mdk_path.setHtml(QCoreApplication.translate("MDGHelpWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">MDK Archive Path:</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choose the Forge MDK archive corresponding to the Minecraft version you are using. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0;"
                        " text-indent:0px;\">You can find it on the MinecraftForge downloads page.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">After downloading the MDK, select the file without unarchiving it, using the same method as selecting the mods folder. </p></body></html>", None))
        self.mdk_button.setText(QCoreApplication.translate("MDGHelpWindow", u"Open MinecraftForge downloads page.", None))
        self.deobf_mods.setHtml(QCoreApplication.translate("MDGHelpWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Deobfuscate Mods:</span><br />Deobfuscation is needed before decompilation in Minecraft modding because the Minecraft codebase is obfuscated before release. Obfuscation is a technique used to make code harder to understand by renaming variables, methods, and classes to obscure their purpose. Deobfuscation is the process of undoing this obfuscation, mak"
                        "ing the code more readable and understandable. Decompilation, on the other hand, is the process of converting bytecode back into human-readable Java code. Without deobfuscation, decompilation would result in code that is difficult to understand and work with, making modding much more challenging. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If enabled, mods will be deobfuscated before decompilation, and the results can be found in the &quot;<span style=\" font-weight:700;\">deobfuscated_mods</span>&quot; folder. </p></body></html>", None))
        self.threads.setHtml(QCoreApplication.translate("MDGHelpWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Deobfuscation/Decompilation Threads:</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This option allows you to configure the number of threads used in deobfuscation/decompilation. Using excessively large values may cause lag on your PC. Decreasing the value wil"
                        "l slow down the process but reduce the load on your PC. Not recomended to use more threads than your system has. </p></body></html>", None))
        self.deobf_failed.setHtml(QCoreApplication.translate("MDGHelpWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">If Deobfuscation of a Mod Fails:</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In rare cases, deobfuscation of a mod may fail. Known mods with such issues include OptiFine, Towns and Towers.<br />Currently forge mdk uses Mojang mappings. Mojang mappings are d"
                        "esigned specifically for deobfuscating the vanilla Minecraft codebase released by Mojang. OptiFine, however, is a third-party mod created independently from Mojang. OptiFine's codebase may have its own obfuscation and unique naming conventions that differ from those used in vanilla Minecraft. As a result, Mojang mappings may not accurately map the obfuscated names in OptiFine's code to their original, readable names. Therefore, using Mojang mappings for deobfuscating OptiFine will result in deofuscation error. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In such cases, you can choose one of the following algorithms to resolve the issue: </p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">interrupt: The process will immediately terminat"
                        "e with a critical error message. </li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">skip mod: The problematic mod will be skipped, and it will not appear in the result folder. You will be notified of skipped mods at the end. </li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">decompile without deobfuscation: The problematic mod will be decompiled without deobfuscation. You will be notified of such mods at the end. The best option if you use this app for reading your modpack codebase. </li></ul></body></html>", None))
        self.decomp_mods.setHtml(QCoreApplication.translate("MDGHelpWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Decompile mods:</span><br />Decompilation of Minecraft mods refers to the process of converting the compiled bytecode of a Minecraft modification (mod) back into human-readable and understandable source code. This process involves reversing the compilation process, typically done to analyze, understand, and/or modify the functionality of the mod. Decom"
                        "pilation is often used in Minecraft modding communities by developers who want to gain insights into how a mod works, fix issues, add new features, or create derivative works based on existing mods. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If enabled: deobfusacted code will be decompiled. Results can be found in the &quot;<span style=\" font-weight:700;\">decompiled_mods</span>&quot; folder. </p></body></html>", None))
        self.merge.setHtml(QCoreApplication.translate("MDGHelpWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Merge result into mdk:</span><br />If we open the &quot;decompiled_mods&quot; folder as project in IntelliJ IDEA or another IDE, indexing between mods or even within a single mod won't function correctly. Therefore, when using the IDE's implementation declaration or usages buttons, you'll likely encounter issues, with only about 5% of cases working as"
                        " expected.<br />To address this, we merge all mods into the MDK, treating them as a single mod. This ensures that IDE indexing resumes correct functionality, enabling nearly all IDE buttons to work properly, with approximately 99.9% reliability. Moreover, this setup allows you to read the source code of Minecraft or Minecraft Forge, as the MDK provides this functionality. </p></body></html>", None))
        self.merge_resources.setHtml(QCoreApplication.translate("MDGHelpWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Merge code/resources:</span><br />This option allows you to configure what will be merged: </p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Code: Decompiled "
                        "code of mods. </li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Resources: Data, assets, etc. It's not recommended to disable this option since if you want to figure out what mode added some messages, they (translations) will be found here. </li></ul></body></html>", None))
        self.patch_mdk.setHtml(QCoreApplication.translate("MDGHelpWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Patch mdk with &quot;downloadSources = true&quot;:</span><br />This will prompt the IDE to download Minecraft and MinecraftForge source code. As a result, you will be able to navigate through them seamlessly.<span style=\" font-size:12pt; font-weight:700;\"><br /></span>Patches build.gradle with:<br /><span style=\" font-size:8pt; font-style:italic;\">"
                        "apply plugin: 'idea'</span> </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">idea {</span> </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\"> module {</span> </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\"> downloadSources = true</span> </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\"> }</span> </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">}</span> </p>\n"
"<p"
                        " style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">apply plugin: 'eclipse'</span> </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">eclipse {</span> </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\"> classpath {</span> </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\"> downloadSources = true</span> </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-ri"
                        "ght:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\"> }</span> </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">}</span></p></body></html>", None))
    # retranslateUi

