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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QHBoxLayout, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QTextBrowser, QVBoxLayout, QWidget)
from . import resources_rc

class Ui_MDGHelpWindow(object):
    def setupUi(self, MDGHelpWindow):
        if not MDGHelpWindow.objectName():
            MDGHelpWindow.setObjectName(u"MDGHelpWindow")
        MDGHelpWindow.resize(1200, 1151)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MDGHelpWindow.sizePolicy().hasHeightForWidth())
        MDGHelpWindow.setSizePolicy(sizePolicy)
        MDGHelpWindow.setMinimumSize(QSize(1200, 0))
        MDGHelpWindow.setMaximumSize(QSize(1200, 16777215))
        icon = QIcon()
        icon.addFile(u":/images/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MDGHelpWindow.setWindowIcon(icon)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1163, 2520))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textBrowser_2 = QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy1)
        self.textBrowser_2.setMinimumSize(QSize(0, 230))
        self.textBrowser_2.setMaximumSize(QSize(16777215, 230))
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
        self.mdk_path.setMinimumSize(QSize(0, 130))
        self.mdk_path.setMaximumSize(QSize(16777215, 130))
        self.mdk_path.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mdk_path.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_2.addWidget(self.mdk_path)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mdk_help_download_button = QPushButton(self.scrollAreaWidgetContents)
        self.mdk_help_download_button.setObjectName(u"mdk_help_download_button")

        self.horizontalLayout.addWidget(self.mdk_help_download_button)

        self.mdk_button = QPushButton(self.scrollAreaWidgetContents)
        self.mdk_button.setObjectName(u"mdk_button")

        self.horizontalLayout.addWidget(self.mdk_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.deobf_mods = QTextBrowser(self.scrollAreaWidgetContents)
        self.deobf_mods.setObjectName(u"deobf_mods")
        sizePolicy1.setHeightForWidth(self.deobf_mods.sizePolicy().hasHeightForWidth())
        self.deobf_mods.setSizePolicy(sizePolicy1)
        self.deobf_mods.setMinimumSize(QSize(0, 130))
        self.deobf_mods.setMaximumSize(QSize(16777215, 130))
        self.deobf_mods.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.deobf_mods.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_2.addWidget(self.deobf_mods)

        self.deobf_algo = QTextBrowser(self.scrollAreaWidgetContents)
        self.deobf_algo.setObjectName(u"deobf_algo")
        sizePolicy1.setHeightForWidth(self.deobf_algo.sizePolicy().hasHeightForWidth())
        self.deobf_algo.setSizePolicy(sizePolicy1)
        self.deobf_algo.setMinimumSize(QSize(0, 230))
        self.deobf_algo.setMaximumSize(QSize(16777215, 230))
        self.deobf_algo.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.deobf_algo.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_2.addWidget(self.deobf_algo)

        self.threads = QTextBrowser(self.scrollAreaWidgetContents)
        self.threads.setObjectName(u"threads")
        sizePolicy1.setHeightForWidth(self.threads.sizePolicy().hasHeightForWidth())
        self.threads.setSizePolicy(sizePolicy1)
        self.threads.setMinimumSize(QSize(0, 110))
        self.threads.setMaximumSize(QSize(16777215, 110))
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

        self.decomp_logging = QTextBrowser(self.scrollAreaWidgetContents)
        self.decomp_logging.setObjectName(u"decomp_logging")
        sizePolicy1.setHeightForWidth(self.decomp_logging.sizePolicy().hasHeightForWidth())
        self.decomp_logging.setSizePolicy(sizePolicy1)
        self.decomp_logging.setMinimumSize(QSize(0, 60))
        self.decomp_logging.setMaximumSize(QSize(16777215, 60))
        self.decomp_logging.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.decomp_logging.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_2.addWidget(self.decomp_logging)

        self.decomp_cmd = QTextBrowser(self.scrollAreaWidgetContents)
        self.decomp_cmd.setObjectName(u"decomp_cmd")
        sizePolicy1.setHeightForWidth(self.decomp_cmd.sizePolicy().hasHeightForWidth())
        self.decomp_cmd.setSizePolicy(sizePolicy1)
        self.decomp_cmd.setMinimumSize(QSize(0, 165))
        self.decomp_cmd.setMaximumSize(QSize(16777215, 165))
        self.decomp_cmd.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.decomp_cmd.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_2.addWidget(self.decomp_cmd)

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

        self.java_home = QTextBrowser(self.scrollAreaWidgetContents)
        self.java_home.setObjectName(u"java_home")
        sizePolicy1.setHeightForWidth(self.java_home.sizePolicy().hasHeightForWidth())
        self.java_home.setSizePolicy(sizePolicy1)
        self.java_home.setMinimumSize(QSize(0, 120))
        self.java_home.setMaximumSize(QSize(16777215, 120))
        self.java_home.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.java_home.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_2.addWidget(self.java_home)

        self.jar_in_jar = QTextBrowser(self.scrollAreaWidgetContents)
        self.jar_in_jar.setObjectName(u"jar_in_jar")
        sizePolicy1.setHeightForWidth(self.jar_in_jar.sizePolicy().hasHeightForWidth())
        self.jar_in_jar.setSizePolicy(sizePolicy1)
        self.jar_in_jar.setMinimumSize(QSize(0, 130))
        self.jar_in_jar.setMaximumSize(QSize(16777215, 130))
        self.jar_in_jar.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.jar_in_jar.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_2.addWidget(self.jar_in_jar)

        self.cache = QTextBrowser(self.scrollAreaWidgetContents)
        self.cache.setObjectName(u"cache")
        sizePolicy1.setHeightForWidth(self.cache.sizePolicy().hasHeightForWidth())
        self.cache.setSizePolicy(sizePolicy1)
        self.cache.setMinimumSize(QSize(0, 130))
        self.cache.setMaximumSize(QSize(16777215, 130))
        self.cache.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.cache.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_2.addWidget(self.cache)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.close_button = QPushButton(self.centralwidget)
        self.close_button.setObjectName(u"close_button")

        self.verticalLayout.addWidget(self.close_button)

        MDGHelpWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MDGHelpWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 22))
        MDGHelpWindow.setMenuBar(self.menubar)

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
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> <span style=\" font-size:16pt; font-weight:700;\">MDG (Mods Decompiler Gui)</span><span style=\" font-size:12pt; font-weight:700;\">:</span><br />The program is designed to simplify and make deobfuscation and decompilation of mods a one-click solution for everyone interested.<br />In almost all English-speaking modding communities, the topic of decompilation is prohibited. If someone tries to discuss"
                        " decompilation and deobfuscation, ARR hamsters will immediately ban them. Since someone will be able to decompile their paid mods and disrupt their profits. Although the majority (95%) those who are interested in this really need to see how something works, find a bug, they are not going to decompile their paid mods in order to break the protection. So it is almost impossible for a novice modder, and even more so for a modpackmaker, to learn how to do what this program does. I want to overcome this and make sure that mods decompilation and deobfuscation can be used by any person, who needs it, even those who only came to modding. A superintuitive one-click solution. You don't know how things work? Just one click and you got your decomplied code!<br />This tool could save us hundreds of hours when developing modpacks or fixing conflicts in mods. For example, it has already saved me around 30 hours. Instead of binary searching in mods, which takes a couple of hours, this program allows us to find conflicts/probl"
                        "ematic mod within 5 minutes.<br />If you don't know whether you need a specific option, use the documentation below. Every option is documented.<br />If you just want the code of your modpack to see how things work, simply don't modify the settings. The program will already do what you need with default settings.<br />Program works by this algorithm; is some option disabled, it will be skipped: </p>\n"
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
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choose the Forge MDK archive corresponding to the Minecraft version you are using. Always use the latest MDK because mappings remain same for corresponding version of Minecraft, although some deo"
                        "bfuscation issues may be fixed between different versions of the MDK.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You can find it on the MinecraftForge downloads page.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">After downloading the MDK, select the file without unarchiving it, using the same method as selecting the mods folder. </p></body></html>", None))
        self.mdk_help_download_button.setText(QCoreApplication.translate("MDGHelpWindow", u"how to download mdk?", None))
        self.mdk_button.setText(QCoreApplication.translate("MDGHelpWindow", u"open MinecraftForge downloads page", None))
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
        self.deobf_algo.setHtml(QCoreApplication.translate("MDGHelpWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Deobfuscation algorithm:</span><br />MDK: 1.12.2+<br />BON2: 1.7.10 - 1.15.2</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You can select one of the deobfuscation algorithms:</p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px"
                        "; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Safe (using MDK): Mods will be deobfuscated with the <span style=\" font-family:'Courier New';\">fg.deobf()</span> function from MDK. The MDK Gradle will be patched with a patch that will apply <span style=\" font-family:'Courier New';\">fg.deobf()</span> to every mod in the libs folder. The mod we are going to deobfuscate will be copied to the libs folder, and the <span style=\" font-family:'Courier New';\">compileJava</span> function will be run. After it finishes, the deobfuscated mod will be copied from the Gradle cache to the deobfuscated mods folder. Each mod will be deobfuscated with a separate MDK.</li>\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fast (using MDK): Same as safe, but all mods will be deobfuscated with one MDK. This can save significant time, but if MDK fa"
                        "ils to deobfuscate a single mod, the whole process will fail without the ability to determine which mod caused this. Use this if you are 100% sure that your modpack does not contain such mods.</li>\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">BON2: Mods will be deobfuscated with a program called BON2. Use this for legacy versions. Select the version and mappings. Do not touch the BON2 command if you are not sure what you are doing.</li></ul></body></html>", None))
        self.threads.setHtml(QCoreApplication.translate("MDGHelpWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Deobfuscation/Decompilation Threads:</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This option allows you to configure the number of threads used in deobfuscation/decompilation. Using excessively large values may cause lag on your PC. Decreasing the value wil"
                        "l slow down the process but reduce the load on your PC. Not recomended to use more threads than your system has.<br />Deobfuscation threads is RAM intensive option. Each thread can eat up to 500 MB of RAM.<br />Decompilation is CPU intensive option. </p></body></html>", None))
        self.deobf_failed.setHtml(QCoreApplication.translate("MDGHelpWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">If Deobfuscation of a Mod Fails:</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In rare cases, deobfuscation of a mod may fail. Known mods with such issues include OptiFine, Towns and Towers. Modern versions of forge gradle can deobfuscate both.<br />Currently"
                        " forge mdk uses Mojang mappings. Mojang mappings are designed specifically for deobfuscating the vanilla Minecraft codebase released by Mojang. OptiFine, however, is a third-party mod created independently from Mojang. OptiFine's codebase may have its own obfuscation and unique naming conventions that differ from those used in vanilla Minecraft. As a result, Mojang mappings may not accurately map the obfuscated names in OptiFine's code to their original, readable names. Therefore, using Mojang mappings for deobfuscating OptiFine will result in deofuscation error. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In such cases, you can choose one of the following algorithms to resolve the issue: </p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0"
                        "px;\">interrupt: The process will immediately terminate with a critical error message. </li>\n"
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
        self.decomp_logging.setHtml(QCoreApplication.translate("MDGHelpWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Show erros/warnings:</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This option allows you to configure the display of warnings/errors from the decompiler in the ProgressWindow logging widget.</p></body></html>", None))
        self.decomp_cmd.setHtml(QCoreApplication.translate("MDGHelpWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Decompilation cmd:</span><br />With this, you can configure console command with which program decompiles mod.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Add additional flags, change the decompiler, etc...<br />String must contain:<br />{path_to_jar} - will be replace"
                        "d with path to jar that we are going to decompile.<br />{out_path} - will be replaced with path to folder with decompiler output.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Touch only if you are sure of what you are doing.<br />If you have in JAVA_HOME java 16 or bellow, You need to replace &quot;java&quot; with path to java 17 or upper. like:<br />&quot;C:\\Program Files\\Eclipse Adoptium\\jdk-17.0.10.7-hotspot\\bin\\java.exe&quot; -jar decompiler\\fernflower.jar -dgs=1 -din=1 {path_to_jar} {out_path}</p></body></html>", None))
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
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Resources: Data, assets, etc. It's not recommended to disable this option since if you want to figure out what mod added some messages, they (translations) will be found here. </li></ul></body></html>", None))
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
        self.java_home.setHtml(QCoreApplication.translate("MDGHelpWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Specify JAVA_HOME:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You can select JAVA_HOME for every tool that MDG uses. For example, if your JAVA_HOME is a legacy version:</p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right:"
                        " 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">BON2: select Java 17+</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">MDK: select the version of Java that is suitable for your MDK.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Decompiler: select Java 17+</li></ul></body></html>", None))
        self.jar_in_jar.setHtml(QCoreApplication.translate("MDGHelpWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Include jar in jar:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Many Minecraft mods include their dependencies not in a separate library mod, but within their own jar file. This is called 'jar-in-jar'. The most popular example is Create and FlyWheel. In modern v"
                        "ersions of Create, FlyWheel is included within Create.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If enabled, MDG will analyze every mod for 'jar-in-jar'. If found, jar inside mod jar, it will be extracted from the mod and processed along with other mods. This process will also be applied recursively to all jar in jars.<br /><br /><span style=\" font-weight:700;\">This algorithm is implemented very efficiently. It has almost no effect on time.</span></p></body></html>", None))
        self.cache.setHtml(QCoreApplication.translate("MDGHelpWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">Use cache:</span><br />By default, MDG voids the tmp and result folders upon pressing the start button. So, if you regularly use this tool on the same modpack while changing/updating 2-3 mods, you still need to wait a considerable amount of time for each use of the tool.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-r"
                        "ight:0px; -qt-block-indent:0; text-indent:0px;\">If enabled, MDG will analyze deobfuscated mods and decompiled mods folders after pressing the start button. If a mod from selected mods folder is already processed, it won't be removed from the result and deobfuscation and/or decompilation stages of this mod will be skipped.<br />Therefore, you can save significant time in this usage case.</p></body></html>", None))
        self.close_button.setText(QCoreApplication.translate("MDGHelpWindow", u"close", None))
    # retranslateUi

