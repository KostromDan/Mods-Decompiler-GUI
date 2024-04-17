# This Python file uses the following encoding: utf-8
import multiprocessing
import os
import sys
import zipfile
from collections import defaultdict, OrderedDict
from typing import Any, Optional

import psutil
from PySide6.QtCore import QMimeData, QCoreApplication, QTimer, Qt
from PySide6.QtGui import QDropEvent, QDragEnterEvent, QDragLeaveEvent, QCloseEvent, QFontMetrics
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QFileSystemModel, QCompleter, QWidget, QLineEdit, \
    QSlider, QSpinBox, QPushButton, QComboBox, QApplication

from MDGUi.generated.Ui_MDGMainWindow import Ui_MDGMainWindow
from MDGUtil import UiUtils, PathUtils, BON2Utils
from MDGUtil.LocalConfig import LocalConfig
from MDGWindow.MDGHelpWindow import MDGHelpWindow
from MDGWindow.MDGProgressWindow import MDGProgressWindow


class MDGMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MDGMainWindow()
        self.ui.setupUi(self)

        self.config = LocalConfig()
        self.was_decomp_enabled = False
        self.serialized_widgets = None
        self.progress_window = None
        self.adjusting_min_height = False
        self.default_cmd_configs = dict()

        self.bon2_mappings = BON2Utils.DEFAULT_MAPPINGS

        if self.config.is_first_launch():
            QMessageBox.information(self, 'First launch information',
                                    'Welcome to MDG (Mods Decompiler Gui)!\n'
                                    'Please check the license of all mods that you are going to use with this tool.\n'
                                    'Otherwise, usage of this tool can lead to license infringement.\n'
                                    'If you are not sure how to use the tool or which options you need, click "?".\n'
                                    'It will provide useful information and tips.',
                                    QMessageBox.StandardButton.Ok)

        self.ui.deobf_check_box.stateChanged.connect(self.check_widgets_visibility)
        self.ui.merge_check_box.stateChanged.connect(self.check_widgets_visibility)
        self.ui.decomp_check_box.stateChanged.connect(self.check_widgets_visibility)

        self.ui.deobf_algo_radio_safe_mdk.toggled.connect(self.check_widgets_visibility)
        self.ui.deobf_algo_radio_fast_mdk.toggled.connect(self.check_widgets_visibility)
        self.ui.deobf_algo_radio_bon2.toggled.connect(self.check_widgets_visibility)

        self.setup_select_button(self.ui.select_mods_button,
                                 self.ui.mods_path_line_edit,
                                 'Select mods folder',
                                 QFileDialog.getExistingDirectory,
                                 QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        self.setup_select_button(self.ui.select_mdk_button,
                                 self.ui.mdk_path_line_edit,
                                 'Select mdk archive',
                                 QFileDialog.getOpenFileName,
                                 self.tr('Archive files (*.zip)'))
        self.setup_select_button(self.ui.bon2_path_select_button,
                                 self.ui.bon2_path_line_edit,
                                 'Select bon2',
                                 QFileDialog.getOpenFileName,
                                 self.tr('Jar files (*.jar)'))

        self.setup_drag_n_drop(self.ui.mods_path_vertical_group_box, self.ui.mods_path_line_edit)
        self.setup_drag_n_drop(self.ui.mdk_path_vertical_group_box, self.ui.mdk_path_line_edit)

        self.ui.start_button.clicked.connect(self.start_button)

        self.ui.mods_path_line_edit.textChanged.connect(lambda: self.ui.mods_path_line_edit.setStyleSheet(''))

        self.ui.mdk_path_line_edit.textChanged.connect(lambda: self.ui.mdk_path_line_edit.setStyleSheet(''))

        self.set_path_completer(self.ui.mods_path_line_edit)
        self.set_path_completer(self.ui.mdk_path_line_edit)

        free_memory_in_gb = psutil.virtual_memory().available / (1024.0 ** 3)
        recommended_threads_ram = int((free_memory_in_gb - 1) / 0.5)  # deobfuscation thread eat 0.5 gb in middle case
        recommended_threads_cpu = multiprocessing.cpu_count()

        recommended_threads = max(1, min(recommended_threads_ram, recommended_threads_cpu))

        self.setup_slider_and_spinbox_pair(self.ui.deobf_threads_spin_box,
                                           self.ui.deobf_threads_horizontal_slider)
        self.setup_slider_and_spinbox_pair(self.ui.decomp_threads_spin_box,
                                           self.ui.decomp_threads_horizontal_slider)

        self.ui.deobf_threads_horizontal_slider.setValue(recommended_threads)
        self.ui.decomp_threads_horizontal_slider.setValue(recommended_threads)

        self.help_window = MDGHelpWindow()

        self.help_widget_pairs = {
            self.ui.help_mdk_button: self.help_window.ui.mdk_path,
            self.ui.help_deobf_button: self.help_window.ui.deobf_mods,
            self.ui.help_merge_button: self.help_window.ui.merge,
            self.ui.help_mods_button: self.help_window.ui.mods_path,
            self.ui.help_merge_button_2: self.help_window.ui.merge_resources,
            self.ui.help_decomp_button: self.help_window.ui.decomp_mods,
            self.ui.help_deobf_failed_button: self.help_window.ui.deobf_failed,
            self.ui.help_sources_button: self.help_window.ui.patch_mdk,
            self.ui.help_decomp_threads_button: self.help_window.ui.threads,
            self.ui.help_deobf_threads_button: self.help_window.ui.threads,
            self.ui.help_decomp_cmd_button: self.help_window.ui.decomp_cmd,
            self.ui.help_cache_button: self.help_window.ui.cache,
            self.ui.jar_in_jar_help_button: self.help_window.ui.jar_in_jar,
            self.ui.help_deobf_algo_button: self.help_window.ui.deobf_algo,
            self.ui.help_bon2_cmd_button: self.help_window.ui.deobf_algo,
            self.ui.help_bon2_java_home_button: self.help_window.ui.java_home,
            self.ui.help_mdk_java_home_button: self.help_window.ui.java_home,
            self.ui.help_decompiler_java_home_button: self.help_window.ui.java_home,
            self.ui.help_bon2_path_button: self.help_window.ui.deobf_algo,
            self.ui.help_decomp_logging_button: self.help_window.ui.decomp_logging,
        }
        for help_button, widget in self.help_widget_pairs.items():
            help_button.clicked.connect(self.help_button_clicked)

        self.java_home_dict = {
            self.ui.mdk_java_home_group_box: {
                'check_box': self.ui.mdk_java_home_check_box,
                'line_edit': self.ui.mdk_java_home_line_edit,
                'select_button': self.ui.mdk_java_home_select_button,
                'reset_button': self.ui.mdk_java_home_reset_button,
                'combo_box': self.ui.mdk_java_home_combo_box,
            },
            self.ui.bon2_java_home_group_box: {
                'check_box': self.ui.bon2_java_home_check_box,
                'line_edit': self.ui.bon2_java_home_line_edit,
                'select_button': self.ui.bon2_java_home_select_button,
                'reset_button': self.ui.bon2_java_home_reset_button,
                'combo_box': self.ui.bon2_java_home_combo_box,
            },
            self.ui.decompiler_java_home_group_box: {
                'check_box': self.ui.decompiler_java_home_check_box,
                'line_edit': self.ui.decompiler_java_home_line_edit,
                'select_button': self.ui.decompiler_java_home_select_button,
                'reset_button': self.ui.decompiler_java_home_reset_button,
                'combo_box': self.ui.decompiler_java_home_combo_box,
            }
        }
        for group_box, data in self.java_home_dict.items():
            data['check_box'].stateChanged.connect(self.check_widgets_visibility)
            self.set_path_completer(data['line_edit'])
            self.setup_line_edit_resettable_pair(data['line_edit'],
                                                 data['reset_button'],
                                                 PathUtils.get_java_home())
            data['line_edit'].setText(PathUtils.get_java_home())
            self.setup_select_button(data['select_button'],
                                     data['line_edit'],
                                     'Select JAVA_HOME folder',
                                     QFileDialog.getExistingDirectory,
                                     QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
            self.setup_java_home_combo_box(data['combo_box'], data['line_edit'])

        self.setup_line_edit_resettable_pair(self.ui.decomp_cmd_line_edit,
                                             self.ui.decomp_cmd_reset_button,
                                             PathUtils.DEFAULT_DECOMPILER_CMD)
        self.setup_line_edit_resettable_pair(self.ui.bon2_cmd_line_edit,
                                             self.ui.bon2_cmd_reset_button,
                                             PathUtils.DEFAULT_BON2_CMD)

        self.setup_line_edit_resettable_pair(self.ui.bon2_path_line_edit,
                                             self.ui.bon2_path_reset_button,
                                             PathUtils.BON2_PATH)

        self.ui.action_reset.triggered.connect(self.action_reset)
        self.ui.action_save.triggered.connect(self.save_ui_to_config)
        self.ui.action_adjust_height.triggered.connect(self.adjust_min_height)
        self.ui.action_open_log.triggered.connect(PathUtils.open_log)

        self.ui.bon2_version_combo_box.currentTextChanged.connect(self.bon2_version_changed)
        self.ui.bon2_version_combo_box.addItems(self.bon2_mappings.keys())

        self.change_visibility_of_widget(self.ui.commit_after_finish_group_box, False)  # NotImplemented yet

        self.load_ui_from_config()
        self.check_widgets_visibility()
        QTimer.singleShot(3000,
                          lambda: self.ui.scrollArea.setMinimumWidth(self.ui.scrollArea.widget().sizeHint().width()))
        self.adjust_min_height()

        if PathUtils.get_java_home() == '':
            QTimer.singleShot(20, UiUtils.show_java_not_found_message_box)

    def fit_window_to_screen(self):
        if self.geometry().bottom() > QApplication.primaryScreen().geometry().bottom():
            self.resize(self.width(),
                        self.height() - 100 - self.geometry().bottom() + QApplication.primaryScreen().geometry().bottom())

    def setup_java_home_combo_box(self, combo_box: QComboBox, line_edit: QLineEdit):
        combo_box.addItems(PathUtils.get_all_java_homes())
        font_metrics = QFontMetrics(combo_box.font())
        longest_width = 0
        for index in range(combo_box.count()):
            item_width = font_metrics.boundingRect(combo_box.itemText(index)).width()
            longest_width = max(longest_width, item_width)
        combo_box.view().setFixedWidth(longest_width + 8)
        combo_box.view().setLayoutDirection(Qt.LeftToRight)
        combo_box.activated.connect(lambda: self.java_home_combo_box_activated(combo_box, line_edit))

    def java_home_combo_box_activated(self, combo_box: QComboBox, line_edit: QLineEdit):
        line_edit.setText(combo_box.currentText())

    def bon2_version_changed(self, value: str) -> None:
        self.ui.bon2_mappings_combo_box.clear()
        self.ui.bon2_mappings_combo_box.addItems(self.bon2_mappings[value])

    def setup_line_edit_resettable_pair(self, line_edit: QLineEdit,
                                        reset_bitton: QPushButton,
                                        default_value: str) -> None:
        reset_bitton.clicked.connect(lambda: line_edit.setText(default_value))
        line_edit.textChanged.connect(
            lambda: self.on_resettable_line_edit_changed(line_edit, reset_bitton, default_value))
        line_edit.setText(default_value)

    def on_resettable_line_edit_changed(self, line_edit: QLineEdit,
                                        reset_bitton: QPushButton,
                                        default_value: str) -> None:
        text = line_edit.text()
        reset_bitton.setEnabled(text != default_value)
        config_name = f'using_default_{line_edit.objectName()}'
        self.default_cmd_configs[config_name] = line_edit.objectName()
        self.config.set(config_name, text == default_value)
        line_edit.setStyleSheet('')

    def action_reset(self) -> None:
        self.setEnabled(False)
        self.config.reset()
        self.config.is_first_launch()
        widget = MDGMainWindow()
        widget.show()
        self.destroy()

    def setup_select_button(self, button: QPushButton,
                            line_edit: QLineEdit,
                            msg: str,
                            get_from: callable,
                            options: Any) -> None:
        button.clicked.connect(lambda e: self.select_button(line_edit,
                                                            msg,
                                                            get_from,
                                                            options))

    def select_button(self, line_edit: QLineEdit,
                      msg: str,
                      get_from: callable,
                      options: Any) -> None:
        line_edit_path = line_edit.text()
        if not os.path.exists(line_edit_path):
            line_edit_path = ''
        selected = get_from(self, self.tr(msg), line_edit_path, options)
        if type(selected) is tuple:
            selected = selected[0]
        if selected == '':
            return
        line_edit.setText(selected)
        self.set_path_completer(line_edit)

    def setup_slider_and_spinbox_pair(self, spin_box: QSpinBox, slider: QSlider) -> None:
        slider.valueChanged.connect(lambda value: spin_box.setValue(value))
        spin_box.valueChanged.connect(lambda value: slider.setValue(value))

    def setup_drag_n_drop(self, element: QWidget, line_edit: QLineEdit) -> None:
        element.dragEnterEvent = lambda event: self.drag_enter_event(event, element)
        element.dragLeaveEvent = lambda event: self.drag_leave_event(event, element)
        element.dropEvent = lambda event: self.drag_drop_event(event, element, line_edit)

    def drag_leave_event(self, event: QDragLeaveEvent, element: QWidget) -> None:
        element.setStyleSheet('')

    def drag_drop_event(self, event: QDropEvent, element: QWidget, line_edit: QLineEdit) -> None:
        result = self.drop_event(event)
        if result is not None:
            line_edit.setText(result)
        element.setStyleSheet('')

    def drop_event(self, event: QDropEvent) -> Optional[str]:
        mime_data: QMimeData = event.mimeData()
        if not mime_data.hasUrls():
            event.ignore()
            return
        file_paths = [url.toLocalFile() for url in mime_data.urls()]
        if len(file_paths) != 1:
            QMessageBox.warning(self, 'Incorrect file selection', f'Dropped {len(file_paths)} files, 1 expected!',
                                QMessageBox.StandardButton.Ok)
            return
        event.accept()
        return file_paths[0]

    def make_red_and_visible(self, widget: QWidget) -> None:
        widget.setStyleSheet('border: 1px solid red')
        self.ui.scrollArea.ensureWidgetVisible(widget)

    def help_button_clicked(self) -> None:
        self.help_window.start_help_window(self.help_widget_pairs[self.sender()])

    def start_button(self) -> None:
        self.save_ui_to_config()
        mods_folder_path = self.ui.mods_path_line_edit.text()
        if not os.path.exists(mods_folder_path):
            self.make_red_and_visible(self.ui.mods_path_line_edit)
            QMessageBox.warning(self, 'Incorrect path', 'Path not exists!\n'
                                                        'Check mods folder path.',
                                QMessageBox.StandardButton.Ok)
            return
        if not os.path.isdir(mods_folder_path):
            self.make_red_and_visible(self.ui.mods_path_line_edit)
            QMessageBox.warning(self, 'Incorrect path', 'Path is not to folder!\n'
                                                        'Check mods folder path.',
                                QMessageBox.StandardButton.Ok)
            return
        for mod in os.listdir(mods_folder_path):
            if mod.endswith('.jar'):
                break
        else:
            self.make_red_and_visible(self.ui.mods_path_line_edit)
            QMessageBox.warning(self, 'Incorrect path', 'Not found a single .jar file in mods folder!\n'
                                                        'Check mods folder path.',
                                QMessageBox.StandardButton.Ok)
            return
        if self.ui.mdk_path_vertical_group_box.isEnabled():
            mdk_path = self.ui.mdk_path_line_edit.text()
            if not os.path.exists(mdk_path):
                self.make_red_and_visible(self.ui.mdk_path_line_edit)
                QMessageBox.warning(self, 'Incorrect path', 'Path not exists!\n'
                                                            'Check mdk archive path.',
                                    QMessageBox.StandardButton.Ok)
                return
            if not zipfile.is_zipfile(mdk_path):
                self.make_red_and_visible(self.ui.mdk_path_line_edit)
                QMessageBox.warning(self, 'Incorrect path', 'Path is not to zip archive!\n'
                                                            'Check mdk archive path.',
                                    QMessageBox.StandardButton.Ok)
                return
            with zipfile.ZipFile(mdk_path) as mdk:
                try:
                    with mdk.open('build.gradle'):
                        pass
                except KeyError:
                    self.make_red_and_visible(self.ui.mdk_path_line_edit)
                    QMessageBox.warning(self, 'Incorrect path', '"build.gradle" not found in mdk!\n'
                                                                'Check that mdk is valid.',
                                        QMessageBox.StandardButton.Ok)
                    return
        if not self.ui.deobf_check_box.isChecked() and not self.ui.decomp_check_box.isChecked():
            QMessageBox.warning(self, 'Incorrect configuration', 'With this configuration program will do nothing.',
                                QMessageBox.StandardButton.Ok)
            return
        if UiUtils.is_checked_and_enabled(self.ui.deobf_algo_radio_bon2):
            if not os.path.exists(self.ui.bon2_path_line_edit.text()):
                self.make_red_and_visible(self.ui.bon2_path_line_edit)
                QMessageBox.warning(self, 'Incorrect path', "Bon2 path doesn't exists.",
                                    QMessageBox.StandardButton.Ok)
        for group_box, data in self.java_home_dict.items():
            if not data['line_edit'].isEnabled():
                continue
            try:
                PathUtils.get_path_to_java(data['line_edit'].text())
            except FileNotFoundError:
                self.make_red_and_visible(data['line_edit'])
                QMessageBox.warning(self, 'Incorrect JAVA_HOME path',
                                    "Can't find executable java in this path.\n"
                                    'Check this JAVA_HOME path.',
                                    QMessageBox.StandardButton.Ok)
                return
        self.serialized_widgets = self.serialize_to_dict()
        self.progress_window = MDGProgressWindow(self)
        self.progress_window.show()
        self.setEnabled(False)
        self.hide()
        self.progress_window.start()

    def serialize_to_dict(self) -> dict[str, dict[str, Any]]:
        out = defaultdict(dict)
        members = [attr for attr in dir(self.ui) if not callable(getattr(self.ui, attr)) and not attr.startswith('__')]
        for member_name in members:
            member_object = getattr(self.ui, member_name)
            member_attrs = [attr for attr in dir(member_object) if not attr.startswith('__')]
            required_fields = ('text', 'value', 'isChecked', 'isEnabled', 'currentText')
            out[member_name]['class'] = type(member_object).__name__
            for field in required_fields:
                if field in member_attrs:
                    out[member_name][field] = getattr(member_object, field)()
        return out

    def save_ui_to_config(self) -> None:
        serialized_widgets = self.serialize_to_dict()
        for config, line_edit in self.default_cmd_configs.items():
            if self.config.get(config) is True:
                serialized_widgets.pop(line_edit)
        serialized_widgets.pop('cache_check_box')
        self.config.set('serialized_widgets', serialized_widgets)

    def load_ui_from_config(self) -> None:
        serialized_widgets = self.config.get('serialized_widgets')
        if serialized_widgets != '':
            self.deserialize_ui_from_dict(serialized_widgets)

    def deserialize_ui_from_dict(self, serialized_dict: dict[str, dict[str]]) -> None:
        get_set_pairs = {
            'text': 'setText',
            'currentText': 'setCurrentText',
            'value': 'setValue',
            'class': 'skip',
            'isChecked': 'setChecked',
            'isEnabled': 'setEnabled'
        }
        required = {'QCheckBox': {'isChecked'},
                    'QLineEdit': {'text'},
                    'QComboBox': {'currentText'},
                    'QRadioButton': {'isChecked'},
                    'QSlider': {'value'},
                    'QSpinBox': {'value'}}
        skip = {'setEnabled', 'skip'}
        widgets_priority = ['bon2_version_combo_box', 'bon2_mappings_combo_box']

        def find_index_with_default(lst, elem, default):
            try:
                index = lst.index(elem)
            except ValueError:
                index = default
            return index

        serialized_dict = OrderedDict(sorted(serialized_dict.items(), key=lambda x: (
            find_index_with_default(widgets_priority, x[0], len(widgets_priority)), x[0])))

        for member_name, member_fields_dict in serialized_dict.items():
            try:
                member_object = getattr(self.ui, member_name)
            except AttributeError:
                continue
            class_name = type(member_object).__name__
            if class_name not in required:
                continue
            for field_name, field_value in member_fields_dict.items():
                if field_name not in required[class_name]:
                    continue
                try:
                    pair_filed_name = get_set_pairs[field_name]
                    if pair_filed_name in skip:
                        continue
                    getattr(member_object, pair_filed_name)(field_value)
                except AttributeError:
                    continue

    def critical_from_progress_window(self, title: str, text: str, widget_name: str) -> None:
        if widget_name not in [None, '']:
            self.make_red_and_visible(getattr(self.ui, widget_name))
        self.setEnabled(True)
        self.show()
        QMessageBox.critical(self, title, text, QMessageBox.StandardButton.Ok)

    def drag_enter_event(self, event: QDragEnterEvent, element: QWidget) -> None:
        if event.mimeData().hasUrls():
            event.accept()
            element.setObjectName('vertical_group_box')
            element.setStyleSheet('#vertical_group_box { border: 2px solid blue; }')
        else:
            event.ignore()

    def closeEvent(self, event: QCloseEvent) -> None:
        self.save_ui_to_config()
        event.accept()
        sys.exit()

    def set_path_completer(self, line_edit: QLineEdit) -> None:
        initial_path = line_edit.text()
        fs_model = QFileSystemModel(line_edit)
        fs_model.setRootPath(initial_path)
        fs_completer = QCompleter(fs_model, line_edit)
        line_edit.setCompleter(fs_completer)

    def get_min_height(self) -> int:
        current_scroll_area_height = self.ui.scrollArea.height()
        min_scroll_area_height = self.ui.scrollArea.widget().minimumSizeHint().height() + 2
        dif = min_scroll_area_height - current_scroll_area_height
        return self.height() + dif

    def adjust_min_height(self, recursive=False) -> None:
        if not recursive and self.adjusting_min_height:
            return
        self.adjusting_min_height = True
        min_height = self.get_min_height()
        if min_height != self.height():
            self.resize(self.width(), min_height)
            QCoreApplication.processEvents()
            QTimer.singleShot(20, lambda: self.adjust_min_height(True))
        else:
            self.fit_window_to_screen()
            self.adjusting_min_height = False

    def change_visibility_of_widget(self, element: QWidget, visible: bool) -> None:
        was_min_size = self.get_min_height() == self.height()
        element.setVisible(visible)
        element.setEnabled(visible)
        if was_min_size:
            self.adjust_min_height()

    def check_widgets_visibility(self, recursive: int = 0) -> None:
        """Setting visibility of widgets according to settings."""
        if recursive == 0:
            QTimer.singleShot(0, lambda: self.check_widgets_visibility(3))

        QCoreApplication.processEvents()
        fast_deobf_selected = self.ui.deobf_algo_radio_fast_mdk.isChecked()
        if fast_deobf_selected:
            self.ui.deobf_algo_radio_safe_mdk.setChecked(True)
            fast_deobf_selected = False  # NotImplemented
            QMessageBox.warning(self, 'NotImplemented', 'Fast unsafe mdk deobf algorithm will be '
                                                        'released in one of the next updates.',
                                QMessageBox.StandardButton.Ok)
        deobfuscation_enabled = UiUtils.is_checked_and_enabled(self.ui.deobf_check_box)
        decompilation_enabled = UiUtils.is_checked_and_enabled(self.ui.decomp_check_box)
        merging_enabled = UiUtils.is_checked_and_enabled(self.ui.merge_check_box)
        deobfuscation_algo_using_mdk = (self.ui.deobf_algo_radio_safe_mdk.isChecked() or
                                        self.ui.deobf_algo_radio_fast_mdk.isChecked())
        mdk_widgets_visible = ((deobfuscation_enabled and deobfuscation_algo_using_mdk) or merging_enabled)
        bon2_widgets_visible = (deobfuscation_enabled and
                                UiUtils.is_checked_and_enabled(self.ui.deobf_algo_radio_bon2))
        at_least_one_java_home_active = (mdk_widgets_visible or
                                         bon2_widgets_visible or
                                         decompilation_enabled)

        fail_logic_radio_buttons = (self.ui.deobf_failed_radio_interrupt,
                                    self.ui.deobf_failed_radio_skip,
                                    self.ui.deobf_failed_radio_decompile,)
        deobf_algo_radio_buttons = (self.ui.deobf_algo_radio_safe_mdk,
                                    self.ui.deobf_algo_radio_fast_mdk,
                                    self.ui.deobf_algo_radio_bon2)

        """is mdk needed"""
        self.change_visibility_of_widget(self.ui.mdk_path_vertical_group_box, mdk_widgets_visible)
        self.change_visibility_of_widget(self.ui.mdk_java_home_group_box, mdk_widgets_visible)

        """bon2 widgets"""
        self.change_visibility_of_widget(self.ui.bon2_cmd_groupbox, bon2_widgets_visible)
        self.change_visibility_of_widget(self.ui.bon2_java_home_group_box, bon2_widgets_visible)
        self.change_visibility_of_widget(self.ui.bon2_version_combo_box, bon2_widgets_visible)
        self.change_visibility_of_widget(self.ui.bon2_mappings_combo_box, bon2_widgets_visible)
        self.change_visibility_of_widget(self.ui.bon2_path_group_box, bon2_widgets_visible)

        """deobf widgets"""
        self.change_visibility_of_widget(self.ui.deobf_failed_group_box, deobfuscation_enabled)
        self.change_visibility_of_widget(self.ui.deobf_threads_group_box, deobfuscation_enabled and
                                         not self.ui.deobf_algo_radio_fast_mdk.isChecked())
        self.change_visibility_of_widget(self.ui.deobf_algo_group_box, deobfuscation_enabled)

        self.ui.deobf_failed_radio_decompile.setEnabled(decompilation_enabled and not fast_deobf_selected)
        self.ui.deobf_failed_radio_skip.setEnabled(not fast_deobf_selected)

        """decomp widgets"""
        self.change_visibility_of_widget(self.ui.decomp_threads_group_box, decompilation_enabled)
        self.change_visibility_of_widget(self.ui.decomp_cmd_groupbox, decompilation_enabled)
        self.change_visibility_of_widget(self.ui.decompiler_java_home_group_box, decompilation_enabled)
        self.change_visibility_of_widget(self.ui.decomp_logging_group_box, decompilation_enabled)

        """merge widgets"""
        self.change_visibility_of_widget(self.ui.merge_main_group_box, decompilation_enabled)
        self.change_visibility_of_widget(self.ui.merge_group_box, merging_enabled)
        self.change_visibility_of_widget(self.ui.patch_mdk_group_box, merging_enabled)

        """java home"""
        self.change_visibility_of_widget(self.ui.java_home_main_group_box, at_least_one_java_home_active)
        for group_box, data in self.java_home_dict.items():
            check_box_checked = data['check_box'].isChecked()
            for widget_name in {'line_edit', 'select_button', 'combo_box'}:
                data[widget_name].setEnabled(check_box_checked)
            is_default_line_edit = data['line_edit'].text() == PathUtils.get_java_home()
            data['reset_button'].setEnabled(check_box_checked and not is_default_line_edit)
            if self.sender() == data['check_box'] and not check_box_checked:
                data['line_edit'].setText(PathUtils.get_java_home())

        """fail logic radio buttons"""
        if self.ui.deobf_failed_group_box.isEnabled():
            for radio in fail_logic_radio_buttons:
                if radio.isChecked() and not radio.isEnabled():
                    self.ui.deobf_failed_radio_interrupt.setChecked(True)
                    if radio == self.ui.deobf_failed_radio_decompile:
                        self.was_decomp_enabled = True
        if self.sender() in deobf_algo_radio_buttons or self.sender() is self.ui.decomp_check_box:
            if self.was_decomp_enabled and self.ui.deobf_failed_radio_decompile.isEnabled():
                self.was_decomp_enabled = False
                self.ui.deobf_failed_radio_decompile.setChecked(True)

        if recursive > 1:
            QTimer.singleShot(0, lambda: self.check_widgets_visibility(recursive=recursive - 1))
