# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MDGMainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MDGMainWindow(object):
    def setupUi(self, MDGMainWindow):
        if not MDGMainWindow.objectName():
            MDGMainWindow.setObjectName(u"MDGMainWindow")
        MDGMainWindow.resize(671, 493)
        MDGMainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MDGMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAutoFillBackground(False)
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mods_path_vertical_group_box = QGroupBox(self.centralwidget)
        self.mods_path_vertical_group_box.setObjectName(u"mods_path_vertical_group_box")
        self.mods_path_vertical_group_box.setEnabled(True)
        self.mods_path_vertical_group_box.setMinimumSize(QSize(0, 50))
        self.mods_path_vertical_group_box.setAcceptDrops(True)
        self.mods_path_vertical_group_box.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.mods_path_vertical_group_box.setFlat(False)
        self.verticalLayout_2 = QVBoxLayout(self.mods_path_vertical_group_box)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mods_path_horizontal_layout = QHBoxLayout()
        self.mods_path_horizontal_layout.setObjectName(u"mods_path_horizontal_layout")
        self.mods_path_label = QLabel(self.mods_path_vertical_group_box)
        self.mods_path_label.setObjectName(u"mods_path_label")

        self.mods_path_horizontal_layout.addWidget(self.mods_path_label)

        self.mods_path_line_edit = QLineEdit(self.mods_path_vertical_group_box)
        self.mods_path_line_edit.setObjectName(u"mods_path_line_edit")
        self.mods_path_line_edit.setClearButtonEnabled(True)

        self.mods_path_horizontal_layout.addWidget(self.mods_path_line_edit)

        self.select_mods_button = QPushButton(self.mods_path_vertical_group_box)
        self.select_mods_button.setObjectName(u"select_mods_button")

        self.mods_path_horizontal_layout.addWidget(self.select_mods_button)

        self.help_mods_button = QPushButton(self.mods_path_vertical_group_box)
        self.help_mods_button.setObjectName(u"help_mods_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.help_mods_button.sizePolicy().hasHeightForWidth())
        self.help_mods_button.setSizePolicy(sizePolicy)
        self.help_mods_button.setMaximumSize(QSize(20, 16777215))

        self.mods_path_horizontal_layout.addWidget(self.help_mods_button)


        self.verticalLayout_2.addLayout(self.mods_path_horizontal_layout)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.label_5 = QLabel(self.mods_path_vertical_group_box)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_8.addWidget(self.label_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.verticalLayout.addWidget(self.mods_path_vertical_group_box)

        self.mdk_path_vertical_group_box = QGroupBox(self.centralwidget)
        self.mdk_path_vertical_group_box.setObjectName(u"mdk_path_vertical_group_box")
        self.mdk_path_vertical_group_box.setMinimumSize(QSize(0, 50))
        self.mdk_path_vertical_group_box.setAcceptDrops(True)
        self.verticalLayout_4 = QVBoxLayout(self.mdk_path_vertical_group_box)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.mdk_path_horizontal_layout = QHBoxLayout()
        self.mdk_path_horizontal_layout.setObjectName(u"mdk_path_horizontal_layout")
        self.mdk_path_label = QLabel(self.mdk_path_vertical_group_box)
        self.mdk_path_label.setObjectName(u"mdk_path_label")

        self.mdk_path_horizontal_layout.addWidget(self.mdk_path_label)

        self.mdk_path_line_edit = QLineEdit(self.mdk_path_vertical_group_box)
        self.mdk_path_line_edit.setObjectName(u"mdk_path_line_edit")
        self.mdk_path_line_edit.setClearButtonEnabled(True)

        self.mdk_path_horizontal_layout.addWidget(self.mdk_path_line_edit)

        self.select_mdk_button = QPushButton(self.mdk_path_vertical_group_box)
        self.select_mdk_button.setObjectName(u"select_mdk_button")

        self.mdk_path_horizontal_layout.addWidget(self.select_mdk_button)

        self.help_mdk_button = QPushButton(self.mdk_path_vertical_group_box)
        self.help_mdk_button.setObjectName(u"help_mdk_button")
        sizePolicy.setHeightForWidth(self.help_mdk_button.sizePolicy().hasHeightForWidth())
        self.help_mdk_button.setSizePolicy(sizePolicy)
        self.help_mdk_button.setMaximumSize(QSize(20, 16777215))

        self.mdk_path_horizontal_layout.addWidget(self.help_mdk_button)


        self.verticalLayout_4.addLayout(self.mdk_path_horizontal_layout)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_3)

        self.label_8 = QLabel(self.mdk_path_vertical_group_box)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_11.addWidget(self.label_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)


        self.verticalLayout.addWidget(self.mdk_path_vertical_group_box)

        self.deobf_group_box = QGroupBox(self.centralwidget)
        self.deobf_group_box.setObjectName(u"deobf_group_box")
        self.horizontalLayout_4 = QHBoxLayout(self.deobf_group_box)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.deobf_check_box = QCheckBox(self.deobf_group_box)
        self.deobf_check_box.setObjectName(u"deobf_check_box")
        self.deobf_check_box.setChecked(True)

        self.horizontalLayout_4.addWidget(self.deobf_check_box)

        self.help_deobf_button = QPushButton(self.deobf_group_box)
        self.help_deobf_button.setObjectName(u"help_deobf_button")
        sizePolicy.setHeightForWidth(self.help_deobf_button.sizePolicy().hasHeightForWidth())
        self.help_deobf_button.setSizePolicy(sizePolicy)
        self.help_deobf_button.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_4.addWidget(self.help_deobf_button)


        self.verticalLayout.addWidget(self.deobf_group_box)

        self.deobf_threads_group_box = QGroupBox(self.centralwidget)
        self.deobf_threads_group_box.setObjectName(u"deobf_threads_group_box")
        self.horizontalLayout_12 = QHBoxLayout(self.deobf_threads_group_box)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.deobf_threads_label = QLabel(self.deobf_threads_group_box)
        self.deobf_threads_label.setObjectName(u"deobf_threads_label")

        self.horizontalLayout_12.addWidget(self.deobf_threads_label)

        self.deobf_threads_spin_box = QSpinBox(self.deobf_threads_group_box)
        self.deobf_threads_spin_box.setObjectName(u"deobf_threads_spin_box")
        self.deobf_threads_spin_box.setMinimum(1)
        self.deobf_threads_spin_box.setMaximum(32)

        self.horizontalLayout_12.addWidget(self.deobf_threads_spin_box)

        self.deobf_threads_horizontal_slider = QSlider(self.deobf_threads_group_box)
        self.deobf_threads_horizontal_slider.setObjectName(u"deobf_threads_horizontal_slider")
        self.deobf_threads_horizontal_slider.setMinimumSize(QSize(360, 0))
        self.deobf_threads_horizontal_slider.setMinimum(1)
        self.deobf_threads_horizontal_slider.setMaximum(32)
        self.deobf_threads_horizontal_slider.setPageStep(1)
        self.deobf_threads_horizontal_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_12.addWidget(self.deobf_threads_horizontal_slider)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)

        self.help_deobf_threads_button = QPushButton(self.deobf_threads_group_box)
        self.help_deobf_threads_button.setObjectName(u"help_deobf_threads_button")
        sizePolicy.setHeightForWidth(self.help_deobf_threads_button.sizePolicy().hasHeightForWidth())
        self.help_deobf_threads_button.setSizePolicy(sizePolicy)
        self.help_deobf_threads_button.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_12.addWidget(self.help_deobf_threads_button)


        self.verticalLayout.addWidget(self.deobf_threads_group_box)

        self.deobf_failed_group_box = QGroupBox(self.centralwidget)
        self.deobf_failed_group_box.setObjectName(u"deobf_failed_group_box")
        self.horizontalLayout_3 = QHBoxLayout(self.deobf_failed_group_box)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.deobf_failed_label = QLabel(self.deobf_failed_group_box)
        self.deobf_failed_label.setObjectName(u"deobf_failed_label")

        self.horizontalLayout_3.addWidget(self.deobf_failed_label)

        self.deobf_failed_radio_interrupt = QRadioButton(self.deobf_failed_group_box)
        self.deobf_failed_radio_interrupt.setObjectName(u"deobf_failed_radio_interrupt")

        self.horizontalLayout_3.addWidget(self.deobf_failed_radio_interrupt)

        self.deobf_failed_radio_skip = QRadioButton(self.deobf_failed_group_box)
        self.deobf_failed_radio_skip.setObjectName(u"deobf_failed_radio_skip")

        self.horizontalLayout_3.addWidget(self.deobf_failed_radio_skip)

        self.deobf_failed_radio_decompile = QRadioButton(self.deobf_failed_group_box)
        self.deobf_failed_radio_decompile.setObjectName(u"deobf_failed_radio_decompile")
        self.deobf_failed_radio_decompile.setChecked(True)

        self.horizontalLayout_3.addWidget(self.deobf_failed_radio_decompile)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.help_deobf_failed_button = QPushButton(self.deobf_failed_group_box)
        self.help_deobf_failed_button.setObjectName(u"help_deobf_failed_button")
        sizePolicy.setHeightForWidth(self.help_deobf_failed_button.sizePolicy().hasHeightForWidth())
        self.help_deobf_failed_button.setSizePolicy(sizePolicy)
        self.help_deobf_failed_button.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_3.addWidget(self.help_deobf_failed_button)


        self.verticalLayout.addWidget(self.deobf_failed_group_box)

        self.decomp_group_box = QGroupBox(self.centralwidget)
        self.decomp_group_box.setObjectName(u"decomp_group_box")
        self.horizontalLayout_6 = QHBoxLayout(self.decomp_group_box)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.decomp_check_box = QCheckBox(self.decomp_group_box)
        self.decomp_check_box.setObjectName(u"decomp_check_box")
        self.decomp_check_box.setChecked(True)

        self.horizontalLayout_6.addWidget(self.decomp_check_box)

        self.help_decomp_button = QPushButton(self.decomp_group_box)
        self.help_decomp_button.setObjectName(u"help_decomp_button")
        sizePolicy.setHeightForWidth(self.help_decomp_button.sizePolicy().hasHeightForWidth())
        self.help_decomp_button.setSizePolicy(sizePolicy)
        self.help_decomp_button.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_6.addWidget(self.help_decomp_button)


        self.verticalLayout.addWidget(self.decomp_group_box)

        self.decomp_threads_group_box = QGroupBox(self.centralwidget)
        self.decomp_threads_group_box.setObjectName(u"decomp_threads_group_box")
        self.horizontalLayout_13 = QHBoxLayout(self.decomp_threads_group_box)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.decomp_threads_label = QLabel(self.decomp_threads_group_box)
        self.decomp_threads_label.setObjectName(u"decomp_threads_label")

        self.horizontalLayout_13.addWidget(self.decomp_threads_label)

        self.decomp_threads_spin_box = QSpinBox(self.decomp_threads_group_box)
        self.decomp_threads_spin_box.setObjectName(u"decomp_threads_spin_box")
        self.decomp_threads_spin_box.setMinimum(1)
        self.decomp_threads_spin_box.setMaximum(32)

        self.horizontalLayout_13.addWidget(self.decomp_threads_spin_box)

        self.decomp_threads_horizontal_slider = QSlider(self.decomp_threads_group_box)
        self.decomp_threads_horizontal_slider.setObjectName(u"decomp_threads_horizontal_slider")
        self.decomp_threads_horizontal_slider.setMinimumSize(QSize(360, 0))
        self.decomp_threads_horizontal_slider.setMinimum(1)
        self.decomp_threads_horizontal_slider.setMaximum(32)
        self.decomp_threads_horizontal_slider.setPageStep(1)
        self.decomp_threads_horizontal_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_13.addWidget(self.decomp_threads_horizontal_slider)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)

        self.help_decomp_threads_button = QPushButton(self.decomp_threads_group_box)
        self.help_decomp_threads_button.setObjectName(u"help_decomp_threads_button")
        sizePolicy.setHeightForWidth(self.help_decomp_threads_button.sizePolicy().hasHeightForWidth())
        self.help_decomp_threads_button.setSizePolicy(sizePolicy)
        self.help_decomp_threads_button.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_13.addWidget(self.help_decomp_threads_button)


        self.verticalLayout.addWidget(self.decomp_threads_group_box)

        self.decomp_cmd_layout = QHBoxLayout()
        self.decomp_cmd_layout.setObjectName(u"decomp_cmd_layout")
        self.decomp_cmd_label = QLabel(self.centralwidget)
        self.decomp_cmd_label.setObjectName(u"decomp_cmd_label")

        self.decomp_cmd_layout.addWidget(self.decomp_cmd_label)

        self.decomp_cmd_line_edit = QLineEdit(self.centralwidget)
        self.decomp_cmd_line_edit.setObjectName(u"decomp_cmd_line_edit")
        self.decomp_cmd_line_edit.setClearButtonEnabled(False)

        self.decomp_cmd_layout.addWidget(self.decomp_cmd_line_edit)

        self.decomp_cmd_reset_button = QPushButton(self.centralwidget)
        self.decomp_cmd_reset_button.setObjectName(u"decomp_cmd_reset_button")
        sizePolicy.setHeightForWidth(self.decomp_cmd_reset_button.sizePolicy().hasHeightForWidth())
        self.decomp_cmd_reset_button.setSizePolicy(sizePolicy)
        self.decomp_cmd_reset_button.setMaximumSize(QSize(40, 16777215))

        self.decomp_cmd_layout.addWidget(self.decomp_cmd_reset_button)


        self.verticalLayout.addLayout(self.decomp_cmd_layout)

        self.merge_horizontal_layout = QHBoxLayout()
        self.merge_horizontal_layout.setObjectName(u"merge_horizontal_layout")
        self.merge_check_box = QCheckBox(self.centralwidget)
        self.merge_check_box.setObjectName(u"merge_check_box")
        self.merge_check_box.setChecked(True)

        self.merge_horizontal_layout.addWidget(self.merge_check_box)

        self.help_merge_button = QPushButton(self.centralwidget)
        self.help_merge_button.setObjectName(u"help_merge_button")
        sizePolicy.setHeightForWidth(self.help_merge_button.sizePolicy().hasHeightForWidth())
        self.help_merge_button.setSizePolicy(sizePolicy)
        self.help_merge_button.setMaximumSize(QSize(20, 16777215))

        self.merge_horizontal_layout.addWidget(self.help_merge_button)


        self.verticalLayout.addLayout(self.merge_horizontal_layout)

        self.merge_group_box = QGroupBox(self.centralwidget)
        self.merge_group_box.setObjectName(u"merge_group_box")
        self.horizontalLayout_5 = QHBoxLayout(self.merge_group_box)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.merge_label = QLabel(self.merge_group_box)
        self.merge_label.setObjectName(u"merge_label")

        self.horizontalLayout_5.addWidget(self.merge_label)

        self.merge_code_check_box = QCheckBox(self.merge_group_box)
        self.merge_code_check_box.setObjectName(u"merge_code_check_box")
        self.merge_code_check_box.setChecked(True)

        self.horizontalLayout_5.addWidget(self.merge_code_check_box)

        self.merge_resources_check_box = QCheckBox(self.merge_group_box)
        self.merge_resources_check_box.setObjectName(u"merge_resources_check_box")
        self.merge_resources_check_box.setChecked(True)

        self.horizontalLayout_5.addWidget(self.merge_resources_check_box)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.help_merge_button_2 = QPushButton(self.merge_group_box)
        self.help_merge_button_2.setObjectName(u"help_merge_button_2")
        sizePolicy.setHeightForWidth(self.help_merge_button_2.sizePolicy().hasHeightForWidth())
        self.help_merge_button_2.setSizePolicy(sizePolicy)
        self.help_merge_button_2.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_5.addWidget(self.help_merge_button_2)


        self.verticalLayout.addWidget(self.merge_group_box)

        self.patch_mdk_group_box = QGroupBox(self.centralwidget)
        self.patch_mdk_group_box.setObjectName(u"patch_mdk_group_box")
        self.horizontalLayout_7 = QHBoxLayout(self.patch_mdk_group_box)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.download_sources_check_box = QCheckBox(self.patch_mdk_group_box)
        self.download_sources_check_box.setObjectName(u"download_sources_check_box")
        self.download_sources_check_box.setChecked(True)

        self.horizontalLayout_7.addWidget(self.download_sources_check_box)

        self.help_sources_button = QPushButton(self.patch_mdk_group_box)
        self.help_sources_button.setObjectName(u"help_sources_button")
        sizePolicy.setHeightForWidth(self.help_sources_button.sizePolicy().hasHeightForWidth())
        self.help_sources_button.setSizePolicy(sizePolicy)
        self.help_sources_button.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_7.addWidget(self.help_sources_button)


        self.verticalLayout.addWidget(self.patch_mdk_group_box)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setAcceptDrops(False)

        self.verticalLayout_3.addWidget(self.start_button)

        MDGMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MDGMainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 671, 22))
        MDGMainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MDGMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MDGMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MDGMainWindow)

        QMetaObject.connectSlotsByName(MDGMainWindow)
    # setupUi

    def retranslateUi(self, MDGMainWindow):
        MDGMainWindow.setWindowTitle(QCoreApplication.translate("MDGMainWindow", u"MDG (Mods Decompiler Gui)", None))
        self.mods_path_label.setText(QCoreApplication.translate("MDGMainWindow", u"Mods folder path:", None))
        self.select_mods_button.setText(QCoreApplication.translate("MDGMainWindow", u"select", None))
        self.help_mods_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.label_5.setText(QCoreApplication.translate("MDGMainWindow", u"accepts drag&drop", None))
        self.mdk_path_label.setText(QCoreApplication.translate("MDGMainWindow", u"MDK archive path:", None))
        self.select_mdk_button.setText(QCoreApplication.translate("MDGMainWindow", u"select", None))
        self.help_mdk_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.label_8.setText(QCoreApplication.translate("MDGMainWindow", u"accepts drag&drop", None))
        self.deobf_check_box.setText(QCoreApplication.translate("MDGMainWindow", u"Deobfuscate mods", None))
        self.help_deobf_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.deobf_threads_label.setText(QCoreApplication.translate("MDGMainWindow", u"Deobfuscation threads:", None))
        self.help_deobf_threads_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.deobf_failed_label.setText(QCoreApplication.translate("MDGMainWindow", u"If deobfuscation of mod failed:", None))
        self.deobf_failed_radio_interrupt.setText(QCoreApplication.translate("MDGMainWindow", u"interrupt", None))
        self.deobf_failed_radio_skip.setText(QCoreApplication.translate("MDGMainWindow", u"skip mod", None))
        self.deobf_failed_radio_decompile.setText(QCoreApplication.translate("MDGMainWindow", u"decompile without deobfuscation", None))
        self.help_deobf_failed_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.decomp_check_box.setText(QCoreApplication.translate("MDGMainWindow", u"Decompile mods", None))
        self.help_decomp_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.decomp_threads_label.setText(QCoreApplication.translate("MDGMainWindow", u"Decompilation threads:", None))
        self.help_decomp_threads_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.decomp_cmd_label.setText(QCoreApplication.translate("MDGMainWindow", u"Decompilation cmd:", None))
        self.decomp_cmd_line_edit.setText(QCoreApplication.translate("MDGMainWindow", u"java -jar vineflower-1.9.3.jar -dgs=1 {path_to_jar} .\\{out_path}", None))
        self.decomp_cmd_reset_button.setText(QCoreApplication.translate("MDGMainWindow", u"reset", None))
        self.merge_check_box.setText(QCoreApplication.translate("MDGMainWindow", u"Merge result into mdk", None))
        self.help_merge_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.merge_label.setText(QCoreApplication.translate("MDGMainWindow", u"Merge:", None))
        self.merge_code_check_box.setText(QCoreApplication.translate("MDGMainWindow", u"code", None))
        self.merge_resources_check_box.setText(QCoreApplication.translate("MDGMainWindow", u"resources", None))
        self.help_merge_button_2.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.download_sources_check_box.setText(QCoreApplication.translate("MDGMainWindow", u"Patch mdk with \"downloadSources = true\"", None))
        self.help_sources_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.start_button.setText(QCoreApplication.translate("MDGMainWindow", u"start", None))
    # retranslateUi

