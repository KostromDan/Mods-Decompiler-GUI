# This Python file uses the following encoding: utf-8
import os.path
import subprocess
import sys

from PySide6.QtGui import QTextCursor, QColor, QCloseEvent
from PySide6.QtWidgets import QMainWindow, QMessageBox

from MDGLogic.Deobfuscation.DeobfuscatioUtils import FailLogic
from MDGUi.generated.Ui_MDGResultWindow import Ui_MDGResultWindow
from MDGUtil import PathUtils


class MDGResultWindow(QMainWindow):

    def __init__(self, progress_window) -> None:
        super().__init__()
        self.ui = Ui_MDGResultWindow()
        self.ui.setupUi(self)
        self.progress_window = progress_window

        self.ui.deobfuscated_mods_button.setEnabled(os.path.exists(PathUtils.DEOBFUSCATED_MODS_PATH))
        self.ui.decompiled_mods_button.setEnabled(os.path.exists(PathUtils.DECOMPILED_MODS_PATH))
        if not os.path.exists(PathUtils.MERGED_MDK_PATH):
            self.ui.merged_mdk_button.setEnabled(False)
            self.ui.intellij_idea_button.setEnabled(False)
            self.ui.eclipse_button.setEnabled(False)

        self.ui.close_button.clicked.connect(self.hide)
        self.ui.deobfuscated_mods_button.clicked.connect(lambda e: self.open_folder(PathUtils.DEOBFUSCATED_MODS_PATH))
        self.ui.decompiled_mods_button.clicked.connect(lambda e: self.open_folder(PathUtils.DECOMPILED_MODS_PATH))
        self.ui.merged_mdk_button.clicked.connect(lambda e: self.open_folder(PathUtils.MERGED_MDK_PATH))
        self.ui.intellij_idea_button.clicked.connect(self.intellij_idea_button)
        self.ui.eclipse_button.clicked.connect(self.eclipse_button)
        self.ui.exit_button.clicked.connect(self.exit_button)
        self.ui.close_button.clicked.connect(self.close_button)
        self.ui.open_log_button.clicked.connect(PathUtils.open_log)

        if self.progress_window.failed_deobfuscation_mods or self.progress_window.failed_decompilation_mods:
            for mod_name in self.progress_window.failed_deobfuscation_mods:
                match self.progress_window.fail_logic:
                    case FailLogic.SKIP:
                        self.append_logger('orange',
                                           f'Finished deobfuscation of {mod_name} with error. '
                                           f'Mod was skipped.')

                    case FailLogic.DECOMPILE:
                        self.append_logger('orange',
                                           f'Finished deobfuscation of {mod_name} with error. '
                                           f'Mod was decompiled without deofuscation.')
            for mod_name in self.progress_window.failed_decompilation_mods:
                self.append_logger('orange', (
                    f'Finished decompilation of {mod_name} with error. '
                    f"Out directory is empty or doesn't contain a single *.java file"))
        else:
            self.append_logger('green', 'Finished without errors.')

    def open_folder(self, path: str | os.PathLike) -> None:
        os.startfile(os.path.realpath(path))

    def intellij_idea_button(self) -> None:
        try:
            subprocess.Popen(['idea64.exe', PathUtils.MERGED_MDK_PATH])
        except FileNotFoundError:
            QMessageBox.warning(self, 'IntelliJ IDEA not found',
                                f"Can't open {PathUtils.MERGED_MDK_PATH} as project in IntelliJ IDEA\n"
                                'due to "idea64.exe" not found!',
                                QMessageBox.StandardButton.Ok)

    def eclipse_button(self) -> None:
        eclipse_paths = PathUtils.get_eclipse_paths()
        if not eclipse_paths:
            QMessageBox.warning(self, 'Eclipse not found',
                                f"Can't open {PathUtils.MERGED_MDK_PATH} as project in Eclipse\n"
                                'due to "eclipse.exe" not found in Start Menu\\Programs!',
                                QMessageBox.StandardButton.Ok)
            return
        try:
            subprocess.Popen([eclipse_paths[0], PathUtils.MERGED_MDK_PATH])
        except FileNotFoundError:
            pass

    def close_button(self) -> None:
        self.progress_window.setEnabled(True)
        self.progress_window.show()
        self.destroy()

    def exit_button(self) -> None:
        self.destroy()
        sys.exit()

    def closeEvent(self, event: QCloseEvent) -> None:
        event.accept()
        self.hide()
        sys.exit()

    def append_logger(self, color: str, msg: str) -> None:
        cursor = self.ui.result_text_edit.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.movePosition(QTextCursor.End)

        line_format = cursor.charFormat()
        line_format.setForeground(QColor(color))
        cursor.setCharFormat(line_format)

        cursor.insertText(msg)
        cursor.insertText('\n')
