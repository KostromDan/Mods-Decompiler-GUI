# This Python file uses the following encoding: utf-8
import multiprocessing
import os
import sys
import zipfile
from collections import defaultdict

from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTextBrowser, QFileSystemModel, QCompleter

from MDGUtil.LocalConfig import LocalConfig, DEFAULT_DECOMPILER_CMD
from MDGWindow.MDGHelpWindow import MDGHelpWindow
from MDGWindow.MDGProgressWindow import MDGProgressWindow
from MDGui.Ui_MDGMainWindow import Ui_MDGMainWindow


class MDGMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MDGMainWindow()
        self.ui.setupUi(self)

        self.config = LocalConfig()
        self.was_decomp_enabled = False

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

        self.ui.mods_path_vertical_group_box.dragEnterEvent = self.drag_enter_event_mods
        self.ui.mods_path_vertical_group_box.dragLeaveEvent = self.drag_leave_event_mods
        self.ui.mods_path_vertical_group_box.dropEvent = self.drop_event_mods

        self.ui.mdk_path_vertical_group_box.dragEnterEvent = self.drag_enter_event_mdk
        self.ui.mdk_path_vertical_group_box.dragLeaveEvent = self.drag_leave_event_mdk
        self.ui.mdk_path_vertical_group_box.dropEvent = self.drop_event_mdk

        self.ui.start_button.clicked.connect(self.start_button)

        self.ui.mods_path_line_edit.setText(self.config.get('mods_line_edit'))
        self.ui.mods_path_line_edit.textChanged.connect(self.mods_line_edit_changed)

        self.ui.mdk_path_line_edit.setText(self.config.get('mdk_line_edit'))
        self.ui.mdk_path_line_edit.textChanged.connect(self.mdk_line_edit_changed)

        if self.config.get('deobf_threads') == '':
            self.config.set('deobf_threads', multiprocessing.cpu_count())
        if self.config.get('decomp_threads') == '':
            self.config.set('decomp_threads', multiprocessing.cpu_count())

        self.ui.deobf_threads_horizontal_slider.valueChanged.connect(self.deobf_threads_horizontal_slider_value_changed)
        self.ui.decomp_threads_horizontal_slider.valueChanged.connect(
            self.decomp_threads_horizontal_slider_value_changed)

        self.ui.deobf_threads_horizontal_slider.setValue(self.config.get('deobf_threads'))
        self.ui.decomp_threads_horizontal_slider.setValue(self.config.get('decomp_threads'))

        self.ui.deobf_threads_spin_box.valueChanged.connect(self.deobf_threads_spin_box_value_changed)
        self.ui.decomp_threads_spin_box.valueChanged.connect(self.decomp_threads_spin_box_value_changed)

        self.ui.help_mdk_button.clicked.connect(self.help_mdk_button_clicked)
        self.ui.help_deobf_button.clicked.connect(self.help_deobf_button_clicked)
        self.ui.help_merge_button.clicked.connect(self.help_merge_button_clicked)
        self.ui.help_mods_button.clicked.connect(self.help_mods_button_clicked)
        self.ui.help_merge_button_2.clicked.connect(self.help_merge_2_button_clicked)
        self.ui.help_decomp_button.clicked.connect(self.help_decomp_button_clicked)
        self.ui.help_deobf_failed_button.clicked.connect(self.help_deobf_failed_button_clicked)
        self.ui.help_sources_button.clicked.connect(self.help_sources_button_clicked)
        self.ui.help_decomp_threads_button.clicked.connect(self.help_threads_button_clicked)
        self.ui.help_deobf_threads_button.clicked.connect(self.help_threads_button_clicked)
        self.ui.help_decomp_cmd_button.clicked.connect(self.help_decomp_cmd_button_clicked)
        self.ui.help_cache_button.clicked.connect(self.help_cache_button_clicked)

        # added to set the file system completer for mods_path_line_edit
        self.set_path_completer(self.ui.mods_path_line_edit)
        self.set_path_completer(self.ui.mdk_path_line_edit)

        self.help_window = MDGHelpWindow()

        self.resize(self.width(), self.minimumSizeHint().height())

        self.ui.decomp_cmd_reset_button.clicked.connect(self.reset_decomp_cmd)
        self.ui.decomp_cmd_line_edit.textChanged.connect(self.decomp_cmd_line_edit_changed)

        self.ui.decomp_cmd_line_edit.setText(
            self.config.get('decomp_cmd') if self.config.get('decomp_cmd') != '' else DEFAULT_DECOMPILER_CMD)

    def decomp_cmd_line_edit_changed(self, value):
        self.ui.decomp_cmd_reset_button.setEnabled(value != DEFAULT_DECOMPILER_CMD)
        self.config.set('decomp_cmd', value if value != DEFAULT_DECOMPILER_CMD else '')
        self.ui.decomp_cmd_line_edit.setStyleSheet('')

    def reset_decomp_cmd(self):
        self.ui.decomp_cmd_line_edit.setText(DEFAULT_DECOMPILER_CMD)

    def start_help_window(self, help_about):
        self.help_window.show()
        browsers = self.help_window.ui.scrollAreaWidgetContents.findChildren(QTextBrowser)
        for browser in browsers:
            browser.setStyleSheet('')
        help_about.setStyleSheet('border: 1px solid red')
        self.help_window.ui.scrollArea.ensureWidgetVisible(help_about)

    def help_mods_button_clicked(self):
        self.start_help_window(self.help_window.ui.mods_path)

    def help_cache_button_clicked(self):
        self.start_help_window(self.help_window.ui.cache)

    def help_decomp_cmd_button_clicked(self):
        self.start_help_window(self.help_window.ui.decomp_cmd)

    def help_mdk_button_clicked(self):
        self.start_help_window(self.help_window.ui.mdk_path)

    def help_sources_button_clicked(self):
        self.start_help_window(self.help_window.ui.patch_mdk)

    def help_deobf_button_clicked(self):
        self.start_help_window(self.help_window.ui.deobf_mods)

    def help_merge_button_clicked(self):
        self.start_help_window(self.help_window.ui.merge)

    def help_threads_button_clicked(self):
        self.start_help_window(self.help_window.ui.threads)

    def help_deobf_failed_button_clicked(self):
        self.start_help_window(self.help_window.ui.deobf_failed)

    def help_merge_2_button_clicked(self):
        self.start_help_window(self.help_window.ui.merge_resources)

    def help_decomp_button_clicked(self):
        self.start_help_window(self.help_window.ui.decomp_mods)

    def deobf_threads_horizontal_slider_value_changed(self, value):
        self.ui.deobf_threads_spin_box.setValue(value)
        self.config.set('deobf_threads', value)

    def deobf_threads_spin_box_value_changed(self, value):
        self.ui.deobf_threads_horizontal_slider.setValue(value)

    def decomp_threads_horizontal_slider_value_changed(self, value):
        self.ui.decomp_threads_spin_box.setValue(value)
        self.config.set('decomp_threads', value)

    def decomp_threads_spin_box_value_changed(self, value):
        self.ui.decomp_threads_horizontal_slider.setValue(value)

    def mods_line_edit_changed(self, text):
        self.config.set('mods_line_edit', text)
        self.ui.mods_path_line_edit.setStyleSheet('')

    def mdk_line_edit_changed(self, text):
        self.config.set('mdk_line_edit', text)
        self.ui.mdk_path_line_edit.setStyleSheet('')

    def start_button(self):
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

    def serialize_to_dict(self):
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

    def decomp_cmd_check_failed(self, s1, s2):
        self.ui.decomp_cmd_line_edit.setStyleSheet('border: 1px solid red')
        self.critical_from_progress_window(s1, s2)

    def critical_from_progress_window(self, s1, s2):
        self.setEnabled(True)
        self.show()
        QMessageBox.critical(self, s1, s2, QMessageBox.StandardButton.Ok)

    def drag_enter_event(self, event, element):
        if event.mimeData().hasUrls():
            event.accept()
            element.setObjectName('vertical_group_box')
            element.setStyleSheet('#vertical_group_box { border: 2px solid blue; }')
        else:
            event.ignore()

    def drag_enter_event_mods(self, event):
        self.drag_enter_event(event, self.ui.mods_path_vertical_group_box)

    def drag_leave_event_mods(self, event):
        self.ui.mods_path_vertical_group_box.setStyleSheet('')

    def drag_enter_event_mdk(self, event):
        self.drag_enter_event(event, self.ui.mdk_path_vertical_group_box)

    def drag_leave_event_mdk(self, event):
        self.ui.mdk_path_vertical_group_box.setStyleSheet('')

    def drop_event_mods(self, event):
        result = self.drop_event(event)
        if result is not None:
            self.ui.mods_path_line_edit.setText(result)
        self.ui.mods_path_vertical_group_box.setStyleSheet('')

    def drop_event_mdk(self, event):
        result = self.drop_event(event)
        if result is not None:
            self.ui.mdk_path_line_edit.setText(result)
        self.ui.mdk_path_vertical_group_box.setStyleSheet('')

    def drop_event(self, event):
        mime_data = event.mimeData()
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

    def select_mods_button(self):
        selected_dir = QFileDialog.getExistingDirectory(self, self.tr('Select mods folder'), '',
                                                        QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        if selected_dir == '':
            return
        self.ui.mods_path_line_edit.setText(selected_dir)

    def select_mdk_button(self):
        selected_file = QFileDialog.getOpenFileName(self,
                                                    self.tr('Select mdk archive'), '',
                                                    self.tr('Archive files (*.zip)'))[0]
        if selected_file == '':
            return
        self.ui.mdk_path_line_edit.setText(selected_file)

    def deobf_checkbox_changed(self, state):
        self.ui.deobf_failed_group_box.setEnabled(state == 2)
        self.ui.deobf_threads_group_box.setEnabled(state == 2)
        self.check_mdk_needed()

    def decomp_checkbox_changed(self, state):
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

    def merge_checkbox_changed(self, state):
        self.ui.merge_group_box.setEnabled(state == 2)
        self.ui.patch_mdk_group_box.setEnabled(state == 2)
        self.check_mdk_needed()

    def check_mdk_needed(self):
        self.ui.mdk_path_vertical_group_box.setEnabled(
            self.ui.deobf_check_box.isChecked() or self.ui.merge_check_box.isChecked())

    def closeEvent(self, event):
        event.accept()
        sys.exit()

    def set_path_completer(self, line_edit):
        fs_model = QFileSystemModel(line_edit)
        fs_model.setRootPath("")
        fs_completer = QCompleter(fs_model, self)
        line_edit.setCompleter(fs_completer)