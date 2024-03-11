# This Python file uses the following encoding: utf-8
import os.path
import subprocess
import sys

from PySide6.QtGui import QTextCursor, QColor
from PySide6.QtWidgets import QMainWindow, QMessageBox

from MDGLogic.DeobfuscationMainThread import FailLogic
from MDGUtil import PathUtils
from MDGui.Ui_MDGResultWindow import Ui_MDGResultWindow


class MDGResultWindow(QMainWindow):

    def __init__(self, progress_window, parent=None):
        super().__init__(parent)
        self.ui = Ui_MDGResultWindow()
        self.ui.setupUi(self)
        self.progress_window = progress_window

        self.ui.deobfuscated_mods_button.setEnabled(os.path.exists(PathUtils.DEOBFUSCATED_MODS_PATH))
        self.ui.decompiled_mods_button.setEnabled(os.path.exists(PathUtils.DECOMPILED_MODS_PATH))
        if not os.path.exists(PathUtils.MERGED_MDK_PATH):
            self.ui.merged_mdk_button.setEnabled(False)
            self.ui.intellij_idea_button.setEnabled(False)

        self.ui.close_button.clicked.connect(self.hide)
        self.ui.deobfuscated_mods_button.clicked.connect(self.deobfuscated_mods_button)
        self.ui.decompiled_mods_button.clicked.connect(self.decompiled_mods_button)
        self.ui.merged_mdk_button.clicked.connect(self.merged_mdk_button)
        self.ui.intellij_idea_button.clicked.connect(self.intellij_idea_button)
        self.ui.exit_button.clicked.connect(sys.exit)
        self.ui.close_button.clicked.connect(self.close_button)

        if self.progress_window.failed_deobfuscation_mods or self.progress_window.failed_decompilation_mods:
            for mod_name in self.progress_window.failed_deobfuscation_mods:
                match self.progress_window.fail_logic:
                    case FailLogic.SKIP:
                        self.append_logger('orange',
                                           f'Finished deobfuscation of {mod_name} with error. '
                                           f'Mod was be skipped.')

                    case FailLogic.DECOMPILE:
                        self.append_logger('orange',
                                           f'Finished deobfuscation of {mod_name} with error. '
                                           f'Mod was decompiled without deofuscation.')
            for mod_name in self.progress_window.failed_decompilation_mods:
                self.append_logger('orange', (
                    f'Finished decompilation of {mod_name} with error. '
                    f'Out directory is empty or doesn\'t contain a single *.java file'))
        else:
            self.append_logger('green', 'Finished without errors.')

    def open_folder(self, path):
        os.startfile(os.path.realpath(path))

    def deobfuscated_mods_button(self):
        self.open_folder(PathUtils.DEOBFUSCATED_MODS_PATH)

    def decompiled_mods_button(self):
        self.open_folder(PathUtils.DECOMPILED_MODS_PATH)

    def merged_mdk_button(self):
        self.open_folder(PathUtils.MERGED_MDK_PATH)

    def intellij_idea_button(self):
        try:
            subprocess.Popen(['idea64.exe', PathUtils.MERGED_MDK_PATH])
        except FileNotFoundError:
            QMessageBox.warning(self, 'IntelliJ IDEA not found',
                                f'Can\'t open {PathUtils.MERGED_MDK_PATH} as project in IntelliJ IDEA\n'
                                'due to "idea64.exe" not found!',
                                QMessageBox.StandardButton.Ok)

    def close_button(self):
        self.progress_window.setEnabled(True)
        self.progress_window.show()
        self.destroy()

    def append_logger(self, color, msg):
        cursor = self.ui.result_text_edit.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.movePosition(QTextCursor.End)

        line_format = cursor.charFormat()
        line_format.setForeground(QColor(color))
        cursor.setCharFormat(line_format)

        cursor.insertText(msg)
        cursor.insertText('\n')
