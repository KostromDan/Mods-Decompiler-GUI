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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_MDGMainWindow(object):
    def setupUi(self, MDGMainWindow):
        if not MDGMainWindow.objectName():
            MDGMainWindow.setObjectName(u"MDGMainWindow")
        MDGMainWindow.resize(1066, 888)
        MDGMainWindow.setMaximumSize(QSize(16777215, 16777215))
        MDGMainWindow.setLayoutDirection(Qt.LeftToRight)
        self.action_reset = QAction(MDGMainWindow)
        self.action_reset.setObjectName(u"action_reset")
        self.action_save = QAction(MDGMainWindow)
        self.action_save.setObjectName(u"action_save")
        self.centralwidget = QWidget(MDGMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAutoFillBackground(False)
        self.verticalLayout_8 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.mods_path_vertical_group_box = QGroupBox(self.centralwidget)
        self.mods_path_vertical_group_box.setObjectName(u"mods_path_vertical_group_box")
        self.mods_path_vertical_group_box.setEnabled(True)
        self.mods_path_vertical_group_box.setMinimumSize(QSize(0, 58))
        self.mods_path_vertical_group_box.setAcceptDrops(True)
        self.mods_path_vertical_group_box.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.mods_path_vertical_group_box.setFlat(False)
        self.verticalLayout_2 = QVBoxLayout(self.mods_path_vertical_group_box)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 0, 9, 2)
        self.mods_path_horizontal_layout = QHBoxLayout()
        self.mods_path_horizontal_layout.setObjectName(u"mods_path_horizontal_layout")
        self.mods_path_label = QLabel(self.mods_path_vertical_group_box)
        self.mods_path_label.setObjectName(u"mods_path_label")
        self.mods_path_label.setMinimumSize(QSize(0, 24))

        self.mods_path_horizontal_layout.addWidget(self.mods_path_label)

        self.mods_path_line_edit = QLineEdit(self.mods_path_vertical_group_box)
        self.mods_path_line_edit.setObjectName(u"mods_path_line_edit")
        self.mods_path_line_edit.setMinimumSize(QSize(0, 24))
        self.mods_path_line_edit.setClearButtonEnabled(True)

        self.mods_path_horizontal_layout.addWidget(self.mods_path_line_edit)

        self.select_mods_button = QPushButton(self.mods_path_vertical_group_box)
        self.select_mods_button.setObjectName(u"select_mods_button")
        self.select_mods_button.setMinimumSize(QSize(0, 24))
        self.select_mods_button.setMaximumSize(QSize(44, 16777215))

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


        self.verticalLayout_8.addWidget(self.mods_path_vertical_group_box)

        self.mdk_path_vertical_group_box = QGroupBox(self.centralwidget)
        self.mdk_path_vertical_group_box.setObjectName(u"mdk_path_vertical_group_box")
        self.mdk_path_vertical_group_box.setMinimumSize(QSize(0, 58))
        self.mdk_path_vertical_group_box.setAcceptDrops(True)
        self.verticalLayout_4 = QVBoxLayout(self.mdk_path_vertical_group_box)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 0, 9, 2)
        self.mdk_path_horizontal_layout = QHBoxLayout()
        self.mdk_path_horizontal_layout.setObjectName(u"mdk_path_horizontal_layout")
        self.mdk_path_label = QLabel(self.mdk_path_vertical_group_box)
        self.mdk_path_label.setObjectName(u"mdk_path_label")
        self.mdk_path_label.setMinimumSize(QSize(0, 24))

        self.mdk_path_horizontal_layout.addWidget(self.mdk_path_label)

        self.mdk_path_line_edit = QLineEdit(self.mdk_path_vertical_group_box)
        self.mdk_path_line_edit.setObjectName(u"mdk_path_line_edit")
        self.mdk_path_line_edit.setMinimumSize(QSize(0, 24))
        self.mdk_path_line_edit.setClearButtonEnabled(True)

        self.mdk_path_horizontal_layout.addWidget(self.mdk_path_line_edit)

        self.select_mdk_button = QPushButton(self.mdk_path_vertical_group_box)
        self.select_mdk_button.setObjectName(u"select_mdk_button")
        self.select_mdk_button.setMinimumSize(QSize(0, 24))
        self.select_mdk_button.setMaximumSize(QSize(44, 16777215))

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


        self.verticalLayout_8.addWidget(self.mdk_path_vertical_group_box)

        self.deobf_main_group_box = QGroupBox(self.centralwidget)
        self.deobf_main_group_box.setObjectName(u"deobf_main_group_box")
        self.verticalLayout = QVBoxLayout(self.deobf_main_group_box)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 6, 9, 6)
        self.deobf_group_box = QGroupBox(self.deobf_main_group_box)
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

        self.deobf_algo_group_box = QGroupBox(self.deobf_main_group_box)
        self.deobf_algo_group_box.setObjectName(u"deobf_algo_group_box")
        self.horizontalLayout_10 = QHBoxLayout(self.deobf_algo_group_box)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.deobf_algo_label = QLabel(self.deobf_algo_group_box)
        self.deobf_algo_label.setObjectName(u"deobf_algo_label")

        self.horizontalLayout_10.addWidget(self.deobf_algo_label)

        self.deobf_algo_radio_safe_mdk = QRadioButton(self.deobf_algo_group_box)
        self.deobf_algo_radio_safe_mdk.setObjectName(u"deobf_algo_radio_safe_mdk")
        self.deobf_algo_radio_safe_mdk.setChecked(True)

        self.horizontalLayout_10.addWidget(self.deobf_algo_radio_safe_mdk)

        self.deobf_algo_radio_fast_mdk = QRadioButton(self.deobf_algo_group_box)
        self.deobf_algo_radio_fast_mdk.setObjectName(u"deobf_algo_radio_fast_mdk")

        self.horizontalLayout_10.addWidget(self.deobf_algo_radio_fast_mdk)

        self.deobf_algo_radio_bon2 = QRadioButton(self.deobf_algo_group_box)
        self.deobf_algo_radio_bon2.setObjectName(u"deobf_algo_radio_bon2")
        self.deobf_algo_radio_bon2.setChecked(False)

        self.horizontalLayout_10.addWidget(self.deobf_algo_radio_bon2)

        self.bon2_version_combo_box = QComboBox(self.deobf_algo_group_box)
        self.bon2_version_combo_box.setObjectName(u"bon2_version_combo_box")
        self.bon2_version_combo_box.setEditable(False)
        self.bon2_version_combo_box.setMaxVisibleItems(10)

        self.horizontalLayout_10.addWidget(self.bon2_version_combo_box)

        self.bon2_mappings_combo_box = QComboBox(self.deobf_algo_group_box)
        self.bon2_mappings_combo_box.setObjectName(u"bon2_mappings_combo_box")
        self.bon2_mappings_combo_box.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_10.addWidget(self.bon2_mappings_combo_box)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.help_deobf_algo_button = QPushButton(self.deobf_algo_group_box)
        self.help_deobf_algo_button.setObjectName(u"help_deobf_algo_button")
        sizePolicy.setHeightForWidth(self.help_deobf_algo_button.sizePolicy().hasHeightForWidth())
        self.help_deobf_algo_button.setSizePolicy(sizePolicy)
        self.help_deobf_algo_button.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_10.addWidget(self.help_deobf_algo_button)


        self.verticalLayout.addWidget(self.deobf_algo_group_box)

        self.bon2_cmd_groupbox = QGroupBox(self.deobf_main_group_box)
        self.bon2_cmd_groupbox.setObjectName(u"bon2_cmd_groupbox")
        self.decomp_cmd_horizontal_layout_2 = QHBoxLayout(self.bon2_cmd_groupbox)
        self.decomp_cmd_horizontal_layout_2.setObjectName(u"decomp_cmd_horizontal_layout_2")
        self.decomp_cmd_horizontal_layout_2.setContentsMargins(0, 0, 0, 0)
        self.bon2_cmd_label = QLabel(self.bon2_cmd_groupbox)
        self.bon2_cmd_label.setObjectName(u"bon2_cmd_label")

        self.decomp_cmd_horizontal_layout_2.addWidget(self.bon2_cmd_label)

        self.bon2_cmd_line_edit = QLineEdit(self.bon2_cmd_groupbox)
        self.bon2_cmd_line_edit.setObjectName(u"bon2_cmd_line_edit")
        self.bon2_cmd_line_edit.setClearButtonEnabled(False)

        self.decomp_cmd_horizontal_layout_2.addWidget(self.bon2_cmd_line_edit)

        self.bon2_cmd_reset_button = QPushButton(self.bon2_cmd_groupbox)
        self.bon2_cmd_reset_button.setObjectName(u"bon2_cmd_reset_button")
        sizePolicy.setHeightForWidth(self.bon2_cmd_reset_button.sizePolicy().hasHeightForWidth())
        self.bon2_cmd_reset_button.setSizePolicy(sizePolicy)
        self.bon2_cmd_reset_button.setMaximumSize(QSize(40, 16777215))

        self.decomp_cmd_horizontal_layout_2.addWidget(self.bon2_cmd_reset_button)

        self.help_bon2_cmd_button = QPushButton(self.bon2_cmd_groupbox)
        self.help_bon2_cmd_button.setObjectName(u"help_bon2_cmd_button")
        sizePolicy.setHeightForWidth(self.help_bon2_cmd_button.sizePolicy().hasHeightForWidth())
        self.help_bon2_cmd_button.setSizePolicy(sizePolicy)
        self.help_bon2_cmd_button.setMaximumSize(QSize(20, 16777215))

        self.decomp_cmd_horizontal_layout_2.addWidget(self.help_bon2_cmd_button)


        self.verticalLayout.addWidget(self.bon2_cmd_groupbox)

        self.deobf_threads_group_box = QGroupBox(self.deobf_main_group_box)
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

        self.deobf_failed_group_box = QGroupBox(self.deobf_main_group_box)
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


        self.verticalLayout_8.addWidget(self.deobf_main_group_box)

        self.decomp_main_group_box = QGroupBox(self.centralwidget)
        self.decomp_main_group_box.setObjectName(u"decomp_main_group_box")
        self.verticalLayout_3 = QVBoxLayout(self.decomp_main_group_box)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 6, 9, 6)
        self.decomp_group_box = QGroupBox(self.decomp_main_group_box)
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


        self.verticalLayout_3.addWidget(self.decomp_group_box)

        self.decomp_threads_group_box = QGroupBox(self.decomp_main_group_box)
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


        self.verticalLayout_3.addWidget(self.decomp_threads_group_box)

        self.decomp_cmd_groupbox = QGroupBox(self.decomp_main_group_box)
        self.decomp_cmd_groupbox.setObjectName(u"decomp_cmd_groupbox")
        self.decomp_cmd_horizontal_layout = QHBoxLayout(self.decomp_cmd_groupbox)
        self.decomp_cmd_horizontal_layout.setObjectName(u"decomp_cmd_horizontal_layout")
        self.decomp_cmd_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.decomp_cmd_label = QLabel(self.decomp_cmd_groupbox)
        self.decomp_cmd_label.setObjectName(u"decomp_cmd_label")

        self.decomp_cmd_horizontal_layout.addWidget(self.decomp_cmd_label)

        self.decomp_cmd_line_edit = QLineEdit(self.decomp_cmd_groupbox)
        self.decomp_cmd_line_edit.setObjectName(u"decomp_cmd_line_edit")
        self.decomp_cmd_line_edit.setClearButtonEnabled(False)

        self.decomp_cmd_horizontal_layout.addWidget(self.decomp_cmd_line_edit)

        self.decomp_cmd_reset_button = QPushButton(self.decomp_cmd_groupbox)
        self.decomp_cmd_reset_button.setObjectName(u"decomp_cmd_reset_button")
        sizePolicy.setHeightForWidth(self.decomp_cmd_reset_button.sizePolicy().hasHeightForWidth())
        self.decomp_cmd_reset_button.setSizePolicy(sizePolicy)
        self.decomp_cmd_reset_button.setMaximumSize(QSize(40, 16777215))

        self.decomp_cmd_horizontal_layout.addWidget(self.decomp_cmd_reset_button)

        self.help_decomp_cmd_button = QPushButton(self.decomp_cmd_groupbox)
        self.help_decomp_cmd_button.setObjectName(u"help_decomp_cmd_button")
        sizePolicy.setHeightForWidth(self.help_decomp_cmd_button.sizePolicy().hasHeightForWidth())
        self.help_decomp_cmd_button.setSizePolicy(sizePolicy)
        self.help_decomp_cmd_button.setMaximumSize(QSize(20, 16777215))

        self.decomp_cmd_horizontal_layout.addWidget(self.help_decomp_cmd_button)


        self.verticalLayout_3.addWidget(self.decomp_cmd_groupbox)


        self.verticalLayout_8.addWidget(self.decomp_main_group_box)

        self.merge_main_group_box = QGroupBox(self.centralwidget)
        self.merge_main_group_box.setObjectName(u"merge_main_group_box")
        self.verticalLayout_5 = QVBoxLayout(self.merge_main_group_box)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 6, 9, 6)
        self.groupBox = QGroupBox(self.merge_main_group_box)
        self.groupBox.setObjectName(u"groupBox")
        self.merge_horizontal_layout = QHBoxLayout(self.groupBox)
        self.merge_horizontal_layout.setObjectName(u"merge_horizontal_layout")
        self.merge_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.merge_check_box = QCheckBox(self.groupBox)
        self.merge_check_box.setObjectName(u"merge_check_box")
        self.merge_check_box.setChecked(True)

        self.merge_horizontal_layout.addWidget(self.merge_check_box)

        self.help_merge_button = QPushButton(self.groupBox)
        self.help_merge_button.setObjectName(u"help_merge_button")
        sizePolicy.setHeightForWidth(self.help_merge_button.sizePolicy().hasHeightForWidth())
        self.help_merge_button.setSizePolicy(sizePolicy)
        self.help_merge_button.setMaximumSize(QSize(20, 16777215))

        self.merge_horizontal_layout.addWidget(self.help_merge_button)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.merge_group_box = QGroupBox(self.merge_main_group_box)
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


        self.verticalLayout_5.addWidget(self.merge_group_box)

        self.patch_mdk_group_box = QGroupBox(self.merge_main_group_box)
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


        self.verticalLayout_5.addWidget(self.patch_mdk_group_box)


        self.verticalLayout_8.addWidget(self.merge_main_group_box)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.java_home_main_group_box = QGroupBox(self.centralwidget)
        self.java_home_main_group_box.setObjectName(u"java_home_main_group_box")
        self.verticalLayout_7 = QVBoxLayout(self.java_home_main_group_box)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(9, 6, 9, 6)
        self.bon2_java_home_group_box = QGroupBox(self.java_home_main_group_box)
        self.bon2_java_home_group_box.setObjectName(u"bon2_java_home_group_box")
        self.horizontalLayout_15 = QHBoxLayout(self.bon2_java_home_group_box)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.bon2_java_home_check_box = QCheckBox(self.bon2_java_home_group_box)
        self.bon2_java_home_check_box.setObjectName(u"bon2_java_home_check_box")
        self.bon2_java_home_check_box.setChecked(False)

        self.horizontalLayout_15.addWidget(self.bon2_java_home_check_box)

        self.bon2_java_home_line_edit = QLineEdit(self.bon2_java_home_group_box)
        self.bon2_java_home_line_edit.setObjectName(u"bon2_java_home_line_edit")
        self.bon2_java_home_line_edit.setClearButtonEnabled(False)

        self.horizontalLayout_15.addWidget(self.bon2_java_home_line_edit)

        self.bon2_java_home_combo_box = QComboBox(self.bon2_java_home_group_box)
        self.bon2_java_home_combo_box.setObjectName(u"bon2_java_home_combo_box")
        self.bon2_java_home_combo_box.setMaximumSize(QSize(18, 16777215))
        self.bon2_java_home_combo_box.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_15.addWidget(self.bon2_java_home_combo_box)

        self.bon2_java_home_select_button = QPushButton(self.bon2_java_home_group_box)
        self.bon2_java_home_select_button.setObjectName(u"bon2_java_home_select_button")
        self.bon2_java_home_select_button.setMaximumSize(QSize(44, 16777215))

        self.horizontalLayout_15.addWidget(self.bon2_java_home_select_button)

        self.bon2_java_home_reset_button = QPushButton(self.bon2_java_home_group_box)
        self.bon2_java_home_reset_button.setObjectName(u"bon2_java_home_reset_button")
        sizePolicy.setHeightForWidth(self.bon2_java_home_reset_button.sizePolicy().hasHeightForWidth())
        self.bon2_java_home_reset_button.setSizePolicy(sizePolicy)
        self.bon2_java_home_reset_button.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_15.addWidget(self.bon2_java_home_reset_button)

        self.bon2_decompiler_java_home_button = QPushButton(self.bon2_java_home_group_box)
        self.bon2_decompiler_java_home_button.setObjectName(u"bon2_decompiler_java_home_button")
        sizePolicy.setHeightForWidth(self.bon2_decompiler_java_home_button.sizePolicy().hasHeightForWidth())
        self.bon2_decompiler_java_home_button.setSizePolicy(sizePolicy)
        self.bon2_decompiler_java_home_button.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_15.addWidget(self.bon2_decompiler_java_home_button)


        self.verticalLayout_7.addWidget(self.bon2_java_home_group_box)

        self.mdk_java_home_group_box = QGroupBox(self.java_home_main_group_box)
        self.mdk_java_home_group_box.setObjectName(u"mdk_java_home_group_box")
        self.horizontalLayout_9 = QHBoxLayout(self.mdk_java_home_group_box)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.mdk_java_home_check_box = QCheckBox(self.mdk_java_home_group_box)
        self.mdk_java_home_check_box.setObjectName(u"mdk_java_home_check_box")
        self.mdk_java_home_check_box.setChecked(False)

        self.horizontalLayout_9.addWidget(self.mdk_java_home_check_box)

        self.mdk_java_home_line_edit = QLineEdit(self.mdk_java_home_group_box)
        self.mdk_java_home_line_edit.setObjectName(u"mdk_java_home_line_edit")
        self.mdk_java_home_line_edit.setClearButtonEnabled(False)

        self.horizontalLayout_9.addWidget(self.mdk_java_home_line_edit)

        self.mdk_java_home_combo_box = QComboBox(self.mdk_java_home_group_box)
        self.mdk_java_home_combo_box.setObjectName(u"mdk_java_home_combo_box")
        self.mdk_java_home_combo_box.setMaximumSize(QSize(18, 16777215))
        self.mdk_java_home_combo_box.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_9.addWidget(self.mdk_java_home_combo_box)

        self.mdk_java_home_select_button = QPushButton(self.mdk_java_home_group_box)
        self.mdk_java_home_select_button.setObjectName(u"mdk_java_home_select_button")
        self.mdk_java_home_select_button.setMaximumSize(QSize(44, 16777215))

        self.horizontalLayout_9.addWidget(self.mdk_java_home_select_button)

        self.mdk_java_home_reset_button = QPushButton(self.mdk_java_home_group_box)
        self.mdk_java_home_reset_button.setObjectName(u"mdk_java_home_reset_button")
        sizePolicy.setHeightForWidth(self.mdk_java_home_reset_button.sizePolicy().hasHeightForWidth())
        self.mdk_java_home_reset_button.setSizePolicy(sizePolicy)
        self.mdk_java_home_reset_button.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_9.addWidget(self.mdk_java_home_reset_button)

        self.help_mdk_java_home_button = QPushButton(self.mdk_java_home_group_box)
        self.help_mdk_java_home_button.setObjectName(u"help_mdk_java_home_button")
        sizePolicy.setHeightForWidth(self.help_mdk_java_home_button.sizePolicy().hasHeightForWidth())
        self.help_mdk_java_home_button.setSizePolicy(sizePolicy)
        self.help_mdk_java_home_button.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_9.addWidget(self.help_mdk_java_home_button)


        self.verticalLayout_7.addWidget(self.mdk_java_home_group_box)

        self.decompiler_java_home_group_box = QGroupBox(self.java_home_main_group_box)
        self.decompiler_java_home_group_box.setObjectName(u"decompiler_java_home_group_box")
        self.horizontalLayout_14 = QHBoxLayout(self.decompiler_java_home_group_box)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.decompiler_java_home_check_box = QCheckBox(self.decompiler_java_home_group_box)
        self.decompiler_java_home_check_box.setObjectName(u"decompiler_java_home_check_box")
        self.decompiler_java_home_check_box.setChecked(False)

        self.horizontalLayout_14.addWidget(self.decompiler_java_home_check_box)

        self.decompiler_java_home_line_edit = QLineEdit(self.decompiler_java_home_group_box)
        self.decompiler_java_home_line_edit.setObjectName(u"decompiler_java_home_line_edit")
        self.decompiler_java_home_line_edit.setClearButtonEnabled(False)

        self.horizontalLayout_14.addWidget(self.decompiler_java_home_line_edit)

        self.decompiler_java_home_combo_box = QComboBox(self.decompiler_java_home_group_box)
        self.decompiler_java_home_combo_box.setObjectName(u"decompiler_java_home_combo_box")
        self.decompiler_java_home_combo_box.setMaximumSize(QSize(18, 16777215))
        self.decompiler_java_home_combo_box.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_14.addWidget(self.decompiler_java_home_combo_box)

        self.decompiler_java_home_select_button = QPushButton(self.decompiler_java_home_group_box)
        self.decompiler_java_home_select_button.setObjectName(u"decompiler_java_home_select_button")
        self.decompiler_java_home_select_button.setMaximumSize(QSize(44, 16777215))

        self.horizontalLayout_14.addWidget(self.decompiler_java_home_select_button)

        self.decompiler_java_home_reset_button = QPushButton(self.decompiler_java_home_group_box)
        self.decompiler_java_home_reset_button.setObjectName(u"decompiler_java_home_reset_button")
        sizePolicy.setHeightForWidth(self.decompiler_java_home_reset_button.sizePolicy().hasHeightForWidth())
        self.decompiler_java_home_reset_button.setSizePolicy(sizePolicy)
        self.decompiler_java_home_reset_button.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_14.addWidget(self.decompiler_java_home_reset_button)

        self.help_decompiler_java_home_button = QPushButton(self.decompiler_java_home_group_box)
        self.help_decompiler_java_home_button.setObjectName(u"help_decompiler_java_home_button")
        sizePolicy.setHeightForWidth(self.help_decompiler_java_home_button.sizePolicy().hasHeightForWidth())
        self.help_decompiler_java_home_button.setSizePolicy(sizePolicy)
        self.help_decompiler_java_home_button.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_14.addWidget(self.help_decompiler_java_home_button)


        self.verticalLayout_7.addWidget(self.decompiler_java_home_group_box)


        self.verticalLayout_8.addWidget(self.java_home_main_group_box)

        self.additional_options_group_box = QGroupBox(self.centralwidget)
        self.additional_options_group_box.setObjectName(u"additional_options_group_box")
        self.verticalLayout_6 = QVBoxLayout(self.additional_options_group_box)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, 6, 9, 2)
        self.jar_in_jar_group_box = QGroupBox(self.additional_options_group_box)
        self.jar_in_jar_group_box.setObjectName(u"jar_in_jar_group_box")
        self.jar_in_jar_horizontal_layout = QHBoxLayout(self.jar_in_jar_group_box)
        self.jar_in_jar_horizontal_layout.setObjectName(u"jar_in_jar_horizontal_layout")
        self.jar_in_jar_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.jar_in_jar_check_box = QCheckBox(self.jar_in_jar_group_box)
        self.jar_in_jar_check_box.setObjectName(u"jar_in_jar_check_box")
        self.jar_in_jar_check_box.setChecked(True)

        self.jar_in_jar_horizontal_layout.addWidget(self.jar_in_jar_check_box)

        self.jar_in_jar_help_button = QPushButton(self.jar_in_jar_group_box)
        self.jar_in_jar_help_button.setObjectName(u"jar_in_jar_help_button")
        sizePolicy.setHeightForWidth(self.jar_in_jar_help_button.sizePolicy().hasHeightForWidth())
        self.jar_in_jar_help_button.setSizePolicy(sizePolicy)
        self.jar_in_jar_help_button.setMaximumSize(QSize(20, 16777215))

        self.jar_in_jar_horizontal_layout.addWidget(self.jar_in_jar_help_button)


        self.verticalLayout_6.addWidget(self.jar_in_jar_group_box)

        self.use_cache_group_box = QGroupBox(self.additional_options_group_box)
        self.use_cache_group_box.setObjectName(u"use_cache_group_box")
        self.cache_horizontal_layout = QHBoxLayout(self.use_cache_group_box)
        self.cache_horizontal_layout.setObjectName(u"cache_horizontal_layout")
        self.cache_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.cache_check_box = QCheckBox(self.use_cache_group_box)
        self.cache_check_box.setObjectName(u"cache_check_box")
        self.cache_check_box.setChecked(True)

        self.cache_horizontal_layout.addWidget(self.cache_check_box)

        self.help_cache_button = QPushButton(self.use_cache_group_box)
        self.help_cache_button.setObjectName(u"help_cache_button")
        sizePolicy.setHeightForWidth(self.help_cache_button.sizePolicy().hasHeightForWidth())
        self.help_cache_button.setSizePolicy(sizePolicy)
        self.help_cache_button.setMaximumSize(QSize(20, 16777215))

        self.cache_horizontal_layout.addWidget(self.help_cache_button)


        self.verticalLayout_6.addWidget(self.use_cache_group_box)

        self.commit_after_finish_group_box = QGroupBox(self.additional_options_group_box)
        self.commit_after_finish_group_box.setObjectName(u"commit_after_finish_group_box")
        self.cache_horizontal_layout_2 = QHBoxLayout(self.commit_after_finish_group_box)
        self.cache_horizontal_layout_2.setObjectName(u"cache_horizontal_layout_2")
        self.cache_horizontal_layout_2.setContentsMargins(0, 0, 0, 0)
        self.commit_after_finish_check_box = QCheckBox(self.commit_after_finish_group_box)
        self.commit_after_finish_check_box.setObjectName(u"commit_after_finish_check_box")
        self.commit_after_finish_check_box.setChecked(True)

        self.cache_horizontal_layout_2.addWidget(self.commit_after_finish_check_box)

        self.help_commit_after_finish_button = QPushButton(self.commit_after_finish_group_box)
        self.help_commit_after_finish_button.setObjectName(u"help_commit_after_finish_button")
        sizePolicy.setHeightForWidth(self.help_commit_after_finish_button.sizePolicy().hasHeightForWidth())
        self.help_commit_after_finish_button.setSizePolicy(sizePolicy)
        self.help_commit_after_finish_button.setMaximumSize(QSize(20, 16777215))

        self.cache_horizontal_layout_2.addWidget(self.help_commit_after_finish_button)


        self.verticalLayout_6.addWidget(self.commit_after_finish_group_box)


        self.verticalLayout_8.addWidget(self.additional_options_group_box)

        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setAcceptDrops(False)

        self.verticalLayout_8.addWidget(self.start_button)

        MDGMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MDGMainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1066, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MDGMainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.action_save)
        self.menuFile.addAction(self.action_reset)

        self.retranslateUi(MDGMainWindow)

        QMetaObject.connectSlotsByName(MDGMainWindow)
    # setupUi

    def retranslateUi(self, MDGMainWindow):
        MDGMainWindow.setWindowTitle(QCoreApplication.translate("MDGMainWindow", u"MDG (Mods Decompiler Gui)", None))
        self.action_reset.setText(QCoreApplication.translate("MDGMainWindow", u"reset", None))
        self.action_save.setText(QCoreApplication.translate("MDGMainWindow", u"save", None))
        self.mods_path_label.setText(QCoreApplication.translate("MDGMainWindow", u"Mods folder path:", None))
        self.select_mods_button.setText(QCoreApplication.translate("MDGMainWindow", u"select", None))
        self.help_mods_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.label_5.setText(QCoreApplication.translate("MDGMainWindow", u"accepts drag&drop", None))
        self.mdk_path_label.setText(QCoreApplication.translate("MDGMainWindow", u"MDK archive path:", None))
        self.select_mdk_button.setText(QCoreApplication.translate("MDGMainWindow", u"select", None))
        self.help_mdk_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.label_8.setText(QCoreApplication.translate("MDGMainWindow", u"accepts drag&drop", None))
        self.deobf_main_group_box.setTitle(QCoreApplication.translate("MDGMainWindow", u"Deobfuscation settings:", None))
        self.deobf_check_box.setText(QCoreApplication.translate("MDGMainWindow", u"Deobfuscate mods", None))
        self.help_deobf_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.deobf_algo_label.setText(QCoreApplication.translate("MDGMainWindow", u"Deobfuscation algoritm:", None))
        self.deobf_algo_radio_safe_mdk.setText(QCoreApplication.translate("MDGMainWindow", u"safe (using mdk)", None))
        self.deobf_algo_radio_fast_mdk.setText(QCoreApplication.translate("MDGMainWindow", u"fast (using mdk)", None))
        self.deobf_algo_radio_bon2.setText(QCoreApplication.translate("MDGMainWindow", u"BON2", None))
        self.help_deobf_algo_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.bon2_cmd_label.setText(QCoreApplication.translate("MDGMainWindow", u"BON2 cmd:", None))
        self.bon2_cmd_line_edit.setText("")
        self.bon2_cmd_reset_button.setText(QCoreApplication.translate("MDGMainWindow", u"reset", None))
        self.help_bon2_cmd_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.deobf_threads_label.setText(QCoreApplication.translate("MDGMainWindow", u"Deobfuscation threads:", None))
        self.help_deobf_threads_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.deobf_failed_label.setText(QCoreApplication.translate("MDGMainWindow", u"If deobfuscation of mod failed:", None))
        self.deobf_failed_radio_interrupt.setText(QCoreApplication.translate("MDGMainWindow", u"interrupt", None))
        self.deobf_failed_radio_skip.setText(QCoreApplication.translate("MDGMainWindow", u"skip mod", None))
        self.deobf_failed_radio_decompile.setText(QCoreApplication.translate("MDGMainWindow", u"decompile without deobfuscation", None))
        self.help_deobf_failed_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.decomp_main_group_box.setTitle(QCoreApplication.translate("MDGMainWindow", u"Decompilation settings:", None))
        self.decomp_check_box.setText(QCoreApplication.translate("MDGMainWindow", u"Decompile mods", None))
        self.help_decomp_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.decomp_threads_label.setText(QCoreApplication.translate("MDGMainWindow", u"Decompilation threads:", None))
        self.help_decomp_threads_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.decomp_cmd_label.setText(QCoreApplication.translate("MDGMainWindow", u"Decompilation cmd:", None))
        self.decomp_cmd_line_edit.setText("")
        self.decomp_cmd_reset_button.setText(QCoreApplication.translate("MDGMainWindow", u"reset", None))
        self.help_decomp_cmd_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.merge_main_group_box.setTitle(QCoreApplication.translate("MDGMainWindow", u"Merging settings:", None))
        self.merge_check_box.setText(QCoreApplication.translate("MDGMainWindow", u"Merge result into mdk", None))
        self.help_merge_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.merge_label.setText(QCoreApplication.translate("MDGMainWindow", u"Merge:", None))
        self.merge_code_check_box.setText(QCoreApplication.translate("MDGMainWindow", u"code", None))
        self.merge_resources_check_box.setText(QCoreApplication.translate("MDGMainWindow", u"resources", None))
        self.help_merge_button_2.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.download_sources_check_box.setText(QCoreApplication.translate("MDGMainWindow", u"Patch mdk with \"downloadSources = true\"", None))
        self.help_sources_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
