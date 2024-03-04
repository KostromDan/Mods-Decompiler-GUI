# This Python file uses the following encoding: utf-8

from PySide6.QtGui import QTextCursor, QColor
from PySide6.QtWidgets import QMainWindow

from MDGLogic.DeobfuscationMainThread import FailLogic
from MDGui.Ui_MDGResultWindow import Ui_MDGResultWindow


class MDGResultWindow(QMainWindow):
    def append_logger(self, color, msg):
        cursor = self.ui.result_text_edit.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.movePosition(QTextCursor.End)

        line_format = cursor.charFormat()
        line_format.setForeground(QColor(color))
        cursor.setCharFormat(line_format)

        cursor.insertText(msg)
        cursor.insertText('\n')

    def __init__(self, progress_window, parent=None):
        super().__init__(parent)
        self.ui = Ui_MDGResultWindow()
        self.ui.setupUi(self)
        self.progress_window = progress_window

        self.ui.close_button.clicked.connect(self.hide)

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
            self.append_logger('green','Finished without errors.')