# This Python file uses the following encoding: utf-8
import os.path
import subprocess
import sys

from PySide6.QtGui import QTextCursor, QColor
from PySide6.QtWidgets import QMainWindow, QMessageBox

from MDGLogic.DeobfuscationMainThread import FailLogic
from MDGui.Ui_MDGResultWindow import Ui_MDGResultWindow


class MDGResultWindow(QMainWindow):

    def __init__(self, progress_window, parent=None):
        super().__init__(parent)
        self.ui = Ui_MDGResultWindow()
        self.ui.setupUi(self)
        self.progress_window = progress_window

        self.ui.deobfuscated_mods_button.setEnabled(os.path.exists(os.path.join('result', 'deobfuscated_mods')))
        self.ui.decompiled_mods_button.setEnabled(os.path.exists(os.path.join('result', 'decompiled_mods')))
        if not os.path.exists(os.path.join('result', 'merged_mdk')):
            self.ui.merged_mdk_button.setEnabled(False)
            self.ui.intellij_idea_button.setEnabled(False)

        self.ui.close_button.clicked.connect(self.hide)
        self.ui.deobfuscated_mods_button.clicked.connect(self.deobfuscated_mods_button)
        self.ui.decompiled_mods_button.clicked.connect(self.decompiled_mods_button)
        self.ui.merged_mdk_button.clicked.connect(self.merged_mdk_button)
        self.ui.intellij_idea_button.clicked.connect(self.intellij_idea_button)
        self.ui.exit_button.clicked.connect(sys.exit)
        self.ui.close_button.clicked.connect(self.close_button)

        if self.progress_window.failed_deobfuscation_mods:
            for mod_name in self.progress_window.failed_deobfuscation_mods:
                match self.progress_window.fail_logic:
                    case FailLogic.SKIP:
                        self.append_logger('orange',
                                           f'Finished deobfuscation of {mod_name} with error. Mod was be skipped.')

                    case FailLogic.DECOMPILE:
                        self.append_logger('orange',
                                           f'Finished deobfuscation of {mod_name} with error. Mod was decompiled without deofuscation.')
        else:
            self.append_logger('green', 'Finished without errors.')

    def open_folder(self, path):
        os.startfile(os.path.realpath(path))

    def deobfuscated_mods_button(self):
        self.open_folder(os.path.join('result', 'deobfuscated_mods'))

    def decompiled_mods_button(self):
        self.open_folder(os.path.join('result', 'decompiled_mods'))

    def merged_mdk_button(self):
        self.open_folder(os.path.join('result', 'merged_mdk'))

    def intellij_idea_button(self):
        try:
            subprocess.Popen(['idea64.exe', os.path.join('result', 'merged_mdk')])
        except FileNotFoundError:
            QMessageBox.warning(self, 'IntelliJ IDEA not found',
                                'Can\'t open "result/merged_mdk" as project in IntelliJ IDEA\n'
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
