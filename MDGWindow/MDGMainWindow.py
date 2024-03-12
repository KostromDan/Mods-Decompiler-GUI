# This Python file uses the following encoding: utf-8
import multiprocessing
import os
import sys
import zipfile
from collections import defaultdict
from typing import Any, Optional, Union

from MDGUi.Ui_MDGMainWindow import Ui_MDGMainWindow
from PySide6.QtCore import QMimeData
from PySide6.QtGui import QDropEvent, QDragEnterEvent, QDragLeaveEvent, QCloseEvent
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QFileSystemModel, QCompleter, QWidget, QLineEdit, \
    QSlider, QSpinBox

from MDGUtil.LocalConfig import LocalConfig, DEFAULT_DECOMPILER_CMD
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

        if self.config.is_first_launch():
            QMessageBox.information(self, 'First launch information',
                                    'Welcome to MDG (Mods Decompiler Gui)!\n'
                                    'Please check the license of all mods that you are going to use with this tool.\n'
                                    'Otherwise, usage of this tool can lead to license infringement.\n'
                                    'If you are not sure how to use the tool or which options you need, click "?".\n'
                                    'It will provide useful information and tips.',
                                    QMessageBox.StandardButton.Ok)

        self.ui.deobf_check_box.stateChanged.connect(self.deobf_checkbox_changed)
        self.ui.merge_check_box.stateChanged.connect(self.merge_checkbox_changed)
        self.ui.decomp_check_box.stateChanged.connect(self.decomp_checkbox_changed)

        self.ui.select_mods_button.clicked.connect(self.select_mods_button)
        self.ui.select_mdk_button.clicked.connect(self.select_mdk_button)

        self.setup_drag_n_drop(self.ui.mods_path_vertical_group_box, self.ui.mods_path_line_edit)
        self.setup_drag_n_drop(self.ui.mdk_path_vertical_group_box, self.ui.mdk_path_line_edit)

        self.ui.start_button.clicked.connect(self.start_button)

        self.ui.mods_path_line_edit.setText(self.config.get('mods_line_edit'))
        self.ui.mods_path_line_edit.textChanged.connect(self.mods_line_edit_changed)

        self.ui.mdk_path_line_edit.setText(self.config.get('mdk_line_edit'))
        self.ui.mdk_path_line_edit.textChanged.connect(self.mdk_line_edit_changed)

        if self.config.get('deobf_threads') == '':
            self.config.set('deobf_threads', multiprocessing.cpu_count())
        if self.config.get('decomp_threads') == '':
            self.config.set('decomp_threads', multiprocessing.cpu_count())

        self.setup_slider_and_spinbox_pair(self.ui.deobf_threads_spin_box,
                                           self.ui.deobf_threads_horizontal_slider,
                                           'deobf_threads')
        self.setup_slider_and_spinbox_pair(self.ui.decomp_threads_spin_box,
                                           self.ui.decomp_threads_horizontal_slider,
                                           'decomp_threads')

        self.ui.deobf_threads_horizontal_slider.setValue(self.config.get('deobf_threads'))
        self.ui.decomp_threads_horizontal_slider.setValue(self.config.get('decomp_threads'))

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
        }
        for help_button, widget in self.help_widget_pairs.items():
            help_button.clicked.connect(self.help_button_clicked)

        # added to set the file system completer for mods_path_line_edit
        self.set_path_completer(self.ui.mods_path_line_edit)
        self.set_path_completer(self.ui.mdk_path_line_edit)

        self.resize(self.width(), self.minimumSizeHint().height())

        self.ui.decomp_cmd_reset_button.clicked.connect(self.reset_decomp_cmd)
        self.ui.decomp_cmd_line_edit.textChanged.connect(self.decomp_cmd_line_edit_changed)

        self.ui.decomp_cmd_line_edit.setText(
            self.config.get('decomp_cmd') if self.config.get('decomp_cmd') != '' else DEFAULT_DECOMPILER_CMD)

    def setup_slider_and_spinbox_pair(self, spin_box: QSpinBox, slider: QSlider, config_name: str) -> None:
        slider.valueChanged.connect(lambda value: self.slider_value_changed(value, spin_box, config_name))
        spin_box.valueChanged.connect(lambda value: self.spin_box_value_changed(value, slider))

    def slider_value_changed(self, value: int, spinbox: QSpinBox, config_name: str) -> None:
        spinbox.setValue(value)
        self.config.set(config_name, value)

    def spin_box_value_changed(self, value: int, slider: QSlider) -> None:
        slider.setValue(value)

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

    def decomp_cmd_line_edit_changed(self, value: str) -> None:
        self.ui.decomp_cmd_reset_button.setEnabled(value != DEFAULT_DECOMPILER_CMD)
        self.config.set('decomp_cmd', value if value != DEFAULT_DECOMPILER_CMD else '')
        self.ui.decomp_cmd_line_edit.setStyleSheet('')

    def reset_decomp_cmd(self) -> None:
        self.ui.decomp_cmd_line_edit.setText(DEFAULT_DECOMPILER_CMD)

    def help_button_clicked(self) -> None:
        self.help_window.start_help_window(self.help_widget_pairs[self.sender()])

    def mods_line_edit_changed(self, text: str) -> None:
        self.config.set('mods_line_edit', text)
        self.ui.mods_path_line_edit.setStyleSheet('')

    def mdk_line_edit_changed(self, text: str) -> None:
        self.config.set('mdk_line_edit', text)
        self.ui.mdk_path_line_edit.setStyleSheet('')

    def start_button(self) -> None:
        mods_folder_path = self.ui.mods_path_line_edit.text()
        if not os.path.exists(mods_folder_path):
            self.ui.mods_path_line_edit.setStyleSheet('border: 1px solid red')
            QMessageBox.warning(self, 'Incorrect path', 'Path not exists!\n'
                                                        'Check mods folder path.',
                                QMessageBox.StandardButton.Ok)
            return
        if not os.path.isdir(mods_folder_path):
            self.ui.mods_path_line_edit.setStyleSheet('border: 1px solid red')
            QMessageBox.warning(self, 'Incorrect path', 'Path is not to folder!\n'
                                                        'Check mods folder path.',
                                QMessageBox.StandardButton.Ok)
            return
        for mod in os.listdir(mods_folder_path):
            if mod.endswith('.jar'):
                break
        else:
            self.ui.mods_path_line_edit.setStyleSheet('border: 1px solid red')
            QMessageBox.warning(self, 'Incorrect path', 'Not found a single .jar file in mods folder!\n'
                                                        'Check mods folder path.',
                                QMessageBox.StandardButton.Ok)
            return
        if self.ui.mdk_path_vertical_group_box.isEnabled():
            mdk_path = self.ui.mdk_path_line_edit.text()
            if not os.path.exists(mdk_path):
                self.ui.mdk_path_line_edit.setStyleSheet('border: 1px solid red')
                QMessageBox.warning(self, 'Incorrect path', 'Path not exists!\n'
                                                            'Check mdk archive path.',
                                    QMessageBox.StandardButton.Ok)
                return
            if not zipfile.is_zipfile(mdk_path):
                self.ui.mdk_path_line_edit.setStyleSheet('border: 1px solid red')
                QMessageBox.warning(self, 'Incorrect path', 'Path is not to zip archive!\n'
                                                            'Check mdk archive path.',
                                    QMessageBox.StandardButton.Ok)
                return
            with zipfile.ZipFile(mdk_path) as mdk:
                try:
                    with mdk.open('build.gradle'):
                        pass
                except KeyError:
                    self.ui.mdk_path_line_edit.setStyleSheet('border: 1px solid red')
                    QMessageBox.warning(self, 'Incorrect path', '"build.gradle" not found in mdk!\n'
                                                                'Check that mdk is valid.',
                                        QMessageBox.StandardButton.Ok)
                    return
        if not self.ui.deobf_check_box.isChecked() and not self.ui.decomp_check_box.isChecked():
            QMessageBox.warning(self, 'Incorrect configuration', 'With this configuration program will do nothing.',
                                QMessageBox.StandardButton.Ok)
            return
        self.serialized_widgets = self.serialize_to_dict()
        self.progress_window = MDGProgressWindow(self)
        self.progress_window.show()
        self.setEnabled(False)
        self.hide()
        self.progress_window.start()

    def serialize_to_dict(self) -> dict[str, Union[dict[str, Any], list[str]]]:
        out = defaultdict(dict)
        members = [attr for attr in dir(self.ui) if not callable(getattr(self.ui, attr)) and not attr.startswith('__')]
        for member_name in members:
            member_object = getattr(self.ui, member_name)
            member_attrs = [attr for attr in dir(member_object) if not attr.startswith('__')]
            required_fields = ('text', 'value', 'isChecked', 'isEnabled')
            for field in required_fields:
                if field in member_attrs:
                    out[member_name][field] = getattr(member_object, field)()
        return out

    def decomp_cmd_check_failed(self, title: str, text: str) -> None:
        self.ui.decomp_cmd_line_edit.setStyleSheet('border: 1px solid red')
        self.critical_from_progress_window(title, text)

    def critical_from_progress_window(self, title: str, text: str) -> None:
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

    def select_mods_button(self) -> None:
        selected_dir = QFileDialog.getExistingDirectory(self, self.tr('Select mods folder'), '',
                                                        QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        if selected_dir == '':
            return
        self.ui.mods_path_line_edit.setText(selected_dir)

    def select_mdk_button(self) -> None:
        selected_file = QFileDialog.getOpenFileName(self,
                                                    self.tr('Select mdk archive'), '',
                                                    self.tr('Archive files (*.zip)'))[0]
        if selected_file == '':
            return
        self.ui.mdk_path_line_edit.setText(selected_file)

    def deobf_checkbox_changed(self, state: int) -> None:
        self.ui.deobf_failed_group_box.setEnabled(state == 2)
        self.ui.deobf_threads_group_box.setEnabled(state == 2)
        self.check_mdk_needed()

    def decomp_checkbox_changed(self, state: int) -> None:
        if state != 2:
            self.was_decomp_enabled = self.ui.deobf_failed_radio_decompile.isChecked()
            if self.was_decomp_enabled:
                self.ui.deobf_failed_radio_interrupt.setChecked(True)
        elif self.was_decomp_enabled:
            self.ui.deobf_failed_radio_decompile.setChecked(True)
            self.was_decomp_enabled = False
        self.ui.deobf_failed_radio_decompile.setEnabled(state == 2)

        self.ui.merge_group_box.setEnabled(state == 2 and self.ui.merge_check_box.isChecked())
        self.ui.patch_mdk_group_box.setEnabled(state == 2 and self.ui.merge_check_box.isChecked())

        self.ui.merge_check_box.setEnabled(state == 2)
        self.ui.decomp_threads_group_box.setEnabled(state == 2)
        self.ui.decomp_cmd_groupbox.setEnabled(state == 2)

    def merge_checkbox_changed(self, state: int) -> None:
        self.ui.merge_group_box.setEnabled(state == 2)
        self.ui.patch_mdk_group_box.setEnabled(state == 2)
        self.check_mdk_needed()

    def check_mdk_needed(self) -> None:
        self.ui.mdk_path_vertical_group_box.setEnabled(
            self.ui.deobf_check_box.isChecked() or self.ui.merge_check_box.isChecked())

    def closeEvent(self, event: QCloseEvent) -> None:
        event.accept()
        sys.exit()

    def set_path_completer(self, line_edit: QLineEdit) -> None:
        fs_model = QFileSystemModel(line_edit)
        fs_model.setRootPath('')
        fs_completer = QCompleter(fs_model, self)
        line_edit.setCompleter(fs_completer)