#if QT_CONFIG(tooltip)
        self.java_home_main_group_box.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.java_home_main_group_box.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.java_home_main_group_box.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.java_home_main_group_box.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.java_home_main_group_box.setTitle(QCoreApplication.translate("MDGMainWindow", u"Specify JAVA_HOME:", None))
        self.bon2_java_home_check_box.setText(QCoreApplication.translate("MDGMainWindow", u"BON2          ", None))
        self.bon2_java_home_line_edit.setText("")
        self.bon2_java_home_select_button.setText(QCoreApplication.translate("MDGMainWindow", u"select", None))
        self.bon2_java_home_reset_button.setText(QCoreApplication.translate("MDGMainWindow", u"reset", None))
        self.bon2_decompiler_java_home_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.mdk_java_home_check_box.setText(QCoreApplication.translate("MDGMainWindow", u"mdk            ", None))
        self.mdk_java_home_line_edit.setText("")
        self.mdk_java_home_select_button.setText(QCoreApplication.translate("MDGMainWindow", u"select", None))
        self.mdk_java_home_reset_button.setText(QCoreApplication.translate("MDGMainWindow", u"reset", None))
        self.help_mdk_java_home_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.decompiler_java_home_check_box.setText(QCoreApplication.translate("MDGMainWindow", u"decompiler", None))
        self.decompiler_java_home_line_edit.setText("")
        self.decompiler_java_home_select_button.setText(QCoreApplication.translate("MDGMainWindow", u"select", None))
        self.decompiler_java_home_reset_button.setText(QCoreApplication.translate("MDGMainWindow", u"reset", None))
        self.help_decompiler_java_home_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.additional_options_group_box.setTitle(QCoreApplication.translate("MDGMainWindow", u"Another options:", None))
        self.jar_in_jar_check_box.setText(QCoreApplication.translate("MDGMainWindow", u"Include jar in jar", None))
        self.jar_in_jar_help_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.cache_check_box.setText(QCoreApplication.translate("MDGMainWindow", u"Use cache", None))
        self.help_cache_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.commit_after_finish_check_box.setText(QCoreApplication.translate("MDGMainWindow", u"Make commit after finish", None))
        self.help_commit_after_finish_button.setText(QCoreApplication.translate("MDGMainWindow", u"?", None))
        self.start_button.setText(QCoreApplication.translate("MDGMainWindow", u"start", None))
        self.menuFile.setTitle(QCoreApplication.translate("MDGMainWindow", u"File", None))
    # retranslateUi

