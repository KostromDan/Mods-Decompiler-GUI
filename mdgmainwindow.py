# This Python file uses the following encoding: utf-8
import os
import sys

from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QCompleter, QFileSystemModel, QMessageBox
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MDGMainWindow
from MDGUtils.LocalConfig import LocalConfig


class MDGMainWindow(QMainWindow):
    was_decomp_enabled = False
    config = LocalConfig()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MDGMainWindow()
        self.ui.setupUi(self)

        if self.config.is_first_launch():
            QMessageBox.information(self, 'First launch information', f'Welcome to MDG (Mods Decompiler Gui)!\n'
                                                                      f'Please check licence of all mods, on which you going to use this tool,'
                                                                      f'otherwise usage of this tool can lead to license infrigment!\n'
                                                                      f'If you not shure how to use tool, which options do you need, click "?",\n'
                                                                      f'it will provide useful information and tips.',
                                    QMessageBox.StandardButton.Ok)

        self.ui.deobf_check_box.stateChanged.connect(self.deobf_checkbox_changed)
        self.ui.merge_check_box.stateChanged.connect(self.merge_checkbox_changed)
        self.ui.decomp_check_box.stateChanged.connect(self.decomp_checkbox_changed)

        self.ui.select_mods_button.clicked.connect(self.select_mods_button)
        self.ui.select_mdk_button.clicked.connect(self.select_mdk_button)

        self.ui.mods_path_vertical_group_box.dragEnterEvent = self.drag_enter_event
        self.ui.mdk_path_vertical_group_box.dragEnterEvent = self.drag_enter_event
        self.ui.mods_path_vertical_group_box.dropEvent = self.drop_event_mods
        self.ui.mdk_path_vertical_group_box.dropEvent = self.drop_event_mdk

        self.ui.start_button.clicked.connect(self.start_button)

        self.ui.mods_path_line_edit.setText(self.config.get("mods_line_edit"))
        self.ui.mods_path_line_edit.textChanged.connect(self.mods_line_edit_changed)

        self.ui.mdk_path_line_edit.setText(self.config.get("mdk_line_edit"))
        self.ui.mdk_path_line_edit.textChanged.connect(self.mdk_line_edit_changed)

        # self.completer = QCompleter(self) # This doesn't work... Fix later...
        # self.completer.setModel(QFileSystemModel(self.completer))
        # self.ui.mods_path_line_edit.setCompleter(self.completer)

    def mods_line_edit_changed(self, text):
        self.config.set("mods_line_edit", text)

    def mdk_line_edit_changed(self, text):
        self.config.set("mdk_line_edit", text)

    def start_button(self):
        pass

    def drag_enter_event(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def drop_event_mods(self, event):
        result = self.drop_event(event)
        if result is not None:
            self.ui.mods_path_line_edit.setText(result)

    def drop_event_mdk(self, event):
        result = self.drop_event(event)
        if result is not None:
            self.ui.mdk_path_line_edit.setText(result)

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
        selected_dir = QFileDialog.getExistingDirectory(self, self.tr("Select mods folder"), "",
                                                        QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        if selected_dir == "":
            return
        self.ui.mods_path_line_edit.setText(selected_dir)

    def select_mdk_button(self):
        selected_file = QFileDialog.getOpenFileName(self,
                                                    self.tr("Select mdk archive"), "",
                                                    self.tr("Archive files (*.zip)"))[0]
        if selected_file == "":
            return
        self.ui.mdk_path_line_edit.setText(selected_file)

    def deobf_checkbox_changed(self, state):
        self.ui.deobf_failed_group_box.setEnabled(state == 2)
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

    def merge_checkbox_changed(self, state):
        self.ui.merge_group_box.setEnabled(state == 2)
        self.ui.patch_mdk_group_box.setEnabled(state == 2)
        self.check_mdk_needed()

    def check_mdk_needed(self):
        self.ui.mdk_path_vertical_group_box.setEnabled(
            self.ui.deobf_check_box.isChecked() or self.ui.merge_check_box.isChecked())


if __name__ == "__main__":
    if not (getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')):  # not inside PyInstaller
        os.system("venv\\Scripts\\activate && pyside6-uic form.ui -o ui_form.py")
    app = QApplication(sys.argv)
    widget = MDGMainWindow()
    widget.show()
    sys.exit(app.exec())
